# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tendermint/privval/types.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from tendermint.crypto import keys_pb2 as tendermint_dot_crypto_dot_keys__pb2
from tendermint.types import types_pb2 as tendermint_dot_types_dot_types__pb2
from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1etendermint/privval/types.proto\x12\x12tendermint.privval\x1a\x1ctendermint/crypto/keys.proto\x1a\x1ctendermint/types/types.proto\x1a\x14gogoproto/gogo.proto\"6\n\x11RemoteSignerError\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\"!\n\rPubKeyRequest\x12\x10\n\x08\x63hain_id\x18\x01 \x01(\t\"{\n\x0ePubKeyResponse\x12\x33\n\x07pub_key\x18\x01 \x01(\x0b\x32\x1c.tendermint.crypto.PublicKeyB\x04\xc8\xde\x1f\x00\x12\x34\n\x05\x65rror\x18\x02 \x01(\x0b\x32%.tendermint.privval.RemoteSignerError\"I\n\x0fSignVoteRequest\x12$\n\x04vote\x18\x01 \x01(\x0b\x32\x16.tendermint.types.Vote\x12\x10\n\x08\x63hain_id\x18\x02 \x01(\t\"v\n\x12SignedVoteResponse\x12*\n\x04vote\x18\x01 \x01(\x0b\x32\x16.tendermint.types.VoteB\x04\xc8\xde\x1f\x00\x12\x34\n\x05\x65rror\x18\x02 \x01(\x0b\x32%.tendermint.privval.RemoteSignerError\"U\n\x13SignProposalRequest\x12,\n\x08proposal\x18\x01 \x01(\x0b\x32\x1a.tendermint.types.Proposal\x12\x10\n\x08\x63hain_id\x18\x02 \x01(\t\"\x82\x01\n\x16SignedProposalResponse\x12\x32\n\x08proposal\x18\x01 \x01(\x0b\x32\x1a.tendermint.types.ProposalB\x04\xc8\xde\x1f\x00\x12\x34\n\x05\x65rror\x18\x02 \x01(\x0b\x32%.tendermint.privval.RemoteSignerError\"\r\n\x0bPingRequest\"\x0e\n\x0cPingResponse\"\xa6\x04\n\x07Message\x12<\n\x0fpub_key_request\x18\x01 \x01(\x0b\x32!.tendermint.privval.PubKeyRequestH\x00\x12>\n\x10pub_key_response\x18\x02 \x01(\x0b\x32\".tendermint.privval.PubKeyResponseH\x00\x12@\n\x11sign_vote_request\x18\x03 \x01(\x0b\x32#.tendermint.privval.SignVoteRequestH\x00\x12\x46\n\x14signed_vote_response\x18\x04 \x01(\x0b\x32&.tendermint.privval.SignedVoteResponseH\x00\x12H\n\x15sign_proposal_request\x18\x05 \x01(\x0b\x32\'.tendermint.privval.SignProposalRequestH\x00\x12N\n\x18signed_proposal_response\x18\x06 \x01(\x0b\x32*.tendermint.privval.SignedProposalResponseH\x00\x12\x37\n\x0cping_request\x18\x07 \x01(\x0b\x32\x1f.tendermint.privval.PingRequestH\x00\x12\x39\n\rping_response\x18\x08 \x01(\x0b\x32 .tendermint.privval.PingResponseH\x00\x42\x05\n\x03sum*\xa8\x01\n\x06\x45rrors\x12\x12\n\x0e\x45RRORS_UNKNOWN\x10\x00\x12\x1e\n\x1a\x45RRORS_UNEXPECTED_RESPONSE\x10\x01\x12\x18\n\x14\x45RRORS_NO_CONNECTION\x10\x02\x12\x1d\n\x19\x45RRORS_CONNECTION_TIMEOUT\x10\x03\x12\x17\n\x13\x45RRORS_READ_TIMEOUT\x10\x04\x12\x18\n\x14\x45RRORS_WRITE_TIMEOUT\x10\x05\x42\x37Z5github.com/cometbft/cometbft/proto/tendermint/privvalb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'tendermint.privval.types_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z5github.com/cometbft/cometbft/proto/tendermint/privval'
  _PUBKEYRESPONSE.fields_by_name['pub_key']._options = None
  _PUBKEYRESPONSE.fields_by_name['pub_key']._serialized_options = b'\310\336\037\000'
  _SIGNEDVOTERESPONSE.fields_by_name['vote']._options = None
  _SIGNEDVOTERESPONSE.fields_by_name['vote']._serialized_options = b'\310\336\037\000'
  _SIGNEDPROPOSALRESPONSE.fields_by_name['proposal']._options = None
  _SIGNEDPROPOSALRESPONSE.fields_by_name['proposal']._serialized_options = b'\310\336\037\000'
  _globals['_ERRORS']._serialized_start=1352
  _globals['_ERRORS']._serialized_end=1520
  _globals['_REMOTESIGNERERROR']._serialized_start=136
  _globals['_REMOTESIGNERERROR']._serialized_end=190
  _globals['_PUBKEYREQUEST']._serialized_start=192
  _globals['_PUBKEYREQUEST']._serialized_end=225
  _globals['_PUBKEYRESPONSE']._serialized_start=227
  _globals['_PUBKEYRESPONSE']._serialized_end=350
  _globals['_SIGNVOTEREQUEST']._serialized_start=352
  _globals['_SIGNVOTEREQUEST']._serialized_end=425
  _globals['_SIGNEDVOTERESPONSE']._serialized_start=427
  _globals['_SIGNEDVOTERESPONSE']._serialized_end=545
  _globals['_SIGNPROPOSALREQUEST']._serialized_start=547
  _globals['_SIGNPROPOSALREQUEST']._serialized_end=632
  _globals['_SIGNEDPROPOSALRESPONSE']._serialized_start=635
  _globals['_SIGNEDPROPOSALRESPONSE']._serialized_end=765
  _globals['_PINGREQUEST']._serialized_start=767
  _globals['_PINGREQUEST']._serialized_end=780
  _globals['_PINGRESPONSE']._serialized_start=782
  _globals['_PINGRESPONSE']._serialized_end=796
  _globals['_MESSAGE']._serialized_start=799
  _globals['_MESSAGE']._serialized_end=1349
# @@protoc_insertion_point(module_scope)
