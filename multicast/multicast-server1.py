import socket
import pickle
import time

#Defined Multicast group and multicast port number
MULTICAST_GROUP_1 = '127.0.0.1'
MULTICAST_PORT = 12000

# Created Socket for UDP Multicast
socket_server1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
socket_server1.setsockopt (socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 255)

#data sending to client
message = bytes( ' Multicasting Assignment ECE 9303A from Server 1 ' , 'utf-8')
#Server delivering the Multicast Message to Client1 and Client2
while True:
    socket_server1.sendto( pickle.dumps(1),(MULTICAST_GROUP_1, MULTICAST_PORT))
    socket_server1.sendto(message, (MULTICAST_GROUP_1, MULTICAST_PORT))
    print( 'Server 1 : multicast packet is sent now' )
    time.sleep(3)
