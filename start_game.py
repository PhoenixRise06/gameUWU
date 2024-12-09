__author__ = "Phoenix Ecker"

import os
from chapters import tu
from save_manager import write, createSave
from logger import logEntry
from misc_utilities import newSection, dialogue, delay

# start
logEntry("info","Initializing...")

# variable creation
saveFilePath = 'save_the_world.xml'
guideName = "???"

### remove this when you're done fucking around with the tuitorial
if os.path.exists(saveFilePath):
    os.remove(saveFilePath)

logEntry("info", "Welcome, new player (or deleter of save files)!")
createSave()
write('playerstate', 'newplayer', '1')
newPlayer = '1'

# check for save file, 
# if os.path.exists(saveFilePath):
#     logEntry("info","Save file found! Welcome back.")
#     write('newplayer', '0')
#     newPlayer = '0'
# else:
#     logEntry("info", "Welcome, new player (or deleter of save files)!")
#     createSave()
#     write('newplayer', '1')
#     newPlayer = '1'

# login
delay()
newSection()
if newPlayer == '1':
    tu()
elif newPlayer == '0':
    dialogue(guideName, "Ah, you're back.")
else:
    logEntry("critical","!!! Critical Logic Error: variable 'newPlayer' is not 1 or 0! (It should be :/)")
    