# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: exchange/injective_meta_rpc.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!exchange/injective_meta_rpc.proto\x12\x12injective_meta_rpc\"\r\n\x0bPingRequest\"\x0e\n\x0cPingResponse\"\x10\n\x0eVersionRequest\"\x8f\x01\n\x0fVersionResponse\x12\x0f\n\x07version\x18\x01 \x01(\t\x12=\n\x05\x62uild\x18\x02 \x03(\x0b\x32..injective_meta_rpc.VersionResponse.BuildEntry\x1a,\n\nBuildEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\" \n\x0bInfoRequest\x12\x11\n\ttimestamp\x18\x01 \x01(\x12\"\xc1\x01\n\x0cInfoResponse\x12\x11\n\ttimestamp\x18\x01 \x01(\x12\x12\x13\n\x0bserver_time\x18\x02 \x01(\x12\x12\x0f\n\x07version\x18\x03 \x01(\t\x12:\n\x05\x62uild\x18\x04 \x03(\x0b\x32+.injective_meta_rpc.InfoResponse.BuildEntry\x12\x0e\n\x06region\x18\x05 \x01(\t\x1a,\n\nBuildEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\x18\n\x16StreamKeepaliveRequest\"Q\n\x17StreamKeepaliveResponse\x12\r\n\x05\x65vent\x18\x01 \x01(\t\x12\x14\n\x0cnew_endpoint\x18\x02 \x01(\t\x12\x11\n\ttimestamp\x18\x03 \x01(\x12\x32\xea\x02\n\x10InjectiveMetaRPC\x12I\n\x04Ping\x12\x1f.injective_meta_rpc.PingRequest\x1a .injective_meta_rpc.PingResponse\x12R\n\x07Version\x12\".injective_meta_rpc.VersionRequest\x1a#.injective_meta_rpc.VersionResponse\x12I\n\x04Info\x12\x1f.injective_meta_rpc.InfoRequest\x1a .injective_meta_rpc.InfoResponse\x12l\n\x0fStreamKeepalive\x12*.injective_meta_rpc.StreamKeepaliveRequest\x1a+.injective_meta_rpc.StreamKeepaliveResponse0\x01\x42\x17Z\x15/injective_meta_rpcpbb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'exchange.injective_meta_rpc_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z\025/injective_meta_rpcpb'
  _VERSIONRESPONSE_BUILDENTRY._options = None
  _VERSIONRESPONSE_BUILDENTRY._serialized_options = b'8\001'
  _INFORESPONSE_BUILDENTRY._options = None
  _INFORESPONSE_BUILDENTRY._serialized_options = b'8\001'
  _globals['_PINGREQUEST']._serialized_start=57
  _globals['_PINGREQUEST']._serialized_end=70
  _globals['_PINGRESPONSE']._serialized_start=72
  _globals['_PINGRESPONSE']._serialized_end=86
  _globals['_VERSIONREQUEST']._serialized_start=88
  _globals['_VERSIONREQUEST']._serialized_end=104
  _globals['_VERSIONRESPONSE']._serialized_start=107
  _globals['_VERSIONRESPONSE']._serialized_end=250
  _globals['_VERSIONRESPONSE_BUILDENTRY']._serialized_start=206
  _globals['_VERSIONRESPONSE_BUILDENTRY']._serialized_end=250
  _globals['_INFOREQUEST']._serialized_start=252
  _globals['_INFOREQUEST']._serialized_end=284
  _globals['_INFORESPONSE']._serialized_start=287
  _globals['_INFORESPONSE']._serialized_end=480
  _globals['_INFORESPONSE_BUILDENTRY']._serialized_start=206
  _globals['_INFORESPONSE_BUILDENTRY']._serialized_end=250
  _globals['_STREAMKEEPALIVEREQUEST']._serialized_start=482
  _globals['_STREAMKEEPALIVEREQUEST']._serialized_end=506
  _globals['_STREAMKEEPALIVERESPONSE']._serialized_start=508
  _globals['_STREAMKEEPALIVERESPONSE']._serialized_end=589
  _globals['_INJECTIVEMETARPC']._serialized_start=592
  _globals['_INJECTIVEMETARPC']._serialized_end=954
# @@protoc_insertion_point(module_scope)
