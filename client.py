import grpc

import ip_to_address_pb2_grpc
import ip_to_address_pb2

channel = grpc.insecure_channel('localhost:50051')
stub = ip_to_address_pb2_grpc.IpToAddressStub(channel)
ip = ip_to_address_pb2.IP(value='45.64.161.176')
response = stub.Location(ip)
print(response.value)