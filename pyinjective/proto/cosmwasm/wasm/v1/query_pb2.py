# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cosmwasm/wasm/v1/query.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from cosmwasm.wasm.v1 import types_pb2 as cosmwasm_dot_wasm_dot_v1_dot_types__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from cosmos.base.query.v1beta1 import pagination_pb2 as cosmos_dot_base_dot_query_dot_v1beta1_dot_pagination__pb2
from amino import amino_pb2 as amino_dot_amino__pb2
from cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1c\x63osmwasm/wasm/v1/query.proto\x12\x10\x63osmwasm.wasm.v1\x1a\x14gogoproto/gogo.proto\x1a\x1c\x63osmwasm/wasm/v1/types.proto\x1a\x1cgoogle/api/annotations.proto\x1a*cosmos/base/query/v1beta1/pagination.proto\x1a\x11\x61mino/amino.proto\x1a\x19\x63osmos_proto/cosmos.proto\"E\n\x18QueryContractInfoRequest\x12)\n\x07\x61\x64\x64ress\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\"\x96\x01\n\x19QueryContractInfoResponse\x12)\n\x07\x61\x64\x64ress\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12H\n\rcontract_info\x18\x02 \x01(\x0b\x32\x1e.cosmwasm.wasm.v1.ContractInfoB\x11\xc8\xde\x1f\x00\xd0\xde\x1f\x01\xea\xde\x1f\x00\xa8\xe7\xb0*\x01:\x04\xe8\xa0\x1f\x01\"\x84\x01\n\x1bQueryContractHistoryRequest\x12)\n\x07\x61\x64\x64ress\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12:\n\npagination\x18\x02 \x01(\x0b\x32&.cosmos.base.query.v1beta1.PageRequest\"\xa3\x01\n\x1cQueryContractHistoryResponse\x12\x46\n\x07\x65ntries\x18\x01 \x03(\x0b\x32*.cosmwasm.wasm.v1.ContractCodeHistoryEntryB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01\x12;\n\npagination\x18\x02 \x01(\x0b\x32\'.cosmos.base.query.v1beta1.PageResponse\"j\n\x1bQueryContractsByCodeRequest\x12\x0f\n\x07\x63ode_id\x18\x01 \x01(\x04\x12:\n\npagination\x18\x02 \x01(\x0b\x32&.cosmos.base.query.v1beta1.PageRequest\"\x88\x01\n\x1cQueryContractsByCodeResponse\x12+\n\tcontracts\x18\x01 \x03(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12;\n\npagination\x18\x02 \x01(\x0b\x32\'.cosmos.base.query.v1beta1.PageResponse\"\x85\x01\n\x1cQueryAllContractStateRequest\x12)\n\x07\x61\x64\x64ress\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12:\n\npagination\x18\x02 \x01(\x0b\x32&.cosmos.base.query.v1beta1.PageRequest\"\x90\x01\n\x1dQueryAllContractStateResponse\x12\x32\n\x06models\x18\x01 \x03(\x0b\x32\x17.cosmwasm.wasm.v1.ModelB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01\x12;\n\npagination\x18\x02 \x01(\x0b\x32\'.cosmos.base.query.v1beta1.PageResponse\"]\n\x1cQueryRawContractStateRequest\x12)\n\x07\x61\x64\x64ress\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12\x12\n\nquery_data\x18\x02 \x01(\x0c\"-\n\x1dQueryRawContractStateResponse\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\x0c\"w\n\x1eQuerySmartContractStateRequest\x12)\n\x07\x61\x64\x64ress\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12*\n\nquery_data\x18\x02 \x01(\x0c\x42\x16\xfa\xde\x1f\x12RawContractMessage\"G\n\x1fQuerySmartContractStateResponse\x12$\n\x04\x64\x61ta\x18\x01 \x01(\x0c\x42\x16\xfa\xde\x1f\x12RawContractMessage\"#\n\x10QueryCodeRequest\x12\x0f\n\x07\x63ode_id\x18\x01 \x01(\x04\"\x86\x02\n\x10\x43odeInfoResponse\x12!\n\x07\x63ode_id\x18\x01 \x01(\x04\x42\x10\xe2\xde\x1f\x06\x43odeID\xea\xde\x1f\x02id\x12)\n\x07\x63reator\x18\x02 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12G\n\tdata_hash\x18\x03 \x01(\x0c\x42\x34\xfa\xde\x1f\x30github.com/cometbft/cometbft/libs/bytes.HexBytes\x12I\n\x16instantiate_permission\x18\x06 \x01(\x0b\x32\x1e.cosmwasm.wasm.v1.AccessConfigB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01:\x04\xe8\xa0\x1f\x01J\x04\x08\x04\x10\x05J\x04\x08\x05\x10\x06\"r\n\x11QueryCodeResponse\x12?\n\tcode_info\x18\x01 \x01(\x0b\x32\".cosmwasm.wasm.v1.CodeInfoResponseB\x08\xd0\xde\x1f\x01\xea\xde\x1f\x00\x12\x16\n\x04\x64\x61ta\x18\x02 \x01(\x0c\x42\x08\xea\xde\x1f\x04\x64\x61ta:\x04\xe8\xa0\x1f\x01\"O\n\x11QueryCodesRequest\x12:\n\npagination\x18\x01 \x01(\x0b\x32&.cosmos.base.query.v1beta1.PageRequest\"\x94\x01\n\x12QueryCodesResponse\x12\x41\n\ncode_infos\x18\x01 \x03(\x0b\x32\".cosmwasm.wasm.v1.CodeInfoResponseB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01\x12;\n\npagination\x18\x02 \x01(\x0b\x32\'.cosmos.base.query.v1beta1.PageResponse\"U\n\x17QueryPinnedCodesRequest\x12:\n\npagination\x18\x02 \x01(\x0b\x32&.cosmos.base.query.v1beta1.PageRequest\"v\n\x18QueryPinnedCodesResponse\x12\x1d\n\x08\x63ode_ids\x18\x01 \x03(\x04\x42\x0b\xe2\xde\x1f\x07\x43odeIDs\x12;\n\npagination\x18\x02 \x01(\x0b\x32\'.cosmos.base.query.v1beta1.PageResponse\"\x14\n\x12QueryParamsRequest\"J\n\x13QueryParamsResponse\x12\x33\n\x06params\x18\x01 \x01(\x0b\x32\x18.cosmwasm.wasm.v1.ParamsB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01\"\x8f\x01\n\x1eQueryContractsByCreatorRequest\x12\x31\n\x0f\x63reator_address\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12:\n\npagination\x18\x02 \x01(\x0b\x32&.cosmos.base.query.v1beta1.PageRequest\"\x94\x01\n\x1fQueryContractsByCreatorResponse\x12\x34\n\x12\x63ontract_addresses\x18\x01 \x03(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12;\n\npagination\x18\x02 \x01(\x0b\x32\'.cosmos.base.query.v1beta1.PageResponse2\xc3\r\n\x05Query\x12\x95\x01\n\x0c\x43ontractInfo\x12*.cosmwasm.wasm.v1.QueryContractInfoRequest\x1a+.cosmwasm.wasm.v1.QueryContractInfoResponse\",\x82\xd3\xe4\x93\x02&\x12$/cosmwasm/wasm/v1/contract/{address}\x12\xa6\x01\n\x0f\x43ontractHistory\x12-.cosmwasm.wasm.v1.QueryContractHistoryRequest\x1a..cosmwasm.wasm.v1.QueryContractHistoryResponse\"4\x82\xd3\xe4\x93\x02.\x12,/cosmwasm/wasm/v1/contract/{address}/history\x12\xa4\x01\n\x0f\x43ontractsByCode\x12-.cosmwasm.wasm.v1.QueryContractsByCodeRequest\x1a..cosmwasm.wasm.v1.QueryContractsByCodeResponse\"2\x82\xd3\xe4\x93\x02,\x12*/cosmwasm/wasm/v1/code/{code_id}/contracts\x12\xa7\x01\n\x10\x41llContractState\x12..cosmwasm.wasm.v1.QueryAllContractStateRequest\x1a/.cosmwasm.wasm.v1.QueryAllContractStateResponse\"2\x82\xd3\xe4\x93\x02,\x12*/cosmwasm/wasm/v1/contract/{address}/state\x12\xb2\x01\n\x10RawContractState\x12..cosmwasm.wasm.v1.QueryRawContractStateRequest\x1a/.cosmwasm.wasm.v1.QueryRawContractStateResponse\"=\x82\xd3\xe4\x93\x02\x37\x12\x35/cosmwasm/wasm/v1/contract/{address}/raw/{query_data}\x12\xba\x01\n\x12SmartContractState\x12\x30.cosmwasm.wasm.v1.QuerySmartContractStateRequest\x1a\x31.cosmwasm.wasm.v1.QuerySmartContractStateResponse\"?\x82\xd3\xe4\x93\x02\x39\x12\x37/cosmwasm/wasm/v1/contract/{address}/smart/{query_data}\x12y\n\x04\x43ode\x12\".cosmwasm.wasm.v1.QueryCodeRequest\x1a#.cosmwasm.wasm.v1.QueryCodeResponse\"(\x82\xd3\xe4\x93\x02\"\x12 /cosmwasm/wasm/v1/code/{code_id}\x12r\n\x05\x43odes\x12#.cosmwasm.wasm.v1.QueryCodesRequest\x1a$.cosmwasm.wasm.v1.QueryCodesResponse\"\x1e\x82\xd3\xe4\x93\x02\x18\x12\x16/cosmwasm/wasm/v1/code\x12\x8c\x01\n\x0bPinnedCodes\x12).cosmwasm.wasm.v1.QueryPinnedCodesRequest\x1a*.cosmwasm.wasm.v1.QueryPinnedCodesResponse\"&\x82\xd3\xe4\x93\x02 \x12\x1e/cosmwasm/wasm/v1/codes/pinned\x12}\n\x06Params\x12$.cosmwasm.wasm.v1.QueryParamsRequest\x1a%.cosmwasm.wasm.v1.QueryParamsResponse\"&\x82\xd3\xe4\x93\x02 \x12\x1e/cosmwasm/wasm/v1/codes/params\x12\xb8\x01\n\x12\x43ontractsByCreator\x12\x30.cosmwasm.wasm.v1.QueryContractsByCreatorRequest\x1a\x31.cosmwasm.wasm.v1.QueryContractsByCreatorResponse\"=\x82\xd3\xe4\x93\x02\x37\x12\x35/cosmwasm/wasm/v1/contracts/creator/{creator_address}B0Z&github.com/CosmWasm/wasmd/x/wasm/types\xc8\xe1\x1e\x00\xa8\xe2\x1e\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmwasm.wasm.v1.query_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z&github.com/CosmWasm/wasmd/x/wasm/types\310\341\036\000\250\342\036\000'
  _QUERYCONTRACTINFOREQUEST.fields_by_name['address']._options = None
  _QUERYCONTRACTINFOREQUEST.fields_by_name['address']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _QUERYCONTRACTINFORESPONSE.fields_by_name['address']._options = None
  _QUERYCONTRACTINFORESPONSE.fields_by_name['address']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _QUERYCONTRACTINFORESPONSE.fields_by_name['contract_info']._options = None
  _QUERYCONTRACTINFORESPONSE.fields_by_name['contract_info']._serialized_options = b'\310\336\037\000\320\336\037\001\352\336\037\000\250\347\260*\001'
  _QUERYCONTRACTINFORESPONSE._options = None
  _QUERYCONTRACTINFORESPONSE._serialized_options = b'\350\240\037\001'
  _QUERYCONTRACTHISTORYREQUEST.fields_by_name['address']._options = None
  _QUERYCONTRACTHISTORYREQUEST.fields_by_name['address']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _QUERYCONTRACTHISTORYRESPONSE.fields_by_name['entries']._options = None
  _QUERYCONTRACTHISTORYRESPONSE.fields_by_name['entries']._serialized_options = b'\310\336\037\000\250\347\260*\001'
  _QUERYCONTRACTSBYCODERESPONSE.fields_by_name['contracts']._options = None
  _QUERYCONTRACTSBYCODERESPONSE.fields_by_name['contracts']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _QUERYALLCONTRACTSTATEREQUEST.fields_by_name['address']._options = None
  _QUERYALLCONTRACTSTATEREQUEST.fields_by_name['address']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _QUERYALLCONTRACTSTATERESPONSE.fields_by_name['models']._options = None
  _QUERYALLCONTRACTSTATERESPONSE.fields_by_name['models']._serialized_options = b'\310\336\037\000\250\347\260*\001'
  _QUERYRAWCONTRACTSTATEREQUEST.fields_by_name['address']._options = None
  _QUERYRAWCONTRACTSTATEREQUEST.fields_by_name['address']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _QUERYSMARTCONTRACTSTATEREQUEST.fields_by_name['address']._options = None
  _QUERYSMARTCONTRACTSTATEREQUEST.fields_by_name['address']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _QUERYSMARTCONTRACTSTATEREQUEST.fields_by_name['query_data']._options = None
  _QUERYSMARTCONTRACTSTATEREQUEST.fields_by_name['query_data']._serialized_options = b'\372\336\037\022RawContractMessage'
  _QUERYSMARTCONTRACTSTATERESPONSE.fields_by_name['data']._options = None
  _QUERYSMARTCONTRACTSTATERESPONSE.fields_by_name['data']._serialized_options = b'\372\336\037\022RawContractMessage'
  _CODEINFORESPONSE.fields_by_name['code_id']._options = None
  _CODEINFORESPONSE.fields_by_name['code_id']._serialized_options = b'\342\336\037\006CodeID\352\336\037\002id'
  _CODEINFORESPONSE.fields_by_name['creator']._options = None
  _CODEINFORESPONSE.fields_by_name['creator']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _CODEINFORESPONSE.fields_by_name['data_hash']._options = None
  _CODEINFORESPONSE.fields_by_name['data_hash']._serialized_options = b'\372\336\0370github.com/cometbft/cometbft/libs/bytes.HexBytes'
  _CODEINFORESPONSE.fields_by_name['instantiate_permission']._options = None
  _CODEINFORESPONSE.fields_by_name['instantiate_permission']._serialized_options = b'\310\336\037\000\250\347\260*\001'
  _CODEINFORESPONSE._options = None
  _CODEINFORESPONSE._serialized_options = b'\350\240\037\001'
  _QUERYCODERESPONSE.fields_by_name['code_info']._options = None
  _QUERYCODERESPONSE.fields_by_name['code_info']._serialized_options = b'\320\336\037\001\352\336\037\000'
  _QUERYCODERESPONSE.fields_by_name['data']._options = None
  _QUERYCODERESPONSE.fields_by_name['data']._serialized_options = b'\352\336\037\004data'
  _QUERYCODERESPONSE._options = None
  _QUERYCODERESPONSE._serialized_options = b'\350\240\037\001'
  _QUERYCODESRESPONSE.fields_by_name['code_infos']._options = None
  _QUERYCODESRESPONSE.fields_by_name['code_infos']._serialized_options = b'\310\336\037\000\250\347\260*\001'
  _QUERYPINNEDCODESRESPONSE.fields_by_name['code_ids']._options = None
  _QUERYPINNEDCODESRESPONSE.fields_by_name['code_ids']._serialized_options = b'\342\336\037\007CodeIDs'
  _QUERYPARAMSRESPONSE.fields_by_name['params']._options = None
  _QUERYPARAMSRESPONSE.fields_by_name['params']._serialized_options = b'\310\336\037\000\250\347\260*\001'
  _QUERYCONTRACTSBYCREATORREQUEST.fields_by_name['creator_address']._options = None
  _QUERYCONTRACTSBYCREATORREQUEST.fields_by_name['creator_address']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _QUERYCONTRACTSBYCREATORRESPONSE.fields_by_name['contract_addresses']._options = None
  _QUERYCONTRACTSBYCREATORRESPONSE.fields_by_name['contract_addresses']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _QUERY.methods_by_name['ContractInfo']._options = None
  _QUERY.methods_by_name['ContractInfo']._serialized_options = b'\202\323\344\223\002&\022$/cosmwasm/wasm/v1/contract/{address}'
  _QUERY.methods_by_name['ContractHistory']._options = None
  _QUERY.methods_by_name['ContractHistory']._serialized_options = b'\202\323\344\223\002.\022,/cosmwasm/wasm/v1/contract/{address}/history'
  _QUERY.methods_by_name['ContractsByCode']._options = None
  _QUERY.methods_by_name['ContractsByCode']._serialized_options = b'\202\323\344\223\002,\022*/cosmwasm/wasm/v1/code/{code_id}/contracts'
  _QUERY.methods_by_name['AllContractState']._options = None
  _QUERY.methods_by_name['AllContractState']._serialized_options = b'\202\323\344\223\002,\022*/cosmwasm/wasm/v1/contract/{address}/state'
  _QUERY.methods_by_name['RawContractState']._options = None
  _QUERY.methods_by_name['RawContractState']._serialized_options = b'\202\323\344\223\0027\0225/cosmwasm/wasm/v1/contract/{address}/raw/{query_data}'
  _QUERY.methods_by_name['SmartContractState']._options = None
  _QUERY.methods_by_name['SmartContractState']._serialized_options = b'\202\323\344\223\0029\0227/cosmwasm/wasm/v1/contract/{address}/smart/{query_data}'
  _QUERY.methods_by_name['Code']._options = None
  _QUERY.methods_by_name['Code']._serialized_options = b'\202\323\344\223\002\"\022 /cosmwasm/wasm/v1/code/{code_id}'
  _QUERY.methods_by_name['Codes']._options = None
  _QUERY.methods_by_name['Codes']._serialized_options = b'\202\323\344\223\002\030\022\026/cosmwasm/wasm/v1/code'
  _QUERY.methods_by_name['PinnedCodes']._options = None
  _QUERY.methods_by_name['PinnedCodes']._serialized_options = b'\202\323\344\223\002 \022\036/cosmwasm/wasm/v1/codes/pinned'
  _QUERY.methods_by_name['Params']._options = None
  _QUERY.methods_by_name['Params']._serialized_options = b'\202\323\344\223\002 \022\036/cosmwasm/wasm/v1/codes/params'
  _QUERY.methods_by_name['ContractsByCreator']._options = None
  _QUERY.methods_by_name['ContractsByCreator']._serialized_options = b'\202\323\344\223\0027\0225/cosmwasm/wasm/v1/contracts/creator/{creator_address}'
  _globals['_QUERYCONTRACTINFOREQUEST']._serialized_start=222
  _globals['_QUERYCONTRACTINFOREQUEST']._serialized_end=291
  _globals['_QUERYCONTRACTINFORESPONSE']._serialized_start=294
  _globals['_QUERYCONTRACTINFORESPONSE']._serialized_end=444
  _globals['_QUERYCONTRACTHISTORYREQUEST']._serialized_start=447
  _globals['_QUERYCONTRACTHISTORYREQUEST']._serialized_end=579
  _globals['_QUERYCONTRACTHISTORYRESPONSE']._serialized_start=582
  _globals['_QUERYCONTRACTHISTORYRESPONSE']._serialized_end=745
  _globals['_QUERYCONTRACTSBYCODEREQUEST']._serialized_start=747
  _globals['_QUERYCONTRACTSBYCODEREQUEST']._serialized_end=853
  _globals['_QUERYCONTRACTSBYCODERESPONSE']._serialized_start=856
  _globals['_QUERYCONTRACTSBYCODERESPONSE']._serialized_end=992
  _globals['_QUERYALLCONTRACTSTATEREQUEST']._serialized_start=995
  _globals['_QUERYALLCONTRACTSTATEREQUEST']._serialized_end=1128
  _globals['_QUERYALLCONTRACTSTATERESPONSE']._serialized_start=1131
  _globals['_QUERYALLCONTRACTSTATERESPONSE']._serialized_end=1275
  _globals['_QUERYRAWCONTRACTSTATEREQUEST']._serialized_start=1277
  _globals['_QUERYRAWCONTRACTSTATEREQUEST']._serialized_end=1370
  _globals['_QUERYRAWCONTRACTSTATERESPONSE']._serialized_start=1372
  _globals['_QUERYRAWCONTRACTSTATERESPONSE']._serialized_end=1417
  _globals['_QUERYSMARTCONTRACTSTATEREQUEST']._serialized_start=1419
  _globals['_QUERYSMARTCONTRACTSTATEREQUEST']._serialized_end=1538
  _globals['_QUERYSMARTCONTRACTSTATERESPONSE']._serialized_start=1540
  _globals['_QUERYSMARTCONTRACTSTATERESPONSE']._serialized_end=1611
  _globals['_QUERYCODEREQUEST']._serialized_start=1613
  _globals['_QUERYCODEREQUEST']._serialized_end=1648
  _globals['_CODEINFORESPONSE']._serialized_start=1651
  _globals['_CODEINFORESPONSE']._serialized_end=1913
  _globals['_QUERYCODERESPONSE']._serialized_start=1915
  _globals['_QUERYCODERESPONSE']._serialized_end=2029
  _globals['_QUERYCODESREQUEST']._serialized_start=2031
  _globals['_QUERYCODESREQUEST']._serialized_end=2110
  _globals['_QUERYCODESRESPONSE']._serialized_start=2113
  _globals['_QUERYCODESRESPONSE']._serialized_end=2261
  _globals['_QUERYPINNEDCODESREQUEST']._serialized_start=2263
  _globals['_QUERYPINNEDCODESREQUEST']._serialized_end=2348
  _globals['_QUERYPINNEDCODESRESPONSE']._serialized_start=2350
  _globals['_QUERYPINNEDCODESRESPONSE']._serialized_end=2468
  _globals['_QUERYPARAMSREQUEST']._serialized_start=2470
  _globals['_QUERYPARAMSREQUEST']._serialized_end=2490
  _globals['_QUERYPARAMSRESPONSE']._serialized_start=2492
  _globals['_QUERYPARAMSRESPONSE']._serialized_end=2566
  _globals['_QUERYCONTRACTSBYCREATORREQUEST']._serialized_start=2569
  _globals['_QUERYCONTRACTSBYCREATORREQUEST']._serialized_end=2712
  _globals['_QUERYCONTRACTSBYCREATORRESPONSE']._serialized_start=2715
  _globals['_QUERYCONTRACTSBYCREATORRESPONSE']._serialized_end=2863
  _globals['_QUERY']._serialized_start=2866
  _globals['_QUERY']._serialized_end=4597
# @@protoc_insertion_point(module_scope)
