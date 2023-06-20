# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ibc/applications/transfer/v1/tx.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from cosmos.msg.v1 import msg_pb2 as cosmos_dot_msg_dot_v1_dot_msg__pb2
from cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from ibc.core.client.v1 import client_pb2 as ibc_dot_core_dot_client_dot_v1_dot_client__pb2
from ibc.applications.transfer.v1 import transfer_pb2 as ibc_dot_applications_dot_transfer_dot_v1_dot_transfer__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%ibc/applications/transfer/v1/tx.proto\x12\x1cibc.applications.transfer.v1\x1a\x14gogoproto/gogo.proto\x1a\x17\x63osmos/msg/v1/msg.proto\x1a\x1e\x63osmos/base/v1beta1/coin.proto\x1a\x1fibc/core/client/v1/client.proto\x1a+ibc/applications/transfer/v1/transfer.proto\"\x84\x02\n\x0bMsgTransfer\x12\x13\n\x0bsource_port\x18\x01 \x01(\t\x12\x16\n\x0esource_channel\x18\x02 \x01(\t\x12.\n\x05token\x18\x03 \x01(\x0b\x32\x19.cosmos.base.v1beta1.CoinB\x04\xc8\xde\x1f\x00\x12\x0e\n\x06sender\x18\x04 \x01(\t\x12\x10\n\x08receiver\x18\x05 \x01(\t\x12\x38\n\x0etimeout_height\x18\x06 \x01(\x0b\x32\x1a.ibc.core.client.v1.HeightB\x04\xc8\xde\x1f\x00\x12\x19\n\x11timeout_timestamp\x18\x07 \x01(\x04\x12\x0c\n\x04memo\x18\x08 \x01(\t:\x13\x82\xe7\xb0*\x06sender\xe8\xa0\x1f\x00\x88\xa0\x1f\x00\"\'\n\x13MsgTransferResponse\x12\x10\n\x08sequence\x18\x01 \x01(\x04\"p\n\x0fMsgUpdateParams\x12\x11\n\tauthority\x18\x01 \x01(\t\x12:\n\x06params\x18\x02 \x01(\x0b\x32$.ibc.applications.transfer.v1.ParamsB\x04\xc8\xde\x1f\x00:\x0e\x82\xe7\xb0*\tauthority\"\x19\n\x17MsgUpdateParamsResponse2\xec\x01\n\x03Msg\x12h\n\x08Transfer\x12).ibc.applications.transfer.v1.MsgTransfer\x1a\x31.ibc.applications.transfer.v1.MsgTransferResponse\x12t\n\x0cUpdateParams\x12-.ibc.applications.transfer.v1.MsgUpdateParams\x1a\x35.ibc.applications.transfer.v1.MsgUpdateParamsResponse\x1a\x05\x80\xe7\xb0*\x01\x42\x39Z7github.com/cosmos/ibc-go/v7/modules/apps/transfer/typesb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'ibc.applications.transfer.v1.tx_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z7github.com/cosmos/ibc-go/v7/modules/apps/transfer/types'
  _MSGTRANSFER.fields_by_name['token']._options = None
  _MSGTRANSFER.fields_by_name['token']._serialized_options = b'\310\336\037\000'
  _MSGTRANSFER.fields_by_name['timeout_height']._options = None
  _MSGTRANSFER.fields_by_name['timeout_height']._serialized_options = b'\310\336\037\000'
  _MSGTRANSFER._options = None
  _MSGTRANSFER._serialized_options = b'\202\347\260*\006sender\350\240\037\000\210\240\037\000'
  _MSGUPDATEPARAMS.fields_by_name['params']._options = None
  _MSGUPDATEPARAMS.fields_by_name['params']._serialized_options = b'\310\336\037\000'
  _MSGUPDATEPARAMS._options = None
  _MSGUPDATEPARAMS._serialized_options = b'\202\347\260*\tauthority'
  _MSG._options = None
  _MSG._serialized_options = b'\200\347\260*\001'
  _MSGTRANSFER._serialized_start=229
  _MSGTRANSFER._serialized_end=489
  _MSGTRANSFERRESPONSE._serialized_start=491
  _MSGTRANSFERRESPONSE._serialized_end=530
  _MSGUPDATEPARAMS._serialized_start=532
  _MSGUPDATEPARAMS._serialized_end=644
  _MSGUPDATEPARAMSRESPONSE._serialized_start=646
  _MSGUPDATEPARAMSRESPONSE._serialized_end=671
  _MSG._serialized_start=674
  _MSG._serialized_end=910
# @@protoc_insertion_point(module_scope)
