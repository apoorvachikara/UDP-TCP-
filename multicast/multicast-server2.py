import socket
import pickle
import time

#Defined Multicast group and multicast port number
MULTICAST_GROUP_2 = '127.0.0.1'
MULTICAST_PORT = 12000

# Created Socket for UDP Multicast
socket_server2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
socket_server2.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 255)

#data sending to client
message = bytes( ' Multicasting Assignment ECE 9303A from Server 2 ' , 'utf-8')
#Server delivering the Multicast Message to Client1 and Client2
while True:
    socket_server2.sendto( pickle.dumps(2),(MULTICAST_GROUP_2, MULTICAST_PORT))
    socket_server2.sendto(message, (MULTICAST_GROUP_2, MULTICAST_PORT))
    print ( ' Server 2 : multicast packet is sent now ' ) 
    time.sleep(3)
