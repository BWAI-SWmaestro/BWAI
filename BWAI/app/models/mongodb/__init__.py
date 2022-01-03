'''
MongoDB Management Modules and Models
'''
from datetime import datetime
from pymongo import MongoClient
from flask import g, current_app
from werkzeug.security import generate_password_hash
from app.controllers.auth import signup


def get_mongo_cur():
    ''' return mongodb cursor'''
    return MongoClient(current_app.config['MONGODB_URI'])


def open_mongo_cur():
    ''' store mongodb cursor in the g'''
    g.mongo_cur = MongoClient(current_app.config['MONGODB_URI'])


def close_mongo_cur():
    ''' pop & close mongodb cursor in the g'''
    mongo_cur = g.pop('mongo_cur', None)
    if mongo_cur:
        mongo_cur.close()


def init_models(config):
    '''mongodb-init function'''
    cur = MongoClient(config.MONGODB_URI)
    db_name = config.MONGODB_DB_NAME

    # Create admin account
    signup(cur,
           config.ADMIN_ID,
           config.ADMIN_PW)

    # Set fee
    col = cur[config.MONGODB_DB_NAME]['master_config']
    col.update_one(
        {"key": "fee"},
        {
            "$set":{
                "value": {'probability': 1, 'judge': 1, 'masking': 1}
            }
        },
        upsert=True)
    
    cur.close()
