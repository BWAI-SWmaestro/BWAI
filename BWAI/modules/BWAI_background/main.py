'''
BWAI Background process
'''
import sys
from pymongo import MongoClient
from modules.BWAI_background.src.dashboard import update_user_dashboard, dummy_input_dashboard


def process_background(config=None):
    '''
    Update User dashboard.
    '''
    cur = MongoClient(config.MONGODB_URI)
    db = cur[config.MONGODB_DB_NAME]

    update_user_dashboard(db, config)
    
    cur.close()
    sys.stdout.write("Update User dashboard. ... OK\n")

def process_dummy_logging(config=None):
    '''
    Insert Dummy log data.
    '''
    cur = MongoClient(config.MONGODB_URI)
    db = cur[config.MONGODB_DB_NAME]

    dummy_input_dashboard(db, config)
    
    cur.close()
    sys.stdout.write("Insert Dummy log data. ... OK\n")