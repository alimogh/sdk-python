# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: injective/tokenfactory/v1beta1/tx.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from cosmos.bank.v1beta1 import bank_pb2 as cosmos_dot_bank_dot_v1beta1_dot_bank__pb2
from cosmos.msg.v1 import msg_pb2 as cosmos_dot_msg_dot_v1_dot_msg__pb2
from cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
from injective.tokenfactory.v1beta1 import params_pb2 as injective_dot_tokenfactory_dot_v1beta1_dot_params__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'injective/tokenfactory/v1beta1/tx.proto\x12\x1einjective.tokenfactory.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x1e\x63osmos/base/v1beta1/coin.proto\x1a\x1e\x63osmos/bank/v1beta1/bank.proto\x1a\x17\x63osmos/msg/v1/msg.proto\x1a\x19\x63osmos_proto/cosmos.proto\x1a+injective/tokenfactory/v1beta1/params.proto\"g\n\x0eMsgCreateDenom\x12!\n\x06sender\x18\x01 \x01(\tB\x11\xf2\xde\x1f\ryaml:\"sender\"\x12%\n\x08subdenom\x18\x02 \x01(\tB\x13\xf2\xde\x1f\x0fyaml:\"subdenom\":\x0b\x82\xe7\xb0*\x06sender\"M\n\x16MsgCreateDenomResponse\x12\x33\n\x0fnew_token_denom\x18\x01 \x01(\tB\x1a\xf2\xde\x1f\x16yaml:\"new_token_denom\"\"{\n\x07MsgMint\x12!\n\x06sender\x18\x01 \x01(\tB\x11\xf2\xde\x1f\ryaml:\"sender\"\x12@\n\x06\x61mount\x18\x02 \x01(\x0b\x32\x19.cosmos.base.v1beta1.CoinB\x15\xc8\xde\x1f\x00\xf2\xde\x1f\ryaml:\"amount\":\x0b\x82\xe7\xb0*\x06sender\"\x11\n\x0fMsgMintResponse\"{\n\x07MsgBurn\x12!\n\x06sender\x18\x01 \x01(\tB\x11\xf2\xde\x1f\ryaml:\"sender\"\x12@\n\x06\x61mount\x18\x02 \x01(\x0b\x32\x19.cosmos.base.v1beta1.CoinB\x15\xc8\xde\x1f\x00\xf2\xde\x1f\ryaml:\"amount\":\x0b\x82\xe7\xb0*\x06sender\"\x11\n\x0fMsgBurnResponse\"\x8a\x01\n\x0eMsgChangeAdmin\x12!\n\x06sender\x18\x01 \x01(\tB\x11\xf2\xde\x1f\ryaml:\"sender\"\x12\x1f\n\x05\x64\x65nom\x18\x02 \x01(\tB\x10\xf2\xde\x1f\x0cyaml:\"denom\"\x12\'\n\tnew_admin\x18\x03 \x01(\tB\x14\xf2\xde\x1f\x10yaml:\"new_admin\":\x0b\x82\xe7\xb0*\x06sender\"\x18\n\x16MsgChangeAdminResponse\"\x8f\x01\n\x13MsgSetDenomMetadata\x12!\n\x06sender\x18\x01 \x01(\tB\x11\xf2\xde\x1f\ryaml:\"sender\"\x12H\n\x08metadata\x18\x02 \x01(\x0b\x32\x1d.cosmos.bank.v1beta1.MetadataB\x17\xc8\xde\x1f\x00\xf2\xde\x1f\x0fyaml:\"metadata\":\x0b\x82\xe7\xb0*\x06sender\"\x1d\n\x1bMsgSetDenomMetadataResponse\"\x8c\x01\n\x0fMsgUpdateParams\x12+\n\tauthority\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12<\n\x06params\x18\x02 \x01(\x0b\x32&.injective.tokenfactory.v1beta1.ParamsB\x04\xc8\xde\x1f\x00:\x0e\x82\xe7\xb0*\tauthority\"\x19\n\x17MsgUpdateParamsResponse2\xb8\x05\n\x03Msg\x12u\n\x0b\x43reateDenom\x12..injective.tokenfactory.v1beta1.MsgCreateDenom\x1a\x36.injective.tokenfactory.v1beta1.MsgCreateDenomResponse\x12`\n\x04Mint\x12\'.injective.tokenfactory.v1beta1.MsgMint\x1a/.injective.tokenfactory.v1beta1.MsgMintResponse\x12`\n\x04\x42urn\x12\'.injective.tokenfactory.v1beta1.MsgBurn\x1a/.injective.tokenfactory.v1beta1.MsgBurnResponse\x12u\n\x0b\x43hangeAdmin\x12..injective.tokenfactory.v1beta1.MsgChangeAdmin\x1a\x36.injective.tokenfactory.v1beta1.MsgChangeAdminResponse\x12\x84\x01\n\x10SetDenomMetadata\x12\x33.injective.tokenfactory.v1beta1.MsgSetDenomMetadata\x1a;.injective.tokenfactory.v1beta1.MsgSetDenomMetadataResponse\x12x\n\x0cUpdateParams\x12/.injective.tokenfactory.v1beta1.MsgUpdateParams\x1a\x37.injective.tokenfactory.v1beta1.MsgUpdateParamsResponseBTZRgithub.com/InjectiveLabs/injective-core/injective-chain/modules/tokenfactory/typesb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'injective.tokenfactory.v1beta1.tx_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'ZRgithub.com/InjectiveLabs/injective-core/injective-chain/modules/tokenfactory/types'
  _MSGCREATEDENOM.fields_by_name['sender']._options = None
  _MSGCREATEDENOM.fields_by_name['sender']._serialized_options = b'\362\336\037\ryaml:\"sender\"'
  _MSGCREATEDENOM.fields_by_name['subdenom']._options = None
  _MSGCREATEDENOM.fields_by_name['subdenom']._serialized_options = b'\362\336\037\017yaml:\"subdenom\"'
  _MSGCREATEDENOM._options = None
  _MSGCREATEDENOM._serialized_options = b'\202\347\260*\006sender'
  _MSGCREATEDENOMRESPONSE.fields_by_name['new_token_denom']._options = None
  _MSGCREATEDENOMRESPONSE.fields_by_name['new_token_denom']._serialized_options = b'\362\336\037\026yaml:\"new_token_denom\"'
  _MSGMINT.fields_by_name['sender']._options = None
  _MSGMINT.fields_by_name['sender']._serialized_options = b'\362\336\037\ryaml:\"sender\"'
  _MSGMINT.fields_by_name['amount']._options = None
  _MSGMINT.fields_by_name['amount']._serialized_options = b'\310\336\037\000\362\336\037\ryaml:\"amount\"'
  _MSGMINT._options = None
  _MSGMINT._serialized_options = b'\202\347\260*\006sender'
  _MSGBURN.fields_by_name['sender']._options = None
  _MSGBURN.fields_by_name['sender']._serialized_options = b'\362\336\037\ryaml:\"sender\"'
  _MSGBURN.fields_by_name['amount']._options = None
  _MSGBURN.fields_by_name['amount']._serialized_options = b'\310\336\037\000\362\336\037\ryaml:\"amount\"'
  _MSGBURN._options = None
  _MSGBURN._serialized_options = b'\202\347\260*\006sender'
  _MSGCHANGEADMIN.fields_by_name['sender']._options = None
  _MSGCHANGEADMIN.fields_by_name['sender']._serialized_options = b'\362\336\037\ryaml:\"sender\"'
  _MSGCHANGEADMIN.fields_by_name['denom']._options = None
  _MSGCHANGEADMIN.fields_by_name['denom']._serialized_options = b'\362\336\037\014yaml:\"denom\"'
  _MSGCHANGEADMIN.fields_by_name['new_admin']._options = None
  _MSGCHANGEADMIN.fields_by_name['new_admin']._serialized_options = b'\362\336\037\020yaml:\"new_admin\"'
  _MSGCHANGEADMIN._options = None
  _MSGCHANGEADMIN._serialized_options = b'\202\347\260*\006sender'
  _MSGSETDENOMMETADATA.fields_by_name['sender']._options = None
  _MSGSETDENOMMETADATA.fields_by_name['sender']._serialized_options = b'\362\336\037\ryaml:\"sender\"'
  _MSGSETDENOMMETADATA.fields_by_name['metadata']._options = None
  _MSGSETDENOMMETADATA.fields_by_name['metadata']._serialized_options = b'\310\336\037\000\362\336\037\017yaml:\"metadata\"'
  _MSGSETDENOMMETADATA._options = None
  _MSGSETDENOMMETADATA._serialized_options = b'\202\347\260*\006sender'
  _MSGUPDATEPARAMS.fields_by_name['authority']._options = None
  _MSGUPDATEPARAMS.fields_by_name['authority']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _MSGUPDATEPARAMS.fields_by_name['params']._options = None
  _MSGUPDATEPARAMS.fields_by_name['params']._serialized_options = b'\310\336\037\000'
  _MSGUPDATEPARAMS._options = None
  _MSGUPDATEPARAMS._serialized_options = b'\202\347\260*\tauthority'
  _globals['_MSGCREATEDENOM']._serialized_start=258
  _globals['_MSGCREATEDENOM']._serialized_end=361
  _globals['_MSGCREATEDENOMRESPONSE']._serialized_start=363
  _globals['_MSGCREATEDENOMRESPONSE']._serialized_end=440
  _globals['_MSGMINT']._serialized_start=442
  _globals['_MSGMINT']._serialized_end=565
  _globals['_MSGMINTRESPONSE']._serialized_start=567
  _globals['_MSGMINTRESPONSE']._serialized_end=584
  _globals['_MSGBURN']._serialized_start=586
  _globals['_MSGBURN']._serialized_end=709
  _globals['_MSGBURNRESPONSE']._serialized_start=711
  _globals['_MSGBURNRESPONSE']._serialized_end=728
  _globals['_MSGCHANGEADMIN']._serialized_start=731
  _globals['_MSGCHANGEADMIN']._serialized_end=869
  _globals['_MSGCHANGEADMINRESPONSE']._serialized_start=871
  _globals['_MSGCHANGEADMINRESPONSE']._serialized_end=895
  _globals['_MSGSETDENOMMETADATA']._serialized_start=898
  _globals['_MSGSETDENOMMETADATA']._serialized_end=1041
  _globals['_MSGSETDENOMMETADATARESPONSE']._serialized_start=1043
  _globals['_MSGSETDENOMMETADATARESPONSE']._serialized_end=1072
  _globals['_MSGUPDATEPARAMS']._serialized_start=1075
  _globals['_MSGUPDATEPARAMS']._serialized_end=1215
  _globals['_MSGUPDATEPARAMSRESPONSE']._serialized_start=1217
  _globals['_MSGUPDATEPARAMSRESPONSE']._serialized_end=1242
  _globals['_MSG']._serialized_start=1245
  _globals['_MSG']._serialized_end=1941
# @@protoc_insertion_point(module_scope)
