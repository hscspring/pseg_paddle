# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from proto import pseg_pb2 as proto_dot_pseg__pb2


class PartOfSpeechStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Predict = channel.unary_unary(
        '/pseg.PartOfSpeech/Predict',
        request_serializer=proto_dot_pseg__pb2.PosRequest.SerializeToString,
        response_deserializer=proto_dot_pseg__pb2.PosResponse.FromString,
        )


class PartOfSpeechServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def Predict(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_PartOfSpeechServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Predict': grpc.unary_unary_rpc_method_handler(
          servicer.Predict,
          request_deserializer=proto_dot_pseg__pb2.PosRequest.FromString,
          response_serializer=proto_dot_pseg__pb2.PosResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'pseg.PartOfSpeech', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
