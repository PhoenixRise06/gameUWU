__author__ = "Phoenix Ecker"

import os, logging
from utils.save_manager import read, write, dupe

saveFilePath = 'save_the_world.xml'

logging.basicConfig(filename='game.log', level='DEBUG', 
                    format='%(asctime)s - %(levelname)s - %(message)s')

if os.path.exists(saveFilePath):
    print("Save file found! Welcome back.")
    newPlayer = 0
    write(newPlayer, 0)
else:
    print("Welcome, new player (or deleter of save files)!")
    newPlayer = 1
    dupe()
    write(newPlayer, 1)

def login(newPlayer):
    if newPlayer == 1:
        print("Shit, man, what are you doing here?")
    elif newPlayer == 0:
        print("Ah, you're back.")
    else:
        logging.critical("!!! Critical Logic Error: variable 'newPlayer' is not a boolean!")
        