from misc_utilities import dialogue, delay, describe, new_section, option_manager
from save_manager import read, write
import logger

def tu1():
    """tuitorial pt 1"""
    write('worldinfo', 'tuitorialstarted', '1')
    write('worldinfo', 'tuitorialcheckpoint', '1')
    guide_name = read("guidedata", "guide_name")

    dialogue(guide_name, "Shit, man, what are you doing here?")
    dialogue(guide_name, "No wait don't answer that, I don't care.")
    dialogue(guide_name, "Anyway, do you have a name?")

    player_name = input("Player: ")

    if player_name == "Phoenix":
        dialogue(guide_name, "Ah, the creator. It is an honor.")
    else:
        dialogue(guide_name, f"{player_name}, huh? Duly noted.")
    
    write('playerstate', 'player_name', player_name)
    
    tu2()

def tu2():
    """tuitorial pt 2"""
    write('worldinfo', 'tuitorialcheckpoint', '2')

    player_name = read('playerstate', 'player_name')
    guide_name = read("guidedata", "guide_name")

    dialogue(guide_name, "Given that the GUI has not been set up, the tuitorial is not going to involve much.")
    dialogue(guide_name, "Most decisions are multiple-choice, answer those with the corresponding number.")
    dialogue(guide_name, "Occasionally you will type things out instead. Be careful about the format.")
    dialogue(guide_name, "I almost forgot, you can give me a name!")

    guide_name = input(f"{player_name}: Your name is ")
    write('guidedata', 'guide_name', guide_name)
    
    if guide_name == player_name:
        dialogue(guide_name, "...that is going to make things quite confusing.")
    else:
        dialogue(guide_name, f"Thank you! {guide_name} is a wonderful name.")
    
    tu3()

def tu3():
    """tuitorial pt 3"""
    write('worldinfo', 'tuitorialcheckpoint', '3')

    guide_name = read("guidedata", "guide_name")
    player_name = read('playerstate', 'player_name')

    dialogue(guide_name, "Now that we've got that out of the way, let's go to the village.")

    ans = None

    while 1 + 1 == 2:
        option_manager(["I can't wait!", "The village...?"])
        ans = input(f"{player_name}: ")

        if ans == "1":
            dialogue(guide_name, "Haha, I haven't even told you about it yet! It is really cool though.")
            break
        elif ans == "2":
            dialogue(guide_name, "It's just a place where several people I know live. You'll love it there.")
            break
        else:
            logger.CDE("You need to choose one of the options given!")
            delay()
    
    new_section()
    describe("[enter the village description here]")
    dialogue(guide_name, "There's a few places we could go first.")
    tu4()

def tu4():
    """tuitorial pt 4"""
    write('worldinfo', 'tuitorialcheckpoint', '4')

    guide_name = read("guidedata", "guide_name")
    player_name = read('playerstate', 'player_name')

    

    

