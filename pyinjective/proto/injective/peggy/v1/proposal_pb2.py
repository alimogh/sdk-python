# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: injective/peggy/v1/proposal.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!injective/peggy/v1/proposal.proto\x12\x12injective.peggy.v1\x1a\x19\x63osmos_proto/cosmos.proto\x1a\x14gogoproto/gogo.proto\"\x8d\x01\n\"BlacklistEthereumAddressesProposal\x12\r\n\x05title\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x1b\n\x13\x62lacklist_addresses\x18\x03 \x03(\t:&\x88\xa0\x1f\x00\xe8\xa0\x1f\x00\xca\xb4-\x1a\x63osmos.gov.v1beta1.Content\"\x8a\x01\n\x1fRevokeEthereumBlacklistProposal\x12\r\n\x05title\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x1b\n\x13\x62lacklist_addresses\x18\x03 \x03(\t:&\x88\xa0\x1f\x00\xe8\xa0\x1f\x00\xca\xb4-\x1a\x63osmos.gov.v1beta1.ContentBMZKgithub.com/InjectiveLabs/injective-core/injective-chain/modules/peggy/typesb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'injective.peggy.v1.proposal_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'ZKgithub.com/InjectiveLabs/injective-core/injective-chain/modules/peggy/types'
  _BLACKLISTETHEREUMADDRESSESPROPOSAL._options = None
  _BLACKLISTETHEREUMADDRESSESPROPOSAL._serialized_options = b'\210\240\037\000\350\240\037\000\312\264-\032cosmos.gov.v1beta1.Content'
  _REVOKEETHEREUMBLACKLISTPROPOSAL._options = None
  _REVOKEETHEREUMBLACKLISTPROPOSAL._serialized_options = b'\210\240\037\000\350\240\037\000\312\264-\032cosmos.gov.v1beta1.Content'
  _globals['_BLACKLISTETHEREUMADDRESSESPROPOSAL']._serialized_start=107
  _globals['_BLACKLISTETHEREUMADDRESSESPROPOSAL']._serialized_end=248
  _globals['_REVOKEETHEREUMBLACKLISTPROPOSAL']._serialized_start=251
  _globals['_REVOKEETHEREUMBLACKLISTPROPOSAL']._serialized_end=389
# @@protoc_insertion_point(module_scope)
