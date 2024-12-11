__author__ = "Phoenix Ecker"

import os
import chapters
from save_manager import write, create_save, read
from logger import log_entry, WLE
from misc_utilities import new_section, dialogue, delay

# start
log_entry("info","Initializing...")

# variable creation
save_file_path = 'save_the_world.xml'
guide_name = "???"

### remove this when you're done fucking around with the tuitorial
if os.path.exists(save_file_path):
    os.remove(save_file_path)

log_entry("info", "Welcome, new player (or deleter of save files)!")
create_save()
write('playerstate', 'newplayer', '1')
new_player = '1'


# check for save file

# if os.path.exists(save_file_path):
#     logEntry("info","Save file found! Welcome back.")
# else:
#     logEntry("info", "Welcome, new player (or deleter of save files)!")
#     createSave()
#     write('newplayer', '1')
#     newPlayer = '1'

# check if tuitorial started

tuitorial_started = read('worldinfo','tuitorialstarted')
checkpoint = read('worldinfo', 'tuitorialcheckpoint')

# login
delay()
new_section()
if new_player == '1':
    if tuitorial_started == '0':
        chapters.tu1()
    elif tuitorial_started == '1':
        if checkpoint == '1':
           chapters.tu1()
        elif checkpoint == '2':
            chapters.tu2()
        elif checkpoint == '3':
            chapters.tu3()
        elif checkpoint == '4':
            chapters.tu4()
        else:
            WLE("Variable 'checkpoint' is outside of 1-4 (bad)")
            

elif new_player == '0':
    dialogue(guide_name, "Ah, you're back.")
else:
    WLE("Variable 'new_player' is not 1 or 0 (it should be :/)")
    