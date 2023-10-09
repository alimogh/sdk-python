# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cosmwasm/wasm/v1/tx.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from cosmos.msg.v1 import msg_pb2 as cosmos_dot_msg_dot_v1_dot_msg__pb2
from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from cosmwasm.wasm.v1 import types_pb2 as cosmwasm_dot_wasm_dot_v1_dot_types__pb2
from cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
from amino import amino_pb2 as amino_dot_amino__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x19\x63osmwasm/wasm/v1/tx.proto\x12\x10\x63osmwasm.wasm.v1\x1a\x1e\x63osmos/base/v1beta1/coin.proto\x1a\x17\x63osmos/msg/v1/msg.proto\x1a\x14gogoproto/gogo.proto\x1a\x1c\x63osmwasm/wasm/v1/types.proto\x1a\x19\x63osmos_proto/cosmos.proto\x1a\x11\x61mino/amino.proto\"\xd1\x01\n\x0cMsgStoreCode\x12(\n\x06sender\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12(\n\x0ewasm_byte_code\x18\x02 \x01(\x0c\x42\x10\xe2\xde\x1f\x0cWASMByteCode\x12>\n\x16instantiate_permission\x18\x05 \x01(\x0b\x32\x1e.cosmwasm.wasm.v1.AccessConfig:!\x82\xe7\xb0*\x06sender\x8a\xe7\xb0*\x11wasm/MsgStoreCodeJ\x04\x08\x03\x10\x04J\x04\x08\x04\x10\x05\"E\n\x14MsgStoreCodeResponse\x12\x1b\n\x07\x63ode_id\x18\x01 \x01(\x04\x42\n\xe2\xde\x1f\x06\x43odeID\x12\x10\n\x08\x63hecksum\x18\x02 \x01(\x0c\"\xca\x02\n\x16MsgInstantiateContract\x12(\n\x06sender\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12\'\n\x05\x61\x64min\x18\x02 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12\x1b\n\x07\x63ode_id\x18\x03 \x01(\x04\x42\n\xe2\xde\x1f\x06\x43odeID\x12\r\n\x05label\x18\x04 \x01(\t\x12#\n\x03msg\x18\x05 \x01(\x0c\x42\x16\xfa\xde\x1f\x12RawContractMessage\x12_\n\x05\x66unds\x18\x06 \x03(\x0b\x32\x19.cosmos.base.v1beta1.CoinB5\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins\xa8\xe7\xb0*\x01:+\x82\xe7\xb0*\x06sender\x8a\xe7\xb0*\x1bwasm/MsgInstantiateContract\"Y\n\x1eMsgInstantiateContractResponse\x12)\n\x07\x61\x64\x64ress\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\x0c\"\xeb\x02\n\x17MsgInstantiateContract2\x12(\n\x06sender\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12\'\n\x05\x61\x64min\x18\x02 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12\x1b\n\x07\x63ode_id\x18\x03 \x01(\x04\x42\n\xe2\xde\x1f\x06\x43odeID\x12\r\n\x05label\x18\x04 \x01(\t\x12#\n\x03msg\x18\x05 \x01(\x0c\x42\x16\xfa\xde\x1f\x12RawContractMessage\x12_\n\x05\x66unds\x18\x06 \x03(\x0b\x32\x19.cosmos.base.v1beta1.CoinB5\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins\xa8\xe7\xb0*\x01\x12\x0c\n\x04salt\x18\x07 \x01(\x0c\x12\x0f\n\x07\x66ix_msg\x18\x08 \x01(\x08:,\x82\xe7\xb0*\x06sender\x8a\xe7\xb0*\x1cwasm/MsgInstantiateContract2\"Z\n\x1fMsgInstantiateContract2Response\x12)\n\x07\x61\x64\x64ress\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\x0c\"\x99\x02\n\x12MsgExecuteContract\x12(\n\x06sender\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12*\n\x08\x63ontract\x18\x02 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12#\n\x03msg\x18\x03 \x01(\x0c\x42\x16\xfa\xde\x1f\x12RawContractMessage\x12_\n\x05\x66unds\x18\x05 \x03(\x0b\x32\x19.cosmos.base.v1beta1.CoinB5\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins\xa8\xe7\xb0*\x01:\'\x82\xe7\xb0*\x06sender\x8a\xe7\xb0*\x17wasm/MsgExecuteContract\"*\n\x1aMsgExecuteContractResponse\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\x0c\"\xd5\x01\n\x12MsgMigrateContract\x12(\n\x06sender\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12*\n\x08\x63ontract\x18\x02 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12\x1b\n\x07\x63ode_id\x18\x03 \x01(\x04\x42\n\xe2\xde\x1f\x06\x43odeID\x12#\n\x03msg\x18\x04 \x01(\x0c\x42\x16\xfa\xde\x1f\x12RawContractMessage:\'\x82\xe7\xb0*\x06sender\x8a\xe7\xb0*\x17wasm/MsgMigrateContract\"*\n\x1aMsgMigrateContractResponse\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\x0c\"\xb8\x01\n\x0eMsgUpdateAdmin\x12(\n\x06sender\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12+\n\tnew_admin\x18\x02 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12*\n\x08\x63ontract\x18\x03 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString:#\x82\xe7\xb0*\x06sender\x8a\xe7\xb0*\x13wasm/MsgUpdateAdmin\"\x18\n\x16MsgUpdateAdminResponse\"\x89\x01\n\rMsgClearAdmin\x12(\n\x06sender\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12*\n\x08\x63ontract\x18\x03 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString:\"\x82\xe7\xb0*\x06sender\x8a\xe7\xb0*\x12wasm/MsgClearAdmin\"\x17\n\x15MsgClearAdminResponse\"|\n\x12\x41\x63\x63\x65ssConfigUpdate\x12\x1b\n\x07\x63ode_id\x18\x01 \x01(\x04\x42\n\xe2\xde\x1f\x06\x43odeID\x12I\n\x16instantiate_permission\x18\x02 \x01(\x0b\x32\x1e.cosmwasm.wasm.v1.AccessConfigB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01\"\xd8\x01\n\x1aMsgUpdateInstantiateConfig\x12(\n\x06sender\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12\x1b\n\x07\x63ode_id\x18\x02 \x01(\x04\x42\n\xe2\xde\x1f\x06\x43odeID\x12\x42\n\x1anew_instantiate_permission\x18\x03 \x01(\x0b\x32\x1e.cosmwasm.wasm.v1.AccessConfig:/\x82\xe7\xb0*\x06sender\x8a\xe7\xb0*\x1fwasm/MsgUpdateInstantiateConfig\"$\n\"MsgUpdateInstantiateConfigResponse\"\x9c\x01\n\x0fMsgUpdateParams\x12+\n\tauthority\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12\x33\n\x06params\x18\x02 \x01(\x0b\x32\x18.cosmwasm.wasm.v1.ParamsB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01:\'\x82\xe7\xb0*\tauthority\x8a\xe7\xb0*\x14wasm/MsgUpdateParams\"\x19\n\x17MsgUpdateParamsResponse\"\xb8\x01\n\x0fMsgSudoContract\x12+\n\tauthority\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12*\n\x08\x63ontract\x18\x02 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12#\n\x03msg\x18\x03 \x01(\x0c\x42\x16\xfa\xde\x1f\x12RawContractMessage:\'\x82\xe7\xb0*\tauthority\x8a\xe7\xb0*\x14wasm/MsgSudoContract\"\'\n\x17MsgSudoContractResponse\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\x0c\"\x91\x01\n\x0bMsgPinCodes\x12+\n\tauthority\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12\x30\n\x08\x63ode_ids\x18\x02 \x03(\x04\x42\x1e\xe2\xde\x1f\x07\x43odeIDs\xf2\xde\x1f\x0fyaml:\"code_ids\":#\x82\xe7\xb0*\tauthority\x8a\xe7\xb0*\x10wasm/MsgPinCodes\"\x15\n\x13MsgPinCodesResponse\"\x95\x01\n\rMsgUnpinCodes\x12+\n\tauthority\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12\x30\n\x08\x63ode_ids\x18\x02 \x03(\x04\x42\x1e\xe2\xde\x1f\x07\x43odeIDs\xf2\xde\x1f\x0fyaml:\"code_ids\":%\x82\xe7\xb0*\tauthority\x8a\xe7\xb0*\x12wasm/MsgUnpinCodes\"\x17\n\x15MsgUnpinCodesResponse\"\xf5\x03\n\x1eMsgStoreAndInstantiateContract\x12+\n\tauthority\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12(\n\x0ewasm_byte_code\x18\x03 \x01(\x0c\x42\x10\xe2\xde\x1f\x0cWASMByteCode\x12>\n\x16instantiate_permission\x18\x04 \x01(\x0b\x32\x1e.cosmwasm.wasm.v1.AccessConfig\x12\x12\n\nunpin_code\x18\x05 \x01(\x08\x12\'\n\x05\x61\x64min\x18\x06 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12\r\n\x05label\x18\x07 \x01(\t\x12#\n\x03msg\x18\x08 \x01(\x0c\x42\x16\xfa\xde\x1f\x12RawContractMessage\x12_\n\x05\x66unds\x18\t \x03(\x0b\x32\x19.cosmos.base.v1beta1.CoinB5\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins\xa8\xe7\xb0*\x01\x12\x0e\n\x06source\x18\n \x01(\t\x12\x0f\n\x07\x62uilder\x18\x0b \x01(\t\x12\x11\n\tcode_hash\x18\x0c \x01(\x0c:6\x82\xe7\xb0*\tauthority\x8a\xe7\xb0*#wasm/MsgStoreAndInstantiateContract\"a\n&MsgStoreAndInstantiateContractResponse\x12)\n\x07\x61\x64\x64ress\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\x0c\"\xb0\x01\n\x1fMsgAddCodeUploadParamsAddresses\x12+\n\tauthority\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12\'\n\taddresses\x18\x02 \x03(\tB\x14\xf2\xde\x1f\x10yaml:\"addresses\":7\x82\xe7\xb0*\tauthority\x8a\xe7\xb0*$wasm/MsgAddCodeUploadParamsAddresses\")\n\'MsgAddCodeUploadParamsAddressesResponse\"\xb6\x01\n\"MsgRemoveCodeUploadParamsAddresses\x12+\n\tauthority\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12\'\n\taddresses\x18\x02 \x03(\tB\x14\xf2\xde\x1f\x10yaml:\"addresses\"::\x82\xe7\xb0*\tauthority\x8a\xe7\xb0*\'wasm/MsgRemoveCodeUploadParamsAddresses\",\n*MsgRemoveCodeUploadParamsAddressesResponse\"\x9e\x02\n\x1aMsgStoreAndMigrateContract\x12+\n\tauthority\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12(\n\x0ewasm_byte_code\x18\x02 \x01(\x0c\x42\x10\xe2\xde\x1f\x0cWASMByteCode\x12>\n\x16instantiate_permission\x18\x03 \x01(\x0b\x32\x1e.cosmwasm.wasm.v1.AccessConfig\x12\x10\n\x08\x63ontract\x18\x04 \x01(\t\x12#\n\x03msg\x18\x05 \x01(\x0c\x42\x16\xfa\xde\x1f\x12RawContractMessage:2\x82\xe7\xb0*\tauthority\x8a\xe7\xb0*\x1fwasm/MsgStoreAndMigrateContract\"a\n\"MsgStoreAndMigrateContractResponse\x12\x1b\n\x07\x63ode_id\x18\x01 \x01(\x04\x42\n\xe2\xde\x1f\x06\x43odeID\x12\x10\n\x08\x63hecksum\x18\x02 \x01(\x0c\x12\x0c\n\x04\x64\x61ta\x18\x03 \x01(\x0c\"\xae\x01\n\x16MsgUpdateContractLabel\x12(\n\x06sender\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12\x11\n\tnew_label\x18\x02 \x01(\t\x12*\n\x08\x63ontract\x18\x03 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString:+\x82\xe7\xb0*\x06sender\x8a\xe7\xb0*\x1bwasm/MsgUpdateContractLabel\" \n\x1eMsgUpdateContractLabelResponse2\xd5\x0e\n\x03Msg\x12S\n\tStoreCode\x12\x1e.cosmwasm.wasm.v1.MsgStoreCode\x1a&.cosmwasm.wasm.v1.MsgStoreCodeResponse\x12q\n\x13InstantiateContract\x12(.cosmwasm.wasm.v1.MsgInstantiateContract\x1a\x30.cosmwasm.wasm.v1.MsgInstantiateContractResponse\x12t\n\x14InstantiateContract2\x12).cosmwasm.wasm.v1.MsgInstantiateContract2\x1a\x31.cosmwasm.wasm.v1.MsgInstantiateContract2Response\x12\x65\n\x0f\x45xecuteContract\x12$.cosmwasm.wasm.v1.MsgExecuteContract\x1a,.cosmwasm.wasm.v1.MsgExecuteContractResponse\x12\x65\n\x0fMigrateContract\x12$.cosmwasm.wasm.v1.MsgMigrateContract\x1a,.cosmwasm.wasm.v1.MsgMigrateContractResponse\x12Y\n\x0bUpdateAdmin\x12 .cosmwasm.wasm.v1.MsgUpdateAdmin\x1a(.cosmwasm.wasm.v1.MsgUpdateAdminResponse\x12V\n\nClearAdmin\x12\x1f.cosmwasm.wasm.v1.MsgClearAdmin\x1a\'.cosmwasm.wasm.v1.MsgClearAdminResponse\x12}\n\x17UpdateInstantiateConfig\x12,.cosmwasm.wasm.v1.MsgUpdateInstantiateConfig\x1a\x34.cosmwasm.wasm.v1.MsgUpdateInstantiateConfigResponse\x12\\\n\x0cUpdateParams\x12!.cosmwasm.wasm.v1.MsgUpdateParams\x1a).cosmwasm.wasm.v1.MsgUpdateParamsResponse\x12\\\n\x0cSudoContract\x12!.cosmwasm.wasm.v1.MsgSudoContract\x1a).cosmwasm.wasm.v1.MsgSudoContractResponse\x12P\n\x08PinCodes\x12\x1d.cosmwasm.wasm.v1.MsgPinCodes\x1a%.cosmwasm.wasm.v1.MsgPinCodesResponse\x12V\n\nUnpinCodes\x12\x1f.cosmwasm.wasm.v1.MsgUnpinCodes\x1a\'.cosmwasm.wasm.v1.MsgUnpinCodesResponse\x12\x89\x01\n\x1bStoreAndInstantiateContract\x12\x30.cosmwasm.wasm.v1.MsgStoreAndInstantiateContract\x1a\x38.cosmwasm.wasm.v1.MsgStoreAndInstantiateContractResponse\x12\x95\x01\n\x1fRemoveCodeUploadParamsAddresses\x12\x34.cosmwasm.wasm.v1.MsgRemoveCodeUploadParamsAddresses\x1a<.cosmwasm.wasm.v1.MsgRemoveCodeUploadParamsAddressesResponse\x12\x8c\x01\n\x1c\x41\x64\x64\x43odeUploadParamsAddresses\x12\x31.cosmwasm.wasm.v1.MsgAddCodeUploadParamsAddresses\x1a\x39.cosmwasm.wasm.v1.MsgAddCodeUploadParamsAddressesResponse\x12}\n\x17StoreAndMigrateContract\x12,.cosmwasm.wasm.v1.MsgStoreAndMigrateContract\x1a\x34.cosmwasm.wasm.v1.MsgStoreAndMigrateContractResponse\x12q\n\x13UpdateContractLabel\x12(.cosmwasm.wasm.v1.MsgUpdateContractLabel\x1a\x30.cosmwasm.wasm.v1.MsgUpdateContractLabelResponse\x1a\x05\x80\xe7\xb0*\x01\x42,Z&github.com/CosmWasm/wasmd/x/wasm/types\xc8\xe1\x1e\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmwasm.wasm.v1.tx_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z&github.com/CosmWasm/wasmd/x/wasm/types\310\341\036\000'
  _MSGSTORECODE.fields_by_name['sender']._options = None
  _MSGSTORECODE.fields_by_name['sender']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _MSGSTORECODE.fields_by_name['wasm_byte_code']._options = None
  _MSGSTORECODE.fields_by_name['wasm_byte_code']._serialized_options = b'\342\336\037\014WASMByteCode'
  _MSGSTORECODE._options = None
  _MSGSTORECODE._serialized_options = b'\202\347\260*\006sender\212\347\260*\021wasm/MsgStoreCode'
  _MSGSTORECODERESPONSE.fields_by_name['code_id']._options = None
  _MSGSTORECODERESPONSE.fields_by_name['code_id']._serialized_options = b'\342\336\037\006CodeID'
  _MSGINSTANTIATECONTRACT.fields_by_name['sender']._options = None
  _MSGINSTANTIATECONTRACT.fields_by_name['sender']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _MSGINSTANTIATECONTRACT.fields_by_name['admin']._options = None
  _MSGINSTANTIATECONTRACT.fields_by_name['admin']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _MSGINSTANTIATECONTRACT.fields_by_name['code_id']._options = None
  _MSGINSTANTIATECONTRACT.fields_by_name['code_id']._serialized_options = b'\342\336\037\006CodeID'
  _MSGINSTANTIATECONTRACT.fields_by_name['msg']._options = None
  _MSGINSTANTIATECONTRACT.fields_by_name['msg']._serialized_options = b'\372\336\037\022RawContractMessage'
  _MSGINSTANTIATECONTRACT.fields_by_name['funds']._options = None
  _MSGINSTANTIATECONTRACT.fields_by_name['funds']._serialized_options = b'\310\336\037\000\252\337\037(github.com/cosmos/cosmos-sdk/types.Coins\250\347\260*\001'
  _MSGINSTANTIATECONTRACT._options = None
  _MSGINSTANTIATECONTRACT._serialized_options = b'\202\347\260*\006sender\212\347\260*\033wasm/MsgInstantiateContract'
  _MSGINSTANTIATECONTRACTRESPONSE.fields_by_name['address']._options = None
  _MSGINSTANTIATECONTRACTRESPONSE.fields_by_name['address']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _MSGINSTANTIATECONTRACT2.fields_by_name['sender']._options = None
  _MSGINSTANTIATECONTRACT2.fields_by_name['sender']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _MSGINSTANTIATECONTRACT2.fields_by_name['admin']._options = None
  _MSGINSTANTIATECONTRACT2.fields_by_name['admin']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _MSGINSTANTIATECONTRACT2.fields_by_name['code_id']._options = None
  _MSGINSTANTIATECONTRACT2.fields_by_name['code_id']._serialized_options = b'\342\336\037\006CodeID'
  _MSGINSTANTIATECONTRACT2.fields_by_name['msg']._options = None
  _MSGINSTANTIATECONTRACT2.fields_by_name['msg']._serialized_options = b'\372\336\037\022RawContractMessage'
  _MSGINSTANTIATECONTRACT2.fields_by_name['funds']._options = None
  _MSGINSTANTIATECONTRACT2.fields_by_name['funds']._serialized_options = b'\310\336\037\000\252\337\037(github.com/cosmos/cosmos-sdk/types.Coins\250\347\260*\001'
  _MSGINSTANTIATECONTRACT2._options = None
  _MSGINSTANTIATECONTRACT2._serialized_options = b'\202\347\260*\006sender\212\347\260*\034wasm/MsgInstantiateContract2'
  _MSGINSTANTIATECONTRACT2RESPONSE.fields_by_name['address']._options = None
  _MSGINSTANTIATECONTRACT2RESPONSE.fields_by_name['address']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _MSGEXECUTECONTRACT.fields_by_name['sender']._options = None
  _MSGEXECUTECONTRACT.fields_by_name['sender']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _MSGEXECUTECONTRACT.fields_by_name['contract']._options = None
  _MSGEXECUTECONTRACT.fields_by_name['contract']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _MSGEXECUTECONTRACT.fields_by_name['msg']._options = None
  _MSGEXECUTECONTRACT.fields_by_name['msg']._serialized_options = b'\372\336\037\022RawContractMessage'
  _MSGEXECUTECONTRACT.fields_by_name['funds']._options = None
  _MSGEXECUTECONTRACT.fields_by_name['funds']._serialized_options = b'\310\336\037\000\252\337\037(github.com/cosmos/cosmos-sdk/types.Coins\250\347\260*\001'
  _MSGEXECUTECONTRACT._options = None
  _MSGEXECUTECONTRACT._serialized_options = b'\202\347\260*\006sender\212\347\260*\027wasm/MsgExecuteContract'
  _MSGMIGRATECONTRACT.fields_by_name['sender']._options = None
  _MSGMIGRATECONTRACT.fields_by_name['sender']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _MSGMIGRATECONTRACT.fields_by_name['contract']._options = None
  _MSGMIGRATECONTRACT.fields_by_name['contract']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _MSGMIGRATECONTRACT.fields_by_name['code_id']._options = None
  _MSGMIGRATECONTRACT.fields_by_name['code_id']._serialized_options = b'\342\336\037\006CodeID'
  _MSGMIGRATECONTRACT.fields_by_name['msg']._options = None
  _MSGMIGRATECONTRACT.fields_by_name['msg']._serialized_options = b'\372\336\037\022RawContractMessage'
  _MSGMIGRATECONTRACT._options = None
  _MSGMIGRATECONTRACT._serialized_options = b'\202\347\260*\006sender\212\347\260*\027wasm/MsgMigrateContract'
  _MSGUPDATEADMIN.fields_by_name['sender']._options = None
  _MSGUPDATEADMIN.fields_by_name['sender']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _MSGUPDATEADMIN.fields_by_name['new_admin']._options = None
  _MSGUPDATEADMIN.fields_by_name['new_admin']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _MSGUPDATEADMIN.fields_by_name['contract']._options = None
  _MSGUPDATEADMIN.fields_by_name['contract']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _MSGUPDATEADMIN._options = None
  _MSGUPDATEADMIN._serialized_options = b'\202\347\260*\006sender\212\347\260*\023wasm/MsgUpdateAdmin'
  _MSGCLEARADMIN.fields_by_name['sender']._options = None
  _MSGCLEARADMIN.fields_by_name['sender']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _MSGCLEARADMIN.fields_by_name['contract']._options = None
  _MSGCLEARADMIN.fields_by_name['contract']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _MSGCLEARADMIN._options = None
  _MSGCLEARADMIN._serialized_options = b'\202\347\260*\006sender\212\347\260*\022wasm/MsgClearAdmin'
  _ACCESSCONFIGUPDATE.fields_by_name['code_id']._options = None
  _ACCESSCONFIGUPDATE.fields_by_name['code_id']._serialized_options = b'\342\336\037\006CodeID'
  _ACCESSCONFIGUPDATE.fields_by_name['instantiate_permission']._options = None
  _ACCESSCONFIGUPDATE.fields_by_name['instantiate_permission']._serialized_options = b'\310\336\037\000\250\347\260*\001'
  _MSGUPDATEINSTANTIATECONFIG.fields_by_name['sender']._options = None
  _MSGUPDATEINSTANTIATECONFIG.fields_by_name['sender']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _MSGUPDATEINSTANTIATECONFIG.fields_by_name['code_id']._options = None
  _MSGUPDATEINSTANTIATECONFIG.fields_by_name['code_id']._serialized_options = b'\342\336\037\006CodeID'
  _MSGUPDATEINSTANTIATECONFIG._options = None
  _MSGUPDATEINSTANTIATECONFIG._serialized_options = b'\202\347\260*\006sender\212\347\260*\037wasm/MsgUpdateInstantiateConfig'
  _MSGUPDATEPARAMS.fields_by_name['authority']._options = None
  _MSGUPDATEPARAMS.fields_by_name['authority']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _MSGUPDATEPARAMS.fields_by_name['params']._options = None
  _MSGUPDATEPARAMS.fields_by_name['params']._serialized_options = b'\310\336\037\000\250\347\260*\001'
  _MSGUPDATEPARAMS._options = None
  _MSGUPDATEPARAMS._serialized_options = b'\202\347\260*\tauthority\212\347\260*\024wasm/MsgUpdateParams'
  _MSGSUDOCONTRACT.fields_by_name['authority']._options = None
  _MSGSUDOCONTRACT.fields_by_name['authority']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _MSGSUDOCONTRACT.fields_by_name['contract']._options = None
  _MSGSUDOCONTRACT.fields_by_name['contract']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _MSGSUDOCONTRACT.fields_by_name['msg']._options = None
  _MSGSUDOCONTRACT.fields_by_name['msg']._serialized_options = b'\372\336\037\022RawContractMessage'
  _MSGSUDOCONTRACT._options = None
  _MSGSUDOCONTRACT._serialized_options = b'\202\347\260*\tauthority\212\347\260*\024wasm/MsgSudoContract'
  _MSGPINCODES.fields_by_name['authority']._options = None
  _MSGPINCODES.fields_by_name['authority']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _MSGPINCODES.fields_by_name['code_ids']._options = None
  _MSGPINCODES.fields_by_name['code_ids']._serialized_options = b'\342\336\037\007CodeIDs\362\336\037\017yaml:\"code_ids\"'
  _MSGPINCODES._options = None
  _MSGPINCODES._serialized_options = b'\202\347\260*\tauthority\212\347\260*\020wasm/MsgPinCodes'
  _MSGUNPINCODES.fields_by_name['authority']._options = None
  _MSGUNPINCODES.fields_by_name['authority']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _MSGUNPINCODES.fields_by_name['code_ids']._options = None
  _MSGUNPINCODES.fields_by_name['code_ids']._serialized_options = b'\342\336\037\007CodeIDs\362\336\037\017yaml:\"code_ids\"'
  _MSGUNPINCODES._options = None
  _MSGUNPINCODES._serialized_options = b'\202\347\260*\tauthority\212\347\260*\022wasm/MsgUnpinCodes'
  _MSGSTOREANDINSTANTIATECONTRACT.fields_by_name['authority']._options = None
  _MSGSTOREANDINSTANTIATECONTRACT.fields_by_name['authority']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _MSGSTOREANDINSTANTIATECONTRACT.fields_by_name['wasm_byte_code']._options = None
  _MSGSTOREANDINSTANTIATECONTRACT.fields_by_name['wasm_byte_code']._serialized_options = b'\342\336\037\014WASMByteCode'
  _MSGSTOREANDINSTANTIATECONTRACT.fields_by_name['admin']._options = None
  _MSGSTOREANDINSTANTIATECONTRACT.fields_by_name['admin']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _MSGSTOREANDINSTANTIATECONTRACT.fields_by_name['msg']._options = None
  _MSGSTOREANDINSTANTIATECONTRACT.fields_by_name['msg']._serialized_options = b'\372\336\037\022RawContractMessage'
  _MSGSTOREANDINSTANTIATECONTRACT.fields_by_name['funds']._options = None
  _MSGSTOREANDINSTANTIATECONTRACT.fields_by_name['funds']._serialized_options = b'\310\336\037\000\252\337\037(github.com/cosmos/cosmos-sdk/types.Coins\250\347\260*\001'
  _MSGSTOREANDINSTANTIATECONTRACT._options = None
  _MSGSTOREANDINSTANTIATECONTRACT._serialized_options = b'\202\347\260*\tauthority\212\347\260*#wasm/MsgStoreAndInstantiateContract'
  _MSGSTOREANDINSTANTIATECONTRACTRESPONSE.fields_by_name['address']._options = None
  _MSGSTOREANDINSTANTIATECONTRACTRESPONSE.fields_by_name['address']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _MSGADDCODEUPLOADPARAMSADDRESSES.fields_by_name['authority']._options = None
  _MSGADDCODEUPLOADPARAMSADDRESSES.fields_by_name['authority']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _MSGADDCODEUPLOADPARAMSADDRESSES.fields_by_name['addresses']._options = None
  _MSGADDCODEUPLOADPARAMSADDRESSES.fields_by_name['addresses']._serialized_options = b'\362\336\037\020yaml:\"addresses\"'
  _MSGADDCODEUPLOADPARAMSADDRESSES._options = None
  _MSGADDCODEUPLOADPARAMSADDRESSES._serialized_options = b'\202\347\260*\tauthority\212\347\260*$wasm/MsgAddCodeUploadParamsAddresses'
  _MSGREMOVECODEUPLOADPARAMSADDRESSES.fields_by_name['authority']._options = None
  _MSGREMOVECODEUPLOADPARAMSADDRESSES.fields_by_name['authority']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _MSGREMOVECODEUPLOADPARAMSADDRESSES.fields_by_name['addresses']._options = None
  _MSGREMOVECODEUPLOADPARAMSADDRESSES.fields_by_name['addresses']._serialized_options = b'\362\336\037\020yaml:\"addresses\"'
  _MSGREMOVECODEUPLOADPARAMSADDRESSES._options = None
  _MSGREMOVECODEUPLOADPARAMSADDRESSES._serialized_options = b'\202\347\260*\tauthority\212\347\260*\'wasm/MsgRemoveCodeUploadParamsAddresses'
  _MSGSTOREANDMIGRATECONTRACT.fields_by_name['authority']._options = None
  _MSGSTOREANDMIGRATECONTRACT.fields_by_name['authority']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _MSGSTOREANDMIGRATECONTRACT.fields_by_name['wasm_byte_code']._options = None
  _MSGSTOREANDMIGRATECONTRACT.fields_by_name['wasm_byte_code']._serialized_options = b'\342\336\037\014WASMByteCode'
  _MSGSTOREANDMIGRATECONTRACT.fields_by_name['msg']._options = None
  _MSGSTOREANDMIGRATECONTRACT.fields_by_name['msg']._serialized_options = b'\372\336\037\022RawContractMessage'
  _MSGSTOREANDMIGRATECONTRACT._options = None
  _MSGSTOREANDMIGRATECONTRACT._serialized_options = b'\202\347\260*\tauthority\212\347\260*\037wasm/MsgStoreAndMigrateContract'
  _MSGSTOREANDMIGRATECONTRACTRESPONSE.fields_by_name['code_id']._options = None
  _MSGSTOREANDMIGRATECONTRACTRESPONSE.fields_by_name['code_id']._serialized_options = b'\342\336\037\006CodeID'
  _MSGUPDATECONTRACTLABEL.fields_by_name['sender']._options = None
  _MSGUPDATECONTRACTLABEL.fields_by_name['sender']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _MSGUPDATECONTRACTLABEL.fields_by_name['contract']._options = None
  _MSGUPDATECONTRACTLABEL.fields_by_name['contract']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _MSGUPDATECONTRACTLABEL._options = None
  _MSGUPDATECONTRACTLABEL._serialized_options = b'\202\347\260*\006sender\212\347\260*\033wasm/MsgUpdateContractLabel'
  _MSG._options = None
  _MSG._serialized_options = b'\200\347\260*\001'
  _globals['_MSGSTORECODE']._serialized_start=203
  _globals['_MSGSTORECODE']._serialized_end=412
  _globals['_MSGSTORECODERESPONSE']._serialized_start=414
  _globals['_MSGSTORECODERESPONSE']._serialized_end=483
  _globals['_MSGINSTANTIATECONTRACT']._serialized_start=486
  _globals['_MSGINSTANTIATECONTRACT']._serialized_end=816
  _globals['_MSGINSTANTIATECONTRACTRESPONSE']._serialized_start=818
  _globals['_MSGINSTANTIATECONTRACTRESPONSE']._serialized_end=907
  _globals['_MSGINSTANTIATECONTRACT2']._serialized_start=910
  _globals['_MSGINSTANTIATECONTRACT2']._serialized_end=1273
  _globals['_MSGINSTANTIATECONTRACT2RESPONSE']._serialized_start=1275
  _globals['_MSGINSTANTIATECONTRACT2RESPONSE']._serialized_end=1365
  _globals['_MSGEXECUTECONTRACT']._serialized_start=1368
  _globals['_MSGEXECUTECONTRACT']._serialized_end=1649
  _globals['_MSGEXECUTECONTRACTRESPONSE']._serialized_start=1651
  _globals['_MSGEXECUTECONTRACTRESPONSE']._serialized_end=1693
  _globals['_MSGMIGRATECONTRACT']._serialized_start=1696
  _globals['_MSGMIGRATECONTRACT']._serialized_end=1909
  _globals['_MSGMIGRATECONTRACTRESPONSE']._serialized_start=1911
  _globals['_MSGMIGRATECONTRACTRESPONSE']._serialized_end=1953
  _globals['_MSGUPDATEADMIN']._serialized_start=1956
  _globals['_MSGUPDATEADMIN']._serialized_end=2140
  _globals['_MSGUPDATEADMINRESPONSE']._serialized_start=2142
  _globals['_MSGUPDATEADMINRESPONSE']._serialized_end=2166
  _globals['_MSGCLEARADMIN']._serialized_start=2169
  _globals['_MSGCLEARADMIN']._serialized_end=2306
  _globals['_MSGCLEARADMINRESPONSE']._serialized_start=2308
  _globals['_MSGCLEARADMINRESPONSE']._serialized_end=2331
  _globals['_ACCESSCONFIGUPDATE']._serialized_start=2333
  _globals['_ACCESSCONFIGUPDATE']._serialized_end=2457
  _globals['_MSGUPDATEINSTANTIATECONFIG']._serialized_start=2460
  _globals['_MSGUPDATEINSTANTIATECONFIG']._serialized_end=2676
  _globals['_MSGUPDATEINSTANTIATECONFIGRESPONSE']._serialized_start=2678
  _globals['_MSGUPDATEINSTANTIATECONFIGRESPONSE']._serialized_end=2714
  _globals['_MSGUPDATEPARAMS']._serialized_start=2717
  _globals['_MSGUPDATEPARAMS']._serialized_end=2873
  _globals['_MSGUPDATEPARAMSRESPONSE']._serialized_start=2875
  _globals['_MSGUPDATEPARAMSRESPONSE']._serialized_end=2900
  _globals['_MSGSUDOCONTRACT']._serialized_start=2903
  _globals['_MSGSUDOCONTRACT']._serialized_end=3087
  _globals['_MSGSUDOCONTRACTRESPONSE']._serialized_start=3089
  _globals['_MSGSUDOCONTRACTRESPONSE']._serialized_end=3128
  _globals['_MSGPINCODES']._serialized_start=3131
  _globals['_MSGPINCODES']._serialized_end=3276
  _globals['_MSGPINCODESRESPONSE']._serialized_start=3278
  _globals['_MSGPINCODESRESPONSE']._serialized_end=3299
  _globals['_MSGUNPINCODES']._serialized_start=3302
  _globals['_MSGUNPINCODES']._serialized_end=3451
  _globals['_MSGUNPINCODESRESPONSE']._serialized_start=3453
  _globals['_MSGUNPINCODESRESPONSE']._serialized_end=3476
  _globals['_MSGSTOREANDINSTANTIATECONTRACT']._serialized_start=3479
  _globals['_MSGSTOREANDINSTANTIATECONTRACT']._serialized_end=3980
  _globals['_MSGSTOREANDINSTANTIATECONTRACTRESPONSE']._serialized_start=3982
  _globals['_MSGSTOREANDINSTANTIATECONTRACTRESPONSE']._serialized_end=4079
  _globals['_MSGADDCODEUPLOADPARAMSADDRESSES']._serialized_start=4082
  _globals['_MSGADDCODEUPLOADPARAMSADDRESSES']._serialized_end=4258
  _globals['_MSGADDCODEUPLOADPARAMSADDRESSESRESPONSE']._serialized_start=4260
  _globals['_MSGADDCODEUPLOADPARAMSADDRESSESRESPONSE']._serialized_end=4301
  _globals['_MSGREMOVECODEUPLOADPARAMSADDRESSES']._serialized_start=4304
  _globals['_MSGREMOVECODEUPLOADPARAMSADDRESSES']._serialized_end=4486
  _globals['_MSGREMOVECODEUPLOADPARAMSADDRESSESRESPONSE']._serialized_start=4488
  _globals['_MSGREMOVECODEUPLOADPARAMSADDRESSESRESPONSE']._serialized_end=4532
  _globals['_MSGSTOREANDMIGRATECONTRACT']._serialized_start=4535
  _globals['_MSGSTOREANDMIGRATECONTRACT']._serialized_end=4821
  _globals['_MSGSTOREANDMIGRATECONTRACTRESPONSE']._serialized_start=4823
  _globals['_MSGSTOREANDMIGRATECONTRACTRESPONSE']._serialized_end=4920
  _globals['_MSGUPDATECONTRACTLABEL']._serialized_start=4923
  _globals['_MSGUPDATECONTRACTLABEL']._serialized_end=5097
  _globals['_MSGUPDATECONTRACTLABELRESPONSE']._serialized_start=5099
  _globals['_MSGUPDATECONTRACTLABELRESPONSE']._serialized_end=5131
  _globals['_MSG']._serialized_start=5134
  _globals['_MSG']._serialized_end=7011
# @@protoc_insertion_point(module_scope)
