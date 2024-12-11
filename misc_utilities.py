import sys
from time import sleep

def cease():
    """this thing closes the game with a nice little message"""
    sys.exit("Closing game...")

def new_section():
    """this thing adds a blank line to aid in readability"""
    print("")

def dialogue(speaker,text):
    """someone besides player is speaking"""
    print(f"{speaker}: {text}")
    text_length = len(text)
    sleepy_length = text_length / 30
    sleep(sleepy_length)


def delay():
    """sleep for 1 second"""
    sleep(1)

def describe(description):
    """descriptions of place"""
    print(f"*{description}*")
    text_length = len(description)
    sleepy_length = text_length / 20
    sleep(sleepy_length)

def option_manager(option_list):
    i = 1
    for entry in option_list:
        print(str(i) + ".", entry)
        i += 1