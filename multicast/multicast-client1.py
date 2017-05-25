import socket
import struct
import pickle

# Assigning IP to multicast group and port number
MULTICAST_GROUP_1 = '224.1.1.1'

MULTICAST_GROUP_2 = '224.1.1.2'

MULTICAST_PORT = 12000

socket_name=('', 12000)

#Created Socket for Client1
socket_client1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
socket_client1.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 225)
socket_client1.bind(socket_name)

#struct module is used for data conversion
message_request_1 = struct.pack("4sl", socket.inet_aton(MULTICAST_GROUP_1), socket.INADDR_ANY)
message_request_2 = struct.pack("4sl", socket.inet_aton(MULTICAST_GROUP_2), socket.INADDR_ANY)

#Setting the value of the given socket option, value can be an integer or a string representing a buffer
socket_client1.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, message_request_1)
socket_client1.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, message_request_2)

#Client receiving the Multicast Message from Server1 and Server2
while True:
    server_number = pickle.loads (socket_client1.recv(10240))
    data, address = socket_client1.recvfrom(1024)
    
    
    if server_number == 1:
        print( ' Client 1: Data Received from %s  \n and the Received Data is %s' % ( address, data))
    else :
        print ( ' Client 1: Data Received from %s  \n and  the Received Data is %s' % ( address, data))
