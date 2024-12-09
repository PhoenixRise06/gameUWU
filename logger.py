import logging

logging.basicConfig(filename='game.log', level='DEBUG', 
                    format='%(asctime)s - %(levelname)s - %(message)s')

def logEntry(type, msg):
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
