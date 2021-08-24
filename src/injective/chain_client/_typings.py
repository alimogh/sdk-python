import sys

from typing import Literal, TypedDict
# for python3.7, you need to change this to the followings
# from typing_extensions import Literal, TypedDict

# Valid transaction broadcast modes for the `POST /txs` endpoint of the
# Cosmos REST API.
SyncMode = Literal["sync", "async", "block"]


class Wallet(TypedDict):
    seed: str
    derivation_path: str
    private_key: bytes
    public_key: bytes
    address: str
