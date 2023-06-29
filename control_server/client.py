import socket

# NOTE: This file is a minimal demonstration of a UDP client sending a message.
# To get this working on the Jetson, you only need to change the Server IP address to reflect the appropriate IP for your network. 

# Setup: Create a UDP socket at client side
serverAddressPort   = ("127.0.0.1", 20001)
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Setup: Declare a helper function to simplify the "send message" call
def send_message(msg: str):
    UDPClientSocket.sendto(msg.encode(), serverAddressPort)

# Main: Write out a message, and send it to the server
msgFromClient = "Hello UDP Server"
send_message(msgFromClient)
