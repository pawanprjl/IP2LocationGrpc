import grpc
from concurrent import futures
import time

import ip_to_address_pb2
import ip_to_address_pb2_grpc

import ip_to_address


class IpAddressServicer(ip_to_address_pb2_grpc.IpToAddressServicer):
    def Location(self, request, context):
        response = ip_to_address_pb2.IP()
        response.value = ip_to_address.ip_to_address(request.value)
        return response


server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

ip_to_address_pb2_grpc.add_IpToAddressServicer_to_server(IpAddressServicer(), server)

print('Starting server. Listening on port 50051.')
server.add_insecure_port('[::]:50051')
server.start()

try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop()