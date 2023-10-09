# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ibc/core/client/v1/tx.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from cosmos.msg.v1 import msg_pb2 as cosmos_dot_msg_dot_v1_dot_msg__pb2
from cosmos.upgrade.v1beta1 import upgrade_pb2 as cosmos_dot_upgrade_dot_v1beta1_dot_upgrade__pb2
from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from ibc.core.client.v1 import client_pb2 as ibc_dot_core_dot_client_dot_v1_dot_client__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1bibc/core/client/v1/tx.proto\x12\x12ibc.core.client.v1\x1a\x17\x63osmos/msg/v1/msg.proto\x1a$cosmos/upgrade/v1beta1/upgrade.proto\x1a\x14gogoproto/gogo.proto\x1a\x19google/protobuf/any.proto\x1a\x1fibc/core/client/v1/client.proto\"\x8d\x01\n\x0fMsgCreateClient\x12*\n\x0c\x63lient_state\x18\x01 \x01(\x0b\x32\x14.google.protobuf.Any\x12-\n\x0f\x63onsensus_state\x18\x02 \x01(\x0b\x32\x14.google.protobuf.Any\x12\x0e\n\x06signer\x18\x03 \x01(\t:\x0f\x88\xa0\x1f\x00\x82\xe7\xb0*\x06signer\"\x19\n\x17MsgCreateClientResponse\"s\n\x0fMsgUpdateClient\x12\x11\n\tclient_id\x18\x01 \x01(\t\x12,\n\x0e\x63lient_message\x18\x02 \x01(\x0b\x32\x14.google.protobuf.Any\x12\x0e\n\x06signer\x18\x03 \x01(\t:\x0f\x88\xa0\x1f\x00\x82\xe7\xb0*\x06signer\"\x19\n\x17MsgUpdateClientResponse\"\xe6\x01\n\x10MsgUpgradeClient\x12\x11\n\tclient_id\x18\x01 \x01(\t\x12*\n\x0c\x63lient_state\x18\x02 \x01(\x0b\x32\x14.google.protobuf.Any\x12-\n\x0f\x63onsensus_state\x18\x03 \x01(\x0b\x32\x14.google.protobuf.Any\x12\x1c\n\x14proof_upgrade_client\x18\x04 \x01(\x0c\x12%\n\x1dproof_upgrade_consensus_state\x18\x05 \x01(\x0c\x12\x0e\n\x06signer\x18\x06 \x01(\t:\x0f\x88\xa0\x1f\x00\x82\xe7\xb0*\x06signer\"\x1a\n\x18MsgUpgradeClientResponse\"y\n\x15MsgSubmitMisbehaviour\x12\x11\n\tclient_id\x18\x01 \x01(\t\x12*\n\x0cmisbehaviour\x18\x02 \x01(\x0b\x32\x14.google.protobuf.Any\x12\x0e\n\x06signer\x18\x03 \x01(\t:\x11\x18\x01\x88\xa0\x1f\x00\x82\xe7\xb0*\x06signer\"\x1f\n\x1dMsgSubmitMisbehaviourResponse\"l\n\x10MsgRecoverClient\x12\x19\n\x11subject_client_id\x18\x01 \x01(\t\x12\x1c\n\x14substitute_client_id\x18\x02 \x01(\t\x12\x0e\n\x06signer\x18\x03 \x01(\t:\x0f\x88\xa0\x1f\x00\x82\xe7\xb0*\x06signer\"\x1a\n\x18MsgRecoverClientResponse\"\x9b\x01\n\x15MsgIBCSoftwareUpgrade\x12\x30\n\x04plan\x18\x01 \x01(\x0b\x32\x1c.cosmos.upgrade.v1beta1.PlanB\x04\xc8\xde\x1f\x00\x12\x33\n\x15upgraded_client_state\x18\x02 \x01(\x0b\x32\x14.google.protobuf.Any\x12\x0e\n\x06signer\x18\x03 \x01(\t:\x0b\x82\xe7\xb0*\x06signer\"\x1f\n\x1dMsgIBCSoftwareUpgradeResponse\"d\n\x0fMsgUpdateParams\x12\x0e\n\x06signer\x18\x01 \x01(\t\x12\x30\n\x06params\x18\x02 \x01(\x0b\x32\x1a.ibc.core.client.v1.ParamsB\x04\xc8\xde\x1f\x00:\x0f\x88\xa0\x1f\x00\x82\xe7\xb0*\x06signer\"\x19\n\x17MsgUpdateParamsResponse2\xea\x05\n\x03Msg\x12`\n\x0c\x43reateClient\x12#.ibc.core.client.v1.MsgCreateClient\x1a+.ibc.core.client.v1.MsgCreateClientResponse\x12`\n\x0cUpdateClient\x12#.ibc.core.client.v1.MsgUpdateClient\x1a+.ibc.core.client.v1.MsgUpdateClientResponse\x12\x63\n\rUpgradeClient\x12$.ibc.core.client.v1.MsgUpgradeClient\x1a,.ibc.core.client.v1.MsgUpgradeClientResponse\x12r\n\x12SubmitMisbehaviour\x12).ibc.core.client.v1.MsgSubmitMisbehaviour\x1a\x31.ibc.core.client.v1.MsgSubmitMisbehaviourResponse\x12\x63\n\rRecoverClient\x12$.ibc.core.client.v1.MsgRecoverClient\x1a,.ibc.core.client.v1.MsgRecoverClientResponse\x12r\n\x12IBCSoftwareUpgrade\x12).ibc.core.client.v1.MsgIBCSoftwareUpgrade\x1a\x31.ibc.core.client.v1.MsgIBCSoftwareUpgradeResponse\x12\x66\n\x12UpdateClientParams\x12#.ibc.core.client.v1.MsgUpdateParams\x1a+.ibc.core.client.v1.MsgUpdateParamsResponse\x1a\x05\x80\xe7\xb0*\x01\x42:Z8github.com/cosmos/ibc-go/v8/modules/core/02-client/typesb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'ibc.core.client.v1.tx_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z8github.com/cosmos/ibc-go/v8/modules/core/02-client/types'
  _MSGCREATECLIENT._options = None
  _MSGCREATECLIENT._serialized_options = b'\210\240\037\000\202\347\260*\006signer'
  _MSGUPDATECLIENT._options = None
  _MSGUPDATECLIENT._serialized_options = b'\210\240\037\000\202\347\260*\006signer'
  _MSGUPGRADECLIENT._options = None
  _MSGUPGRADECLIENT._serialized_options = b'\210\240\037\000\202\347\260*\006signer'
  _MSGSUBMITMISBEHAVIOUR._options = None
  _MSGSUBMITMISBEHAVIOUR._serialized_options = b'\030\001\210\240\037\000\202\347\260*\006signer'
  _MSGRECOVERCLIENT._options = None
  _MSGRECOVERCLIENT._serialized_options = b'\210\240\037\000\202\347\260*\006signer'
  _MSGIBCSOFTWAREUPGRADE.fields_by_name['plan']._options = None
  _MSGIBCSOFTWAREUPGRADE.fields_by_name['plan']._serialized_options = b'\310\336\037\000'
  _MSGIBCSOFTWAREUPGRADE._options = None
  _MSGIBCSOFTWAREUPGRADE._serialized_options = b'\202\347\260*\006signer'
  _MSGUPDATEPARAMS.fields_by_name['params']._options = None
  _MSGUPDATEPARAMS.fields_by_name['params']._serialized_options = b'\310\336\037\000'
  _MSGUPDATEPARAMS._options = None
  _MSGUPDATEPARAMS._serialized_options = b'\210\240\037\000\202\347\260*\006signer'
  _MSG._options = None
  _MSG._serialized_options = b'\200\347\260*\001'
  _globals['_MSGCREATECLIENT']._serialized_start=197
  _globals['_MSGCREATECLIENT']._serialized_end=338
  _globals['_MSGCREATECLIENTRESPONSE']._serialized_start=340
  _globals['_MSGCREATECLIENTRESPONSE']._serialized_end=365
  _globals['_MSGUPDATECLIENT']._serialized_start=367
  _globals['_MSGUPDATECLIENT']._serialized_end=482
  _globals['_MSGUPDATECLIENTRESPONSE']._serialized_start=484
  _globals['_MSGUPDATECLIENTRESPONSE']._serialized_end=509
  _globals['_MSGUPGRADECLIENT']._serialized_start=512
  _globals['_MSGUPGRADECLIENT']._serialized_end=742
  _globals['_MSGUPGRADECLIENTRESPONSE']._serialized_start=744
  _globals['_MSGUPGRADECLIENTRESPONSE']._serialized_end=770
  _globals['_MSGSUBMITMISBEHAVIOUR']._serialized_start=772
  _globals['_MSGSUBMITMISBEHAVIOUR']._serialized_end=893
  _globals['_MSGSUBMITMISBEHAVIOURRESPONSE']._serialized_start=895
  _globals['_MSGSUBMITMISBEHAVIOURRESPONSE']._serialized_end=926
  _globals['_MSGRECOVERCLIENT']._serialized_start=928
  _globals['_MSGRECOVERCLIENT']._serialized_end=1036
  _globals['_MSGRECOVERCLIENTRESPONSE']._serialized_start=1038
  _globals['_MSGRECOVERCLIENTRESPONSE']._serialized_end=1064
  _globals['_MSGIBCSOFTWAREUPGRADE']._serialized_start=1067
  _globals['_MSGIBCSOFTWAREUPGRADE']._serialized_end=1222
  _globals['_MSGIBCSOFTWAREUPGRADERESPONSE']._serialized_start=1224
  _globals['_MSGIBCSOFTWAREUPGRADERESPONSE']._serialized_end=1255
  _globals['_MSGUPDATEPARAMS']._serialized_start=1257
  _globals['_MSGUPDATEPARAMS']._serialized_end=1357
  _globals['_MSGUPDATEPARAMSRESPONSE']._serialized_start=1359
  _globals['_MSGUPDATEPARAMSRESPONSE']._serialized_end=1384
  _globals['_MSG']._serialized_start=1387
  _globals['_MSG']._serialized_end=2133
# @@protoc_insertion_point(module_scope)
