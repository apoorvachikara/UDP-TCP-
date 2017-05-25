import time
from socket import *

# variables initialized before use
time_count1 = 0
time_count2 = 0
ping_number = 1
packet_loss = 0
ELAPSED_SUM = 0

#Send ping 10 times 
while ( ping_number < 11 ):
    #Create a UDP socket
    clientSocket = socket(AF_INET, SOCK_DGRAM)
    clientSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    

    #Set a timeout value of 1 second
    clientSocket.settimeout(1)
    
    #Ping to server
    message = bytes("ping", 'utf-8')

    addr = ("127.0.0.1", 12000)
    #Send ping
    start = time.time()
    clientSocket.sendto(message, addr)

    #If data is received back from server, print , it will calculate elapsed time and avg elapsed time 
    try:
        data, server = clientSocket.recvfrom(1024)
        end = time.time()
        elapsed = end - start
        ELAPSED_SUM = elapsed + ELAPSED_SUM
        AVG_ELAPSED = ELAPSED_SUM/10

        #if loop is used to calculate the min and max time vaules
        if elapsed > time_count1:
            time_count1 = elapsed
        if elapsed > time_count1:
            time_count1 = elapsed
        if elapsed < time_count2:
             time_count2 = elapsed
        # printing data, ping_number and elapsed time
        print (data, ping_number, elapsed)

    #If data is not received from server, print it will print timeout 
    except timeout:
        print ("REQUEST TIMED OUT")
        packet_loss = packet_loss + 1
        

   
    ping_number = ping_number + 1
packet_loss = (packet_loss * 10)
# print min, max, avg and Packet loss as per requirement
print("RTT: Min: %sms Avg: %sms Max: %sms PacketLoss: %s " % (time_count2, AVG_ELAPSED,time_count1, packet_loss))
