import asyncio
import aiohttp
import logging
import base64
import json
import ecdsa
import sha3
import grpc

from typing import Any, Dict, List
from injective.chain_client._wallet import (
    generate_wallet,
    privkey_to_address,
    privkey_to_pubkey,
    pubkey_to_address,
    seed_to_privkey,
    DEFAULT_BECH32_HRP,
)

from injective.chain_client._typings import SyncMode

MIN_GAS_PRICE = 500000000

class Transaction:

    def __init__(
        self,
        *,
        privkey: bytes,
        account_num: int,
        sequence: int,
        fee: int,
        gas: int,
        fee_denom: str = "inj",
        memo: str = "",
        chain_id: str = "injective-888",
        hrp: str = DEFAULT_BECH32_HRP,
        sync_mode: SyncMode = "block",
    ) -> None:
        self._privkey = privkey
        self._account_num = account_num
        self._sequence = sequence
        self._fee = fee
        self._fee_denom = fee_denom
        self._gas = gas
        self._memo = memo
        self._chain_id = chain_id
        self._hrp = hrp
        self._sync_mode = sync_mode
        self._msgs: List[dict] = []

    def msg_cancel_derivative_order(self, subaccount: str, market_id: str, order_hash: str) -> None:
        msg = {
            "type": "exchange/MsgCancelDerivativeOrder",
            "value": {
                "sender": privkey_to_address(self._privkey, hrp=self._hrp),
                "subaccount_id": subaccount,
                "market_id": market_id,
                "order_hash": order_hash,
            },
        }
        self._msgs.append(msg)

    def get_signed(self) -> str:
        pubkey = privkey_to_pubkey(self._privkey)
        base64_pubkey = base64.b64encode(pubkey).decode("utf-8")
        signed_tx = {
            "tx": {
                "msg": self._msgs,
                "fee": {
                    "gas": str(self._gas),
                    "amount": [{"denom": self._fee_denom, "amount": str(self._fee)}],
                },
                "memo": self._memo,
                "signatures": [
                    {
                        "signature": self._sign(),
                        "pub_key": {"type": "injective/PubKeyEthSecp256k1", "value": base64_pubkey},
                        "account_number": str(self._account_num),
                        "sequence": str(self._sequence),
                    }
                ],
            },
            "mode": self._sync_mode,
        }
        return json.dumps(signed_tx, separators=(",", ":"))

    def _sign(self) -> str:
        message_str = json.dumps(
            self._get_sign_message(), separators=(",", ":"), sort_keys=True)
        message_bytes = message_str.encode("utf-8")

        privkey = ecdsa.SigningKey.from_string(
            self._privkey, curve=ecdsa.SECP256k1)
        signature_compact_keccak = privkey.sign_deterministic(
            message_bytes, hashfunc=sha3.keccak_256, sigencode=ecdsa.util.sigencode_string_canonize
        )
        signature_base64_str = base64.b64encode(
            signature_compact_keccak).decode("utf-8")
        return signature_base64_str

    def _get_sign_message(self) -> Dict[str, Any]:
        return {
            "chain_id": self._chain_id,
            "account_number": str(self._account_num),
            "fee": {
                "gas": str(self._gas),
                "amount": [{"amount": str(self._fee), "denom": self._fee_denom}],
            },
            "memo": self._memo,
            "sequence": str(self._sequence),
            "msgs": self._msgs,
        }

async def main() -> None:
    sender_pk = seed_to_privkey(
        "physical page glare junk return scale subject river token door mirror title"
    )
    sender_acc_addr = privkey_to_address(sender_pk)
    print("Sender Account:", sender_acc_addr)

    acc_num, acc_seq = await get_account_num_seq(sender_acc_addr)

    tx = Transaction(
        privkey=sender_pk,
        account_num=acc_num,
        sequence=acc_seq,
        gas=200000,
        fee=200000 * MIN_GAS_PRICE,
        sync_mode="block",
    )

    tx.msg_cancel_derivative_order (
        market_id = "0xd0f46edfba58827fe692aab7c8d46395d1696239fdf6aeddfa668b73ca82ea30",
        subaccount = "0xbdaedec95d563fb05240d6e01821008454c24c36000000000000000000000000",
        order_hash = "0xc8a42f4056fe3d0e6ae88b66b0cd192a992edc9073f3bf03c1a19f6b08c86901",
        )

    tx_json = tx.get_signed()

    print("Signed Tx:", tx_json)
    print("Sent Tx:", await post_tx(tx_json))

async def get_account_num_seq(address: str) -> (int, int):
    async with aiohttp.ClientSession() as session:
        async with session.request(
            'GET', 'http://staking-lcd-testnet.injective.network/cosmos/auth/v1beta1/accounts/' + address,
            headers={'Accept-Encoding': 'application/json'},
        ) as response:
            if response.status != 200:
                print(await response.text())
                raise ValueError("HTTP response status", response.status)

            resp = json.loads(await response.text())
            acc = resp['account']['base_account']
            return acc['account_number'], acc['sequence']

async def post_tx(tx_json: str):
    async with aiohttp.ClientSession() as session:
        async with session.request(
            'POST', 'http://staking-lcd-testnet.injective.network/txs', data=tx_json,
            headers={'Content-Type': 'application/json'},
        ) as response:
            if response.status != 200:
                print(await response.text())
                raise ValueError("HTTP response status", response.status)

            resp = json.loads(await response.text())
            if 'code' in resp:
                print("Response:", resp)
                raise ValueError('sdk error %d: %s' % (resp['code'], resp['raw_log']))

            return resp['txhash']

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.get_event_loop().run_until_complete(main())