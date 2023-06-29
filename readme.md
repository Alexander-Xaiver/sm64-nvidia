# ASL64

This project adds motion control capabilities to Super Mario 64 by leveraging a detection dataset with python-based machine learning. It allows for simple functionality to move, jump, attack, crouch and navigate menus. 
![](direct image link here)

## The Algorithm

This algorithm is an AI detection model that uses an ASL dataset. It takes the recognized ASL letters and ties them in to the Super Mario 64 game, which is locally emulated on an attached computer. The project functions as follows:

    1. An AI image detection model trained on an ASL dataset (which was found at this link: 
       https://public.roboflow.com/object-detection/american-sign-language-letters) is used to 
       take a live camera feed and output any ASL letters detected within. 
    2. Those outputs are sent from a client on the Jetson Nano to a server on the host computer. 
    3. Pydirectinput is used to take those AI outputs and turn them into inputs to be sent on the host computer.
    4. Project64 is used to emulate Super Mario 64. 
    5. Super Mario 64 is able to played using only ASL hand signs. 
   

## Running this project

1. Check requirements:
   * This project requires pydirectinput, along with a jetson-inference repo install.
   * An emulation environment for SM64.
 2. Clone the Github repository for the project in an environment containing a jetson-inference install.
 3. Download the control_server file to the host computer from the Github repository.
 4. Lauch Project64 (or any N64 emulator) and bind the following buttons to the following commands:
    * Analog stick up = arrow key up (this is used to move forward using ASL sign N.
    * Analog stick right = arrow key right (this is used to move right using ASL sign Q.)
    * Analog stick left = arrow key left (this is used to move left using ASL sign L.)
    * B = B (this is used to attack and interact ingame using ASL sign B.)
    * A = A (this is used to jump using ASL sign A.)
    * Start = Y (this is used for entering the game and pausing using ASL sign Y.)
    * Z trigger = C (this is used to crouch using ASL sign Z.)
 5. Open up a SM64 rom in the emulator.
 6. Run the python-detection.py script on the Jetson and the server.py script on the host.
 7. Focus the SM64 window and test the game using ASL controls. 

[View a video explanation here](video link)
