import socket
import struct
import pickle

# Mulicats IP and PORT are assigned 
MULTICAST_GROUP_1 = '224.1.1.1'
MULTICAST_GROUP_2 = '224.1.1.2'
MULTICAST_PORT = 12000
socket2=('',12000)

# SOcket is cretaed for Client2 and binded
socket_client2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
socket_client2.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 255)
socket_client2.bind(socket2)

#struct module is used for data conversion
message_request_1 = struct.pack("4sl", socket.inet_aton(MULTICAST_GROUP_1), socket.INADDR_ANY)
message_request_2 = struct.pack("4sl", socket.inet_aton(MULTICAST_GROUP_2), socket.INADDR_ANY)

#Setting the value of the given socket option, value can be an integer or a string representing a buffer
socket_client2.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, message_request_1)
socket_client2.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, message_request_2)

#Client receiving the Multicast Message from Server1 and Server2
while True:
    server_number = pickle.loads(socket_client2.recv(10240))
    data, address = socket_client2.recvfrom(10240)
    
    if server_number == 1 :
        print( ' Client 2: Data Received from %s \n and the Received Data is %s' % ( address, data))
    else :
        print ( ' Client 2: Data Received from %s  \n and the Received Data is %s' % ( address, data))
    
