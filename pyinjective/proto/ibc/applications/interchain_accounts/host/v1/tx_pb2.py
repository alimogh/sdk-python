# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ibc/applications/interchain_accounts/host/v1/tx.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from cosmos.msg.v1 import msg_pb2 as cosmos_dot_msg_dot_v1_dot_msg__pb2
from ibc.applications.interchain_accounts.host.v1 import host_pb2 as ibc_dot_applications_dot_interchain__accounts_dot_host_dot_v1_dot_host__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n5ibc/applications/interchain_accounts/host/v1/tx.proto\x12,ibc.applications.interchain_accounts.host.v1\x1a\x14gogoproto/gogo.proto\x1a\x17\x63osmos/msg/v1/msg.proto\x1a\x37ibc/applications/interchain_accounts/host/v1/host.proto\"\x80\x01\n\x0fMsgUpdateParams\x12\x11\n\tauthority\x18\x01 \x01(\t\x12J\n\x06params\x18\x02 \x01(\x0b\x32\x34.ibc.applications.interchain_accounts.host.v1.ParamsB\x04\xc8\xde\x1f\x00:\x0e\x82\xe7\xb0*\tauthority\"\x19\n\x17MsgUpdateParamsResponse2\xa3\x01\n\x03Msg\x12\x94\x01\n\x0cUpdateParams\x12=.ibc.applications.interchain_accounts.host.v1.MsgUpdateParams\x1a\x45.ibc.applications.interchain_accounts.host.v1.MsgUpdateParamsResponse\x1a\x05\x80\xe7\xb0*\x01\x42LZJgithub.com/cosmos/ibc-go/v7/modules/apps/27-interchain-accounts/host/typesb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'ibc.applications.interchain_accounts.host.v1.tx_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'ZJgithub.com/cosmos/ibc-go/v7/modules/apps/27-interchain-accounts/host/types'
  _MSGUPDATEPARAMS.fields_by_name['params']._options = None
  _MSGUPDATEPARAMS.fields_by_name['params']._serialized_options = b'\310\336\037\000'
  _MSGUPDATEPARAMS._options = None
  _MSGUPDATEPARAMS._serialized_options = b'\202\347\260*\tauthority'
  _MSG._options = None
  _MSG._serialized_options = b'\200\347\260*\001'
  _MSGUPDATEPARAMS._serialized_start=208
  _MSGUPDATEPARAMS._serialized_end=336
  _MSGUPDATEPARAMSRESPONSE._serialized_start=338
  _MSGUPDATEPARAMSRESPONSE._serialized_end=363
  _MSG._serialized_start=366
  _MSG._serialized_end=529
# @@protoc_insertion_point(module_scope)