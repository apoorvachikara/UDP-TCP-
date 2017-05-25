from struct import *
import time 
import pickle
from socket import *
 
# Create a UDP socket 
# Notice the use of SOCK_DGRAM for UDP packets 
SERVER_Socket = socket(AF_INET, SOCK_DGRAM) 
# Assign IP address and port number to socket
SERVER_Socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
SERVER_Socket.bind(('127.0.0.1', 12000))
SERVER_Socket.settimeout(5)  

#Initializing Sequence Number
sequence_number = -1

#data receving from client
while True: 

    timestamp, addr  = SERVER_Socket.recvfrom(1024) 
    sequence, addr  = SERVER_Socket.recvfrom(1024) 
    #Calculate time difference between sending and receiving packet
    time_stamp = pickle.loads (timestamp)
    timetaken = time.time() - time_stamp    
    if sequence_number == -1:
        print ("Listening the client", addr,)
        
    seq_no_client = pickle.loads (sequence)

    #Check if any packet is lost(Checks the difference for previous packet)
    if seq_no_client - sequence_number == 1:
        #Avoid displaying message if client has been restarted
        if seq_no_client > sequence_number:
            print ("\nPACKETS LOST : ", seq_no_client -1 -sequence_number)
    print ("\nSequence no. : %s time taken: %s" %(seq_no_client, timetaken))
    sequence_number=seq_no_client
