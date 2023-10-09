# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: injective/insurance/v1beta1/tx.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from cosmos.msg.v1 import msg_pb2 as cosmos_dot_msg_dot_v1_dot_msg__pb2
from cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
from injective.insurance.v1beta1 import insurance_pb2 as injective_dot_insurance_dot_v1beta1_dot_insurance__pb2
from injective.oracle.v1beta1 import oracle_pb2 as injective_dot_oracle_dot_v1beta1_dot_oracle__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$injective/insurance/v1beta1/tx.proto\x12\x1binjective.insurance.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x1e\x63osmos/base/v1beta1/coin.proto\x1a\x17\x63osmos/msg/v1/msg.proto\x1a\x19\x63osmos_proto/cosmos.proto\x1a+injective/insurance/v1beta1/insurance.proto\x1a%injective/oracle/v1beta1/oracle.proto\"\x92\x02\n\x16MsgCreateInsuranceFund\x12\x0e\n\x06sender\x18\x01 \x01(\t\x12\x0e\n\x06ticker\x18\x02 \x01(\t\x12\x13\n\x0bquote_denom\x18\x03 \x01(\t\x12\x13\n\x0boracle_base\x18\x04 \x01(\t\x12\x14\n\x0coracle_quote\x18\x05 \x01(\t\x12\x39\n\x0boracle_type\x18\x06 \x01(\x0e\x32$.injective.oracle.v1beta1.OracleType\x12\x0e\n\x06\x65xpiry\x18\x07 \x01(\x03\x12\x38\n\x0finitial_deposit\x18\x08 \x01(\x0b\x32\x19.cosmos.base.v1beta1.CoinB\x04\xc8\xde\x1f\x00:\x13\x88\xa0\x1f\x00\xe8\xa0\x1f\x00\x82\xe7\xb0*\x06sender\" \n\x1eMsgCreateInsuranceFundResponse\"y\n\rMsgUnderwrite\x12\x0e\n\x06sender\x18\x01 \x01(\t\x12\x11\n\tmarket_id\x18\x02 \x01(\t\x12\x30\n\x07\x64\x65posit\x18\x03 \x01(\x0b\x32\x19.cosmos.base.v1beta1.CoinB\x04\xc8\xde\x1f\x00:\x13\x88\xa0\x1f\x00\xe8\xa0\x1f\x00\x82\xe7\xb0*\x06sender\"\x17\n\x15MsgUnderwriteResponse\"\x7f\n\x14MsgRequestRedemption\x12\x0e\n\x06sender\x18\x01 \x01(\t\x12\x11\n\tmarket_id\x18\x02 \x01(\t\x12/\n\x06\x61mount\x18\x03 \x01(\x0b\x32\x19.cosmos.base.v1beta1.CoinB\x04\xc8\xde\x1f\x00:\x13\x88\xa0\x1f\x00\xe8\xa0\x1f\x00\x82\xe7\xb0*\x06sender\"\x1e\n\x1cMsgRequestRedemptionResponse\"\x89\x01\n\x0fMsgUpdateParams\x12+\n\tauthority\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12\x39\n\x06params\x18\x02 \x01(\x0b\x32#.injective.insurance.v1beta1.ParamsB\x04\xc8\xde\x1f\x00:\x0e\x82\xe7\xb0*\tauthority\"\x19\n\x17MsgUpdateParamsResponse2\xf5\x03\n\x03Msg\x12\x87\x01\n\x13\x43reateInsuranceFund\x12\x33.injective.insurance.v1beta1.MsgCreateInsuranceFund\x1a;.injective.insurance.v1beta1.MsgCreateInsuranceFundResponse\x12l\n\nUnderwrite\x12*.injective.insurance.v1beta1.MsgUnderwrite\x1a\x32.injective.insurance.v1beta1.MsgUnderwriteResponse\x12\x81\x01\n\x11RequestRedemption\x12\x31.injective.insurance.v1beta1.MsgRequestRedemption\x1a\x39.injective.insurance.v1beta1.MsgRequestRedemptionResponse\x12r\n\x0cUpdateParams\x12,.injective.insurance.v1beta1.MsgUpdateParams\x1a\x34.injective.insurance.v1beta1.MsgUpdateParamsResponseBQZOgithub.com/InjectiveLabs/injective-core/injective-chain/modules/insurance/typesb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'injective.insurance.v1beta1.tx_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'ZOgithub.com/InjectiveLabs/injective-core/injective-chain/modules/insurance/types'
  _MSGCREATEINSURANCEFUND.fields_by_name['initial_deposit']._options = None
  _MSGCREATEINSURANCEFUND.fields_by_name['initial_deposit']._serialized_options = b'\310\336\037\000'
  _MSGCREATEINSURANCEFUND._options = None
  _MSGCREATEINSURANCEFUND._serialized_options = b'\210\240\037\000\350\240\037\000\202\347\260*\006sender'
  _MSGUNDERWRITE.fields_by_name['deposit']._options = None
  _MSGUNDERWRITE.fields_by_name['deposit']._serialized_options = b'\310\336\037\000'
  _MSGUNDERWRITE._options = None
  _MSGUNDERWRITE._serialized_options = b'\210\240\037\000\350\240\037\000\202\347\260*\006sender'
  _MSGREQUESTREDEMPTION.fields_by_name['amount']._options = None
  _MSGREQUESTREDEMPTION.fields_by_name['amount']._serialized_options = b'\310\336\037\000'
  _MSGREQUESTREDEMPTION._options = None
  _MSGREQUESTREDEMPTION._serialized_options = b'\210\240\037\000\350\240\037\000\202\347\260*\006sender'
  _MSGUPDATEPARAMS.fields_by_name['authority']._options = None
  _MSGUPDATEPARAMS.fields_by_name['authority']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _MSGUPDATEPARAMS.fields_by_name['params']._options = None
  _MSGUPDATEPARAMS.fields_by_name['params']._serialized_options = b'\310\336\037\000'
  _MSGUPDATEPARAMS._options = None
  _MSGUPDATEPARAMS._serialized_options = b'\202\347\260*\tauthority'
  _globals['_MSGCREATEINSURANCEFUND']._serialized_start=260
  _globals['_MSGCREATEINSURANCEFUND']._serialized_end=534
  _globals['_MSGCREATEINSURANCEFUNDRESPONSE']._serialized_start=536
  _globals['_MSGCREATEINSURANCEFUNDRESPONSE']._serialized_end=568
  _globals['_MSGUNDERWRITE']._serialized_start=570
  _globals['_MSGUNDERWRITE']._serialized_end=691
  _globals['_MSGUNDERWRITERESPONSE']._serialized_start=693
  _globals['_MSGUNDERWRITERESPONSE']._serialized_end=716
  _globals['_MSGREQUESTREDEMPTION']._serialized_start=718
  _globals['_MSGREQUESTREDEMPTION']._serialized_end=845
  _globals['_MSGREQUESTREDEMPTIONRESPONSE']._serialized_start=847
  _globals['_MSGREQUESTREDEMPTIONRESPONSE']._serialized_end=877
  _globals['_MSGUPDATEPARAMS']._serialized_start=880
  _globals['_MSGUPDATEPARAMS']._serialized_end=1017
  _globals['_MSGUPDATEPARAMSRESPONSE']._serialized_start=1019
  _globals['_MSGUPDATEPARAMSRESPONSE']._serialized_end=1044
  _globals['_MSG']._serialized_start=1047
  _globals['_MSG']._serialized_end=1548
# @@protoc_insertion_point(module_scope)
