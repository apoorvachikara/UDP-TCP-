import pickle
import time
from socket import *
from struct import *

print ("\n UDP Heartbeat Client ")
print ( "Sending heartbeat to server in every 3 seconds\n")

# Creating Socket and Sending data to Server
for ping in range(20):
    CLIENT_Socket = socket(AF_INET, SOCK_DGRAM)
    CLIENT_Socket.settimeout(3)
    addr = ('127.0.0.1', 12000)
    
    TIME = time.time()
    try:

        CLIENT_Socket.sendto(pickle.dumps(TIME),addr)
        CLIENT_Socket.sendto(pickle.dumps(ping), addr)
        
    except timeout:
        print("TIME OUT OCCURED")

    time.sleep(3)
