# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: routing/v1alpha1/http_fault.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='routing/v1alpha1/http_fault.proto',
  package='istio.routing.v1alpha1',
  syntax='proto3',
  serialized_pb=_b('\n!routing/v1alpha1/http_fault.proto\x12\x16istio.routing.v1alpha1\x1a\x1egoogle/protobuf/duration.proto\"\xd8\x03\n\x12HTTPFaultInjection\x12?\n\x05\x64\x65lay\x18\x01 \x01(\x0b\x32\x30.istio.routing.v1alpha1.HTTPFaultInjection.Delay\x12?\n\x05\x61\x62ort\x18\x02 \x01(\x0b\x32\x30.istio.routing.v1alpha1.HTTPFaultInjection.Abort\x1a\xb3\x01\n\x05\x44\x65lay\x12\x0f\n\x07percent\x18\x01 \x01(\x02\x12\x30\n\x0b\x66ixed_delay\x18\x02 \x01(\x0b\x32\x19.google.protobuf.DurationH\x00\x12\x36\n\x11\x65xponential_delay\x18\x03 \x01(\x0b\x32\x19.google.protobuf.DurationH\x00\x12\x1c\n\x14override_header_name\x18\x04 \x01(\tB\x11\n\x0fhttp_delay_type\x1a\x89\x01\n\x05\x41\x62ort\x12\x0f\n\x07percent\x18\x01 \x01(\x02\x12\x15\n\x0bgrpc_status\x18\x02 \x01(\tH\x00\x12\x15\n\x0bhttp2_error\x18\x03 \x01(\tH\x00\x12\x15\n\x0bhttp_status\x18\x04 \x01(\x05H\x00\x12\x1c\n\x14override_header_name\x18\x05 \x01(\tB\x0c\n\nerror_typeB\x1fZ\x1distio.io/api/routing/v1alpha1b\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_duration__pb2.DESCRIPTOR,])




_HTTPFAULTINJECTION_DELAY = _descriptor.Descriptor(
  name='Delay',
  full_name='istio.routing.v1alpha1.HTTPFaultInjection.Delay',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='percent', full_name='istio.routing.v1alpha1.HTTPFaultInjection.Delay.percent', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fixed_delay', full_name='istio.routing.v1alpha1.HTTPFaultInjection.Delay.fixed_delay', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='exponential_delay', full_name='istio.routing.v1alpha1.HTTPFaultInjection.Delay.exponential_delay', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='override_header_name', full_name='istio.routing.v1alpha1.HTTPFaultInjection.Delay.override_header_name', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='http_delay_type', full_name='istio.routing.v1alpha1.HTTPFaultInjection.Delay.http_delay_type',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=247,
  serialized_end=426,
)

_HTTPFAULTINJECTION_ABORT = _descriptor.Descriptor(
  name='Abort',
  full_name='istio.routing.v1alpha1.HTTPFaultInjection.Abort',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='percent', full_name='istio.routing.v1alpha1.HTTPFaultInjection.Abort.percent', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='grpc_status', full_name='istio.routing.v1alpha1.HTTPFaultInjection.Abort.grpc_status', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='http2_error', full_name='istio.routing.v1alpha1.HTTPFaultInjection.Abort.http2_error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='http_status', full_name='istio.routing.v1alpha1.HTTPFaultInjection.Abort.http_status', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='override_header_name', full_name='istio.routing.v1alpha1.HTTPFaultInjection.Abort.override_header_name', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='error_type', full_name='istio.routing.v1alpha1.HTTPFaultInjection.Abort.error_type',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=429,
  serialized_end=566,
)

_HTTPFAULTINJECTION = _descriptor.Descriptor(
  name='HTTPFaultInjection',
  full_name='istio.routing.v1alpha1.HTTPFaultInjection',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='delay', full_name='istio.routing.v1alpha1.HTTPFaultInjection.delay', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='abort', full_name='istio.routing.v1alpha1.HTTPFaultInjection.abort', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_HTTPFAULTINJECTION_DELAY, _HTTPFAULTINJECTION_ABORT, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=94,
  serialized_end=566,
)

_HTTPFAULTINJECTION_DELAY.fields_by_name['fixed_delay'].message_type = google_dot_protobuf_dot_duration__pb2._DURATION
_HTTPFAULTINJECTION_DELAY.fields_by_name['exponential_delay'].message_type = google_dot_protobuf_dot_duration__pb2._DURATION
_HTTPFAULTINJECTION_DELAY.containing_type = _HTTPFAULTINJECTION
_HTTPFAULTINJECTION_DELAY.oneofs_by_name['http_delay_type'].fields.append(
  _HTTPFAULTINJECTION_DELAY.fields_by_name['fixed_delay'])
_HTTPFAULTINJECTION_DELAY.fields_by_name['fixed_delay'].containing_oneof = _HTTPFAULTINJECTION_DELAY.oneofs_by_name['http_delay_type']
_HTTPFAULTINJECTION_DELAY.oneofs_by_name['http_delay_type'].fields.append(
  _HTTPFAULTINJECTION_DELAY.fields_by_name['exponential_delay'])
_HTTPFAULTINJECTION_DELAY.fields_by_name['exponential_delay'].containing_oneof = _HTTPFAULTINJECTION_DELAY.oneofs_by_name['http_delay_type']
_HTTPFAULTINJECTION_ABORT.containing_type = _HTTPFAULTINJECTION
_HTTPFAULTINJECTION_ABORT.oneofs_by_name['error_type'].fields.append(
  _HTTPFAULTINJECTION_ABORT.fields_by_name['grpc_status'])
_HTTPFAULTINJECTION_ABORT.fields_by_name['grpc_status'].containing_oneof = _HTTPFAULTINJECTION_ABORT.oneofs_by_name['error_type']
_HTTPFAULTINJECTION_ABORT.oneofs_by_name['error_type'].fields.append(
  _HTTPFAULTINJECTION_ABORT.fields_by_name['http2_error'])
_HTTPFAULTINJECTION_ABORT.fields_by_name['http2_error'].containing_oneof = _HTTPFAULTINJECTION_ABORT.oneofs_by_name['error_type']
_HTTPFAULTINJECTION_ABORT.oneofs_by_name['error_type'].fields.append(
  _HTTPFAULTINJECTION_ABORT.fields_by_name['http_status'])
_HTTPFAULTINJECTION_ABORT.fields_by_name['http_status'].containing_oneof = _HTTPFAULTINJECTION_ABORT.oneofs_by_name['error_type']
_HTTPFAULTINJECTION.fields_by_name['delay'].message_type = _HTTPFAULTINJECTION_DELAY
_HTTPFAULTINJECTION.fields_by_name['abort'].message_type = _HTTPFAULTINJECTION_ABORT
DESCRIPTOR.message_types_by_name['HTTPFaultInjection'] = _HTTPFAULTINJECTION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

HTTPFaultInjection = _reflection.GeneratedProtocolMessageType('HTTPFaultInjection', (_message.Message,), dict(

  Delay = _reflection.GeneratedProtocolMessageType('Delay', (_message.Message,), dict(
    DESCRIPTOR = _HTTPFAULTINJECTION_DELAY,
    __module__ = 'routing.v1alpha1.http_fault_pb2'
    # @@protoc_insertion_point(class_scope:istio.routing.v1alpha1.HTTPFaultInjection.Delay)
    ))
  ,

  Abort = _reflection.GeneratedProtocolMessageType('Abort', (_message.Message,), dict(
    DESCRIPTOR = _HTTPFAULTINJECTION_ABORT,
    __module__ = 'routing.v1alpha1.http_fault_pb2'
    # @@protoc_insertion_point(class_scope:istio.routing.v1alpha1.HTTPFaultInjection.Abort)
    ))
  ,
  DESCRIPTOR = _HTTPFAULTINJECTION,
  __module__ = 'routing.v1alpha1.http_fault_pb2'
  # @@protoc_insertion_point(class_scope:istio.routing.v1alpha1.HTTPFaultInjection)
  ))
_sym_db.RegisterMessage(HTTPFaultInjection)
_sym_db.RegisterMessage(HTTPFaultInjection.Delay)
_sym_db.RegisterMessage(HTTPFaultInjection.Abort)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('Z\035istio.io/api/routing/v1alpha1'))
# @@protoc_insertion_point(module_scope)
