 
import logging

def setup_logger():
    logging.basicConfig(filename='app.log', level=logging.INFO,
                        format='%(asctime)s:%(levelname)s:%(message)s')

setup_logger()