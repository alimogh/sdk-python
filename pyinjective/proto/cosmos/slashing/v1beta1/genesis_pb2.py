# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cosmos/slashing/v1beta1/genesis.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from cosmos.slashing.v1beta1 import slashing_pb2 as cosmos_dot_slashing_dot_v1beta1_dot_slashing__pb2
from cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
from amino import amino_pb2 as amino_dot_amino__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%cosmos/slashing/v1beta1/genesis.proto\x12\x17\x63osmos.slashing.v1beta1\x1a\x14gogoproto/gogo.proto\x1a&cosmos/slashing/v1beta1/slashing.proto\x1a\x19\x63osmos_proto/cosmos.proto\x1a\x11\x61mino/amino.proto\"\xe4\x01\n\x0cGenesisState\x12:\n\x06params\x18\x01 \x01(\x0b\x32\x1f.cosmos.slashing.v1beta1.ParamsB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01\x12\x46\n\rsigning_infos\x18\x02 \x03(\x0b\x32$.cosmos.slashing.v1beta1.SigningInfoB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01\x12P\n\rmissed_blocks\x18\x03 \x03(\x0b\x32..cosmos.slashing.v1beta1.ValidatorMissedBlocksB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01\"\x92\x01\n\x0bSigningInfo\x12)\n\x07\x61\x64\x64ress\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12X\n\x16validator_signing_info\x18\x02 \x01(\x0b\x32-.cosmos.slashing.v1beta1.ValidatorSigningInfoB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01\"\x8a\x01\n\x15ValidatorMissedBlocks\x12)\n\x07\x61\x64\x64ress\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12\x46\n\rmissed_blocks\x18\x02 \x03(\x0b\x32$.cosmos.slashing.v1beta1.MissedBlockB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01\",\n\x0bMissedBlock\x12\r\n\x05index\x18\x01 \x01(\x03\x12\x0e\n\x06missed\x18\x02 \x01(\x08\x42/Z-github.com/cosmos/cosmos-sdk/x/slashing/typesb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmos.slashing.v1beta1.genesis_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z-github.com/cosmos/cosmos-sdk/x/slashing/types'
  _GENESISSTATE.fields_by_name['params']._options = None
  _GENESISSTATE.fields_by_name['params']._serialized_options = b'\310\336\037\000\250\347\260*\001'
  _GENESISSTATE.fields_by_name['signing_infos']._options = None
  _GENESISSTATE.fields_by_name['signing_infos']._serialized_options = b'\310\336\037\000\250\347\260*\001'
  _GENESISSTATE.fields_by_name['missed_blocks']._options = None
  _GENESISSTATE.fields_by_name['missed_blocks']._serialized_options = b'\310\336\037\000\250\347\260*\001'
  _SIGNINGINFO.fields_by_name['address']._options = None
  _SIGNINGINFO.fields_by_name['address']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _SIGNINGINFO.fields_by_name['validator_signing_info']._options = None
  _SIGNINGINFO.fields_by_name['validator_signing_info']._serialized_options = b'\310\336\037\000\250\347\260*\001'
  _VALIDATORMISSEDBLOCKS.fields_by_name['address']._options = None
  _VALIDATORMISSEDBLOCKS.fields_by_name['address']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _VALIDATORMISSEDBLOCKS.fields_by_name['missed_blocks']._options = None
  _VALIDATORMISSEDBLOCKS.fields_by_name['missed_blocks']._serialized_options = b'\310\336\037\000\250\347\260*\001'
  _GENESISSTATE._serialized_start=175
  _GENESISSTATE._serialized_end=403
  _SIGNINGINFO._serialized_start=406
  _SIGNINGINFO._serialized_end=552
  _VALIDATORMISSEDBLOCKS._serialized_start=555
  _VALIDATORMISSEDBLOCKS._serialized_end=693
  _MISSEDBLOCK._serialized_start=695
  _MISSEDBLOCK._serialized_end=739
# @@protoc_insertion_point(module_scope)
