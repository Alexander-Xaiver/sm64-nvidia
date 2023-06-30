# ASL64

This project adds motion control capabilities to Super Mario 64 by leveraging a detection dataset with python-based machine learning. It allows for simple functionality to move, jump, attack, crouch and navigate menus. 
![](direct image link here)

## How the project functions

This algorithm is an AI detection model that uses an ASL dataset. It takes the recognized ASL letters and ties them in to the Super Mario 64 game, which is locally emulated on an attached computer. The project functions as follows:

    1. An AI image detection model trained on an ASL dataset (which was found at this link: 
       https://public.roboflow.com/object-detection/american-sign-language-letters) is used to 
       take a live camera feed and output any ASL letters detected within. 
    2. Those outputs are sent from a client on the Jetson Nano to a server on the host computer. 
    3. Pydirectinput is used to take those AI outputs and turn them into inputs to be sent on the host computer.
    4. Project64 is used to emulate Super Mario 64. 
    5. Super Mario 64 is able to played using only ASL hand signs. 
   

## Getting the project running

The following is an inclusive list on getting the project running on a Jetson Nano using the jetson-inference repo: 

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
     6. Edit the models/python-detection.py to include the IP of the host computer.
     7. Connect the Jetson Nano to the host computer via hotspot.
     8. Run the python-detection.py script (you'll want to be in the docker container by running docker/run.sh)
     in the jetson-inference folder on the Jetson and the server.py script on the host.
     9. Focus the SM64 window and test the game using ASL controls.

A demonstration is available at the following link: https://youtu.be/5Te2JgiFlbs
Another video dives further into the system itself and how it manages to accomplish its task: https://youtu.be/uAghRpsAIko

## Difficulties and limitations

A difficulty that I was able to overcome was an issue regarding the structure of the dataset I downloaded. 
It was structured in a way that was incompatible with the provided training script. This
required me to write a script that allowed me to create a text file with every imageID.
The organized folder system is saved under data/asl_clean, and the script used is under data/organize.py.

The limitation of the project would primarily be inaccuracy regarding the ASL detection.
This could be solved using a larger dataset and more training cycles, both of which are 
important limitations but are solvable. Ultimately, this project serves as a proof of 
concept for controlling an N64 game with ASL inputs instead of traditional keystrokes
or controller inputs.


