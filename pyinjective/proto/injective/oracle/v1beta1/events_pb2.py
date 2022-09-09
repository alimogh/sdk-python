# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: injective/oracle/v1beta1/events.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='injective/oracle/v1beta1/events.proto',
  package='injective.oracle.v1beta1',
  syntax='proto3',
  serialized_options=b'ZLgithub.com/InjectiveLabs/injective-core/injective-chain/modules/oracle/types',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n%injective/oracle/v1beta1/events.proto\x12\x18injective.oracle.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x1e\x63osmos/base/v1beta1/coin.proto\"|\n\x16SetChainlinkPriceEvent\x12\x0f\n\x07\x66\x65\x65\x64_id\x18\x01 \x01(\t\x12>\n\x06\x61nswer\x18\x02 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\x12\x11\n\ttimestamp\x18\x03 \x01(\x04\"\x9d\x01\n\x11SetBandPriceEvent\x12\x0f\n\x07relayer\x18\x01 \x01(\t\x12\x0e\n\x06symbol\x18\x02 \x01(\t\x12=\n\x05price\x18\x03 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\x12\x14\n\x0cresolve_time\x18\x04 \x01(\x04\x12\x12\n\nrequest_id\x18\x05 \x01(\x04\"\xb5\x01\n\x14SetBandIBCPriceEvent\x12\x0f\n\x07relayer\x18\x01 \x01(\t\x12\x0f\n\x07symbols\x18\x02 \x03(\t\x12>\n\x06prices\x18\x03 \x03(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\x12\x14\n\x0cresolve_time\x18\x04 \x01(\x04\x12\x12\n\nrequest_id\x18\x05 \x01(\x04\x12\x11\n\tclient_id\x18\x06 \x01(\x03\"?\n\x16\x45ventBandIBCAckSuccess\x12\x12\n\nack_result\x18\x01 \x01(\t\x12\x11\n\tclient_id\x18\x02 \x01(\x03\"<\n\x14\x45ventBandIBCAckError\x12\x11\n\tack_error\x18\x01 \x01(\t\x12\x11\n\tclient_id\x18\x02 \x01(\x03\"0\n\x1b\x45ventBandIBCResponseTimeout\x12\x11\n\tclient_id\x18\x01 \x01(\x03\"\x85\x01\n\x16SetPriceFeedPriceEvent\x12\x0f\n\x07relayer\x18\x01 \x01(\t\x12\x0c\n\x04\x62\x61se\x18\x02 \x01(\t\x12\r\n\x05quote\x18\x03 \x01(\t\x12=\n\x05price\x18\x04 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\"\x89\x01\n\x15SetProviderPriceEvent\x12\x10\n\x08provider\x18\x01 \x01(\t\x12\x0f\n\x07relayer\x18\x02 \x01(\t\x12\x0e\n\x06symbol\x18\x03 \x01(\t\x12=\n\x05price\x18\x04 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\"y\n\x15SetCoinbasePriceEvent\x12\x0e\n\x06symbol\x18\x01 \x01(\t\x12=\n\x05price\x18\x02 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\x12\x11\n\ttimestamp\x18\x03 \x01(\x04\x42NZLgithub.com/InjectiveLabs/injective-core/injective-chain/modules/oracle/typesb\x06proto3'
  ,
  dependencies=[gogoproto_dot_gogo__pb2.DESCRIPTOR,cosmos_dot_base_dot_v1beta1_dot_coin__pb2.DESCRIPTOR,])




_SETCHAINLINKPRICEEVENT = _descriptor.Descriptor(
  name='SetChainlinkPriceEvent',
  full_name='injective.oracle.v1beta1.SetChainlinkPriceEvent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='feed_id', full_name='injective.oracle.v1beta1.SetChainlinkPriceEvent.feed_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='answer', full_name='injective.oracle.v1beta1.SetChainlinkPriceEvent.answer', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\310\336\037\000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='injective.oracle.v1beta1.SetChainlinkPriceEvent.timestamp', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=121,
  serialized_end=245,
)


_SETBANDPRICEEVENT = _descriptor.Descriptor(
  name='SetBandPriceEvent',
  full_name='injective.oracle.v1beta1.SetBandPriceEvent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='relayer', full_name='injective.oracle.v1beta1.SetBandPriceEvent.relayer', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='symbol', full_name='injective.oracle.v1beta1.SetBandPriceEvent.symbol', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='price', full_name='injective.oracle.v1beta1.SetBandPriceEvent.price', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\310\336\037\000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='resolve_time', full_name='injective.oracle.v1beta1.SetBandPriceEvent.resolve_time', index=3,
      number=4, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='request_id', full_name='injective.oracle.v1beta1.SetBandPriceEvent.request_id', index=4,
      number=5, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=248,
  serialized_end=405,
)


_SETBANDIBCPRICEEVENT = _descriptor.Descriptor(
  name='SetBandIBCPriceEvent',
  full_name='injective.oracle.v1beta1.SetBandIBCPriceEvent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='relayer', full_name='injective.oracle.v1beta1.SetBandIBCPriceEvent.relayer', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='symbols', full_name='injective.oracle.v1beta1.SetBandIBCPriceEvent.symbols', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='prices', full_name='injective.oracle.v1beta1.SetBandIBCPriceEvent.prices', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\310\336\037\000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='resolve_time', full_name='injective.oracle.v1beta1.SetBandIBCPriceEvent.resolve_time', index=3,
      number=4, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='request_id', full_name='injective.oracle.v1beta1.SetBandIBCPriceEvent.request_id', index=4,
      number=5, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='client_id', full_name='injective.oracle.v1beta1.SetBandIBCPriceEvent.client_id', index=5,
      number=6, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=408,
  serialized_end=589,
)


_EVENTBANDIBCACKSUCCESS = _descriptor.Descriptor(
  name='EventBandIBCAckSuccess',
  full_name='injective.oracle.v1beta1.EventBandIBCAckSuccess',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='ack_result', full_name='injective.oracle.v1beta1.EventBandIBCAckSuccess.ack_result', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='client_id', full_name='injective.oracle.v1beta1.EventBandIBCAckSuccess.client_id', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=591,
  serialized_end=654,
)


_EVENTBANDIBCACKERROR = _descriptor.Descriptor(
  name='EventBandIBCAckError',
  full_name='injective.oracle.v1beta1.EventBandIBCAckError',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='ack_error', full_name='injective.oracle.v1beta1.EventBandIBCAckError.ack_error', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='client_id', full_name='injective.oracle.v1beta1.EventBandIBCAckError.client_id', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=656,
  serialized_end=716,
)


_EVENTBANDIBCRESPONSETIMEOUT = _descriptor.Descriptor(
  name='EventBandIBCResponseTimeout',
  full_name='injective.oracle.v1beta1.EventBandIBCResponseTimeout',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='client_id', full_name='injective.oracle.v1beta1.EventBandIBCResponseTimeout.client_id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=718,
  serialized_end=766,
)


_SETPRICEFEEDPRICEEVENT = _descriptor.Descriptor(
  name='SetPriceFeedPriceEvent',
  full_name='injective.oracle.v1beta1.SetPriceFeedPriceEvent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='relayer', full_name='injective.oracle.v1beta1.SetPriceFeedPriceEvent.relayer', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='base', full_name='injective.oracle.v1beta1.SetPriceFeedPriceEvent.base', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='quote', full_name='injective.oracle.v1beta1.SetPriceFeedPriceEvent.quote', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='price', full_name='injective.oracle.v1beta1.SetPriceFeedPriceEvent.price', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\310\336\037\000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=769,
  serialized_end=902,
)


_SETPROVIDERPRICEEVENT = _descriptor.Descriptor(
  name='SetProviderPriceEvent',
  full_name='injective.oracle.v1beta1.SetProviderPriceEvent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='provider', full_name='injective.oracle.v1beta1.SetProviderPriceEvent.provider', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='relayer', full_name='injective.oracle.v1beta1.SetProviderPriceEvent.relayer', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='symbol', full_name='injective.oracle.v1beta1.SetProviderPriceEvent.symbol', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='price', full_name='injective.oracle.v1beta1.SetProviderPriceEvent.price', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\310\336\037\000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=905,
  serialized_end=1042,
)


_SETCOINBASEPRICEEVENT = _descriptor.Descriptor(
  name='SetCoinbasePriceEvent',
  full_name='injective.oracle.v1beta1.SetCoinbasePriceEvent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='symbol', full_name='injective.oracle.v1beta1.SetCoinbasePriceEvent.symbol', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='price', full_name='injective.oracle.v1beta1.SetCoinbasePriceEvent.price', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\310\336\037\000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='injective.oracle.v1beta1.SetCoinbasePriceEvent.timestamp', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1044,
  serialized_end=1165,
)

DESCRIPTOR.message_types_by_name['SetChainlinkPriceEvent'] = _SETCHAINLINKPRICEEVENT
DESCRIPTOR.message_types_by_name['SetBandPriceEvent'] = _SETBANDPRICEEVENT
DESCRIPTOR.message_types_by_name['SetBandIBCPriceEvent'] = _SETBANDIBCPRICEEVENT
DESCRIPTOR.message_types_by_name['EventBandIBCAckSuccess'] = _EVENTBANDIBCACKSUCCESS
DESCRIPTOR.message_types_by_name['EventBandIBCAckError'] = _EVENTBANDIBCACKERROR
DESCRIPTOR.message_types_by_name['EventBandIBCResponseTimeout'] = _EVENTBANDIBCRESPONSETIMEOUT
DESCRIPTOR.message_types_by_name['SetPriceFeedPriceEvent'] = _SETPRICEFEEDPRICEEVENT
DESCRIPTOR.message_types_by_name['SetProviderPriceEvent'] = _SETPROVIDERPRICEEVENT
DESCRIPTOR.message_types_by_name['SetCoinbasePriceEvent'] = _SETCOINBASEPRICEEVENT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SetChainlinkPriceEvent = _reflection.GeneratedProtocolMessageType('SetChainlinkPriceEvent', (_message.Message,), {
  'DESCRIPTOR' : _SETCHAINLINKPRICEEVENT,
  '__module__' : 'injective.oracle.v1beta1.events_pb2'
  # @@protoc_insertion_point(class_scope:injective.oracle.v1beta1.SetChainlinkPriceEvent)
  })
_sym_db.RegisterMessage(SetChainlinkPriceEvent)

SetBandPriceEvent = _reflection.GeneratedProtocolMessageType('SetBandPriceEvent', (_message.Message,), {
  'DESCRIPTOR' : _SETBANDPRICEEVENT,
  '__module__' : 'injective.oracle.v1beta1.events_pb2'
  # @@protoc_insertion_point(class_scope:injective.oracle.v1beta1.SetBandPriceEvent)
  })
_sym_db.RegisterMessage(SetBandPriceEvent)

SetBandIBCPriceEvent = _reflection.GeneratedProtocolMessageType('SetBandIBCPriceEvent', (_message.Message,), {
  'DESCRIPTOR' : _SETBANDIBCPRICEEVENT,
  '__module__' : 'injective.oracle.v1beta1.events_pb2'
  # @@protoc_insertion_point(class_scope:injective.oracle.v1beta1.SetBandIBCPriceEvent)
  })
_sym_db.RegisterMessage(SetBandIBCPriceEvent)

EventBandIBCAckSuccess = _reflection.GeneratedProtocolMessageType('EventBandIBCAckSuccess', (_message.Message,), {
  'DESCRIPTOR' : _EVENTBANDIBCACKSUCCESS,
  '__module__' : 'injective.oracle.v1beta1.events_pb2'
  # @@protoc_insertion_point(class_scope:injective.oracle.v1beta1.EventBandIBCAckSuccess)
  })
_sym_db.RegisterMessage(EventBandIBCAckSuccess)

EventBandIBCAckError = _reflection.GeneratedProtocolMessageType('EventBandIBCAckError', (_message.Message,), {
  'DESCRIPTOR' : _EVENTBANDIBCACKERROR,
  '__module__' : 'injective.oracle.v1beta1.events_pb2'
  # @@protoc_insertion_point(class_scope:injective.oracle.v1beta1.EventBandIBCAckError)
  })
_sym_db.RegisterMessage(EventBandIBCAckError)

EventBandIBCResponseTimeout = _reflection.GeneratedProtocolMessageType('EventBandIBCResponseTimeout', (_message.Message,), {
  'DESCRIPTOR' : _EVENTBANDIBCRESPONSETIMEOUT,
  '__module__' : 'injective.oracle.v1beta1.events_pb2'
  # @@protoc_insertion_point(class_scope:injective.oracle.v1beta1.EventBandIBCResponseTimeout)
  })
_sym_db.RegisterMessage(EventBandIBCResponseTimeout)

SetPriceFeedPriceEvent = _reflection.GeneratedProtocolMessageType('SetPriceFeedPriceEvent', (_message.Message,), {
  'DESCRIPTOR' : _SETPRICEFEEDPRICEEVENT,
  '__module__' : 'injective.oracle.v1beta1.events_pb2'
  # @@protoc_insertion_point(class_scope:injective.oracle.v1beta1.SetPriceFeedPriceEvent)
  })
_sym_db.RegisterMessage(SetPriceFeedPriceEvent)

SetProviderPriceEvent = _reflection.GeneratedProtocolMessageType('SetProviderPriceEvent', (_message.Message,), {
  'DESCRIPTOR' : _SETPROVIDERPRICEEVENT,
  '__module__' : 'injective.oracle.v1beta1.events_pb2'
  # @@protoc_insertion_point(class_scope:injective.oracle.v1beta1.SetProviderPriceEvent)
  })
_sym_db.RegisterMessage(SetProviderPriceEvent)

SetCoinbasePriceEvent = _reflection.GeneratedProtocolMessageType('SetCoinbasePriceEvent', (_message.Message,), {
  'DESCRIPTOR' : _SETCOINBASEPRICEEVENT,
  '__module__' : 'injective.oracle.v1beta1.events_pb2'
  # @@protoc_insertion_point(class_scope:injective.oracle.v1beta1.SetCoinbasePriceEvent)
  })
_sym_db.RegisterMessage(SetCoinbasePriceEvent)


DESCRIPTOR._options = None
_SETCHAINLINKPRICEEVENT.fields_by_name['answer']._options = None
_SETBANDPRICEEVENT.fields_by_name['price']._options = None
_SETBANDIBCPRICEEVENT.fields_by_name['prices']._options = None
_SETPRICEFEEDPRICEEVENT.fields_by_name['price']._options = None
_SETPROVIDERPRICEEVENT.fields_by_name['price']._options = None
_SETCOINBASEPRICEEVENT.fields_by_name['price']._options = None
# @@protoc_insertion_point(module_scope)