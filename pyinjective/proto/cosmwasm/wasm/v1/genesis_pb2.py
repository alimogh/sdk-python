# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cosmwasm/wasm/v1/genesis.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from cosmwasm.wasm.v1 import types_pb2 as cosmwasm_dot_wasm_dot_v1_dot_types__pb2
from amino import amino_pb2 as amino_dot_amino__pb2
from cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1e\x63osmwasm/wasm/v1/genesis.proto\x12\x10\x63osmwasm.wasm.v1\x1a\x14gogoproto/gogo.proto\x1a\x1c\x63osmwasm/wasm/v1/types.proto\x1a\x11\x61mino/amino.proto\x1a\x19\x63osmos_proto/cosmos.proto\"\xaa\x02\n\x0cGenesisState\x12\x33\n\x06params\x18\x01 \x01(\x0b\x32\x18.cosmwasm.wasm.v1.ParamsB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01\x12\x43\n\x05\x63odes\x18\x02 \x03(\x0b\x32\x16.cosmwasm.wasm.v1.CodeB\x1c\xc8\xde\x1f\x00\xea\xde\x1f\x0f\x63odes,omitempty\xa8\xe7\xb0*\x01\x12O\n\tcontracts\x18\x03 \x03(\x0b\x32\x1a.cosmwasm.wasm.v1.ContractB \xc8\xde\x1f\x00\xea\xde\x1f\x13\x63ontracts,omitempty\xa8\xe7\xb0*\x01\x12O\n\tsequences\x18\x04 \x03(\x0b\x32\x1a.cosmwasm.wasm.v1.SequenceB \xc8\xde\x1f\x00\xea\xde\x1f\x13sequences,omitempty\xa8\xe7\xb0*\x01\"\x81\x01\n\x04\x43ode\x12\x1b\n\x07\x63ode_id\x18\x01 \x01(\x04\x42\n\xe2\xde\x1f\x06\x43odeID\x12\x38\n\tcode_info\x18\x02 \x01(\x0b\x32\x1a.cosmwasm.wasm.v1.CodeInfoB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01\x12\x12\n\ncode_bytes\x18\x03 \x01(\x0c\x12\x0e\n\x06pinned\x18\x04 \x01(\x08\"\x92\x02\n\x08\x43ontract\x12\x32\n\x10\x63ontract_address\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12@\n\rcontract_info\x18\x02 \x01(\x0b\x32\x1e.cosmwasm.wasm.v1.ContractInfoB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01\x12:\n\x0e\x63ontract_state\x18\x03 \x03(\x0b\x32\x17.cosmwasm.wasm.v1.ModelB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01\x12T\n\x15\x63ontract_code_history\x18\x04 \x03(\x0b\x32*.cosmwasm.wasm.v1.ContractCodeHistoryEntryB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01\"4\n\x08Sequence\x12\x19\n\x06id_key\x18\x01 \x01(\x0c\x42\t\xe2\xde\x1f\x05IDKey\x12\r\n\x05value\x18\x02 \x01(\x04\x42(Z&github.com/CosmWasm/wasmd/x/wasm/typesb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmwasm.wasm.v1.genesis_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z&github.com/CosmWasm/wasmd/x/wasm/types'
  _GENESISSTATE.fields_by_name['params']._options = None
  _GENESISSTATE.fields_by_name['params']._serialized_options = b'\310\336\037\000\250\347\260*\001'
  _GENESISSTATE.fields_by_name['codes']._options = None
  _GENESISSTATE.fields_by_name['codes']._serialized_options = b'\310\336\037\000\352\336\037\017codes,omitempty\250\347\260*\001'
  _GENESISSTATE.fields_by_name['contracts']._options = None
  _GENESISSTATE.fields_by_name['contracts']._serialized_options = b'\310\336\037\000\352\336\037\023contracts,omitempty\250\347\260*\001'
  _GENESISSTATE.fields_by_name['sequences']._options = None
  _GENESISSTATE.fields_by_name['sequences']._serialized_options = b'\310\336\037\000\352\336\037\023sequences,omitempty\250\347\260*\001'
  _CODE.fields_by_name['code_id']._options = None
  _CODE.fields_by_name['code_id']._serialized_options = b'\342\336\037\006CodeID'
  _CODE.fields_by_name['code_info']._options = None
  _CODE.fields_by_name['code_info']._serialized_options = b'\310\336\037\000\250\347\260*\001'
  _CONTRACT.fields_by_name['contract_address']._options = None
  _CONTRACT.fields_by_name['contract_address']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _CONTRACT.fields_by_name['contract_info']._options = None
  _CONTRACT.fields_by_name['contract_info']._serialized_options = b'\310\336\037\000\250\347\260*\001'
  _CONTRACT.fields_by_name['contract_state']._options = None
  _CONTRACT.fields_by_name['contract_state']._serialized_options = b'\310\336\037\000\250\347\260*\001'
  _CONTRACT.fields_by_name['contract_code_history']._options = None
  _CONTRACT.fields_by_name['contract_code_history']._serialized_options = b'\310\336\037\000\250\347\260*\001'
  _SEQUENCE.fields_by_name['id_key']._options = None
  _SEQUENCE.fields_by_name['id_key']._serialized_options = b'\342\336\037\005IDKey'
  _globals['_GENESISSTATE']._serialized_start=151
  _globals['_GENESISSTATE']._serialized_end=449
  _globals['_CODE']._serialized_start=452
  _globals['_CODE']._serialized_end=581
  _globals['_CONTRACT']._serialized_start=584
  _globals['_CONTRACT']._serialized_end=858
  _globals['_SEQUENCE']._serialized_start=860
  _globals['_SEQUENCE']._serialized_end=912
# @@protoc_insertion_point(module_scope)
