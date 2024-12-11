import logging

logging.basicConfig(filename='game.log', level='DEBUG', 
                    format='%(asctime)s - %(levelname)s - %(message)s')

def log_entry(type, msg):
    """logging yippee"""
    if type == "critical":
        logging.critical(msg)
    elif type == "error":
        logging.error(msg)
    elif type == "warning":
        logging.warning(msg)
    elif type == "info":
        logging.info(msg)
    else:
        logging.debug(msg)
    
    print(msg)

def CDE(reasoning):
    """critical dumbass error"""
    log_entry("critical", "!!! Critical Dumbass Error: " + reasoning + "!")

def WLE(reasoning):
    """weird logic error"""
    log_entry("error", "!! Weird Logic Error: " + reasoning + "!")