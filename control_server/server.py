import socket
import pydirectinput
import time


# TODO: look into 'pyautogui' to programmatically press keys
# just be careful that you can safely turn it off while it's controlling your keyboard!

localIP     = "" # NOTE: empty string means "accept traffic from anywhere; localhost, LAN, or the wider internet". it's weird. lmk Thursday evening if you want to know a bit more
localPort   = 20001
bufferSize  = 1024

# Create a datagram (UDP) socket
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
# Bind to address and ip
UDPServerSocket.bind((localIP, localPort))
print("UDP server up and listening")

pydirectinput.FAILSAFE = True
pydirectinput.PAUSE=0.0

# Listen for incoming datagrams
while(True):
    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
    message = bytesAddressPair[0].decode()
    # address = bytesAddressPair[1] # we don't care about the address
    
    print(f"Message from client: {message}")
    
    if "N" in message:
        pydirectinput.keyDown("up")
        time.sleep(0.1)
        pydirectinput.keyUp("up")
    if "Q" in message:
        pydirectinput.keyDown("right")
        time.sleep(0.1)
        pydirectinput.keyUp("right")
    if "L" in message:
        pydirectinput.keyDown("left")
        time.sleep(0.1)
        pydirectinput.keyUp("left")
    if "C" in message:
        pydirectinput.keyDown("c")
        time.sleep(0.1)
        pydirectinput.keyUp("c")
    if "A" in message:
        pydirectinput.keyDown("a")
        time.sleep(0.1)
        pydirectinput.keyUp("a")
    if "B" in message:
        pydirectinput.keyDown("b")
        time.sleep(0.1)
        pydirectinput.keyUp("b")
    if "Y" in message:
        pydirectinput.keyDown("y")
        time.sleep(0.1)
        pydirectinput.keyUp("y")
            
    # TODO: look through the message for any keys we care about, and press certain buttons on the keyboard
