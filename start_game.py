__author__ = "Phoenix"

import os
import logging

saveFilePath = 'save_the_world.txt'

logging.basicConfig(filename='game.log', level=logging.debug, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

if os.path.exists(saveFilePath):
    with open(saveFilePath, 'r') as f:
        contents = f.read()
    print("\nSave file found! Welcome back.")
    newPlayer = False
else:
    with open(saveFilePath, 'x') as f:
        f.write("you cuck")
    print("\nWelcome, new player (or deleter of save files)!")
    newPlayer = True


os.system('login.py')