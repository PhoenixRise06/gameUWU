from misc_utilities import dialogue, playerInput as PI
from save_manager import read, write

def tu():
    guideName = read("guidedata", "guidename")

    dialogue(guideName, "Shit, man, what are you doing here?")
    dialogue(guideName, "No wait don't answer that, I don't care.")
    dialogue(guideName, "Anyway, do you have a name?")

    playerName = input("Player: ")

    if playerName == "Phoenix":
        dialogue(guideName, "Ah, the creator. It is an honor.")
    else:
        dialogue(guideName, f"{playerName}, huh? Duly noted.")

    print(read("playerstate", "playername"))
    
    write('playerstate', 'playername', playerName)

    dialogue(guideName, "Given that the GUI has not been set up, the tuitorial is not going to involve much.")
    dialogue(guideName, "Most decisions are multiple-choice, answer those with the corresponding number.")
    dialogue(guideName, "Occasionally you will type things out instead. Be careful about the format.")
    dialogue(guideName, "I almost forgot, you can give me a name!")

    guideName = PI(" Your name is ")
    write('guidedata', 'guidename', guideName)
    
    if guideName == playerName:
        dialogue(guideName, "...that is going to make things quite confusing.")
    else:
        dialogue(guideName, f"Thank you! {guideName} is a wonderful name.")
    
    dialogue(guideName, "Now that we've got that out of the way, let's go to the village.")
