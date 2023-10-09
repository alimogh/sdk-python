# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: injective/auction/v1beta1/auction.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'injective/auction/v1beta1/auction.proto\x12\x19injective.auction.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x1e\x63osmos/base/v1beta1/coin.proto\"{\n\x06Params\x12\x16\n\x0e\x61uction_period\x18\x01 \x01(\x03\x12S\n\x1bmin_next_bid_increment_rate\x18\x02 \x01(\tB.\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec:\x04\xe8\xa0\x1f\x01\"s\n\x03\x42id\x12+\n\x06\x62idder\x18\x01 \x01(\tB\x1b\xea\xde\x1f\x06\x62idder\xf2\xde\x1f\ryaml:\"bidder\"\x12?\n\x06\x61mount\x18\x02 \x01(\tB/\xc8\xde\x1f\x00\xda\xde\x1f\'github.com/cosmos/cosmos-sdk/types.Coin\"j\n\x08\x45ventBid\x12\x0e\n\x06\x62idder\x18\x01 \x01(\t\x12?\n\x06\x61mount\x18\x02 \x01(\tB/\xc8\xde\x1f\x00\xda\xde\x1f\'github.com/cosmos/cosmos-sdk/types.Coin\x12\r\n\x05round\x18\x03 \x01(\x04\"t\n\x12\x45ventAuctionResult\x12\x0e\n\x06winner\x18\x01 \x01(\t\x12?\n\x06\x61mount\x18\x02 \x01(\tB/\xc8\xde\x1f\x00\xda\xde\x1f\'github.com/cosmos/cosmos-sdk/types.Coin\x12\r\n\x05round\x18\x03 \x01(\x04\"\x9d\x01\n\x11\x45ventAuctionStart\x12\r\n\x05round\x18\x01 \x01(\x04\x12\x18\n\x10\x65nding_timestamp\x18\x02 \x01(\x03\x12_\n\nnew_basket\x18\x03 \x03(\x0b\x32\x19.cosmos.base.v1beta1.CoinB0\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.CoinsBOZMgithub.com/InjectiveLabs/injective-core/injective-chain/modules/auction/typesb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'injective.auction.v1beta1.auction_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'ZMgithub.com/InjectiveLabs/injective-core/injective-chain/modules/auction/types'
  _PARAMS.fields_by_name['min_next_bid_increment_rate']._options = None
  _PARAMS.fields_by_name['min_next_bid_increment_rate']._serialized_options = b'\310\336\037\000\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec'
  _PARAMS._options = None
  _PARAMS._serialized_options = b'\350\240\037\001'
  _BID.fields_by_name['bidder']._options = None
  _BID.fields_by_name['bidder']._serialized_options = b'\352\336\037\006bidder\362\336\037\ryaml:\"bidder\"'
  _BID.fields_by_name['amount']._options = None
  _BID.fields_by_name['amount']._serialized_options = b'\310\336\037\000\332\336\037\'github.com/cosmos/cosmos-sdk/types.Coin'
  _EVENTBID.fields_by_name['amount']._options = None
  _EVENTBID.fields_by_name['amount']._serialized_options = b'\310\336\037\000\332\336\037\'github.com/cosmos/cosmos-sdk/types.Coin'
  _EVENTAUCTIONRESULT.fields_by_name['amount']._options = None
  _EVENTAUCTIONRESULT.fields_by_name['amount']._serialized_options = b'\310\336\037\000\332\336\037\'github.com/cosmos/cosmos-sdk/types.Coin'
  _EVENTAUCTIONSTART.fields_by_name['new_basket']._options = None
  _EVENTAUCTIONSTART.fields_by_name['new_basket']._serialized_options = b'\310\336\037\000\252\337\037(github.com/cosmos/cosmos-sdk/types.Coins'
  _globals['_PARAMS']._serialized_start=124
  _globals['_PARAMS']._serialized_end=247
  _globals['_BID']._serialized_start=249
  _globals['_BID']._serialized_end=364
  _globals['_EVENTBID']._serialized_start=366
  _globals['_EVENTBID']._serialized_end=472
  _globals['_EVENTAUCTIONRESULT']._serialized_start=474
  _globals['_EVENTAUCTIONRESULT']._serialized_end=590
  _globals['_EVENTAUCTIONSTART']._serialized_start=593
  _globals['_EVENTAUCTIONSTART']._serialized_end=750
# @@protoc_insertion_point(module_scope)
