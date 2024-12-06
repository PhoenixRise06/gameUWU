import start_game, logging

logger = logging.getLogger('')

if start_game.newPlayer == True:
    print("Shit man, what are you doing here?")
elif start_game.newPlayer == False:
    print("Ah, you're back.")
else:
    logging.error('')