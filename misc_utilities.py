import sys
from time import sleep
from save_manager import read

def cease():
    sys.exit("Stopping script")

def newSection():
    print("")

def dialogue(speaker,text):
    delay()
    print(f"{speaker}: {text}")

def delay():
    sleep(1)

def playerInput(leadUp):
    speaker = read('playerstate', 'playername')
    input(f"{speaker}:{leadUp}")

def describe(description):
    descriptionLength = len(description)
    sleepyLength = descriptionLength / 20
    sleep(sleepyLength)
    print(f"*{description}*")