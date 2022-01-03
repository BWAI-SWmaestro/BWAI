'''
MongoDB log Collection Model
'''
from flask import current_app
from bson.objectid import ObjectId


class Log:
    """BWAI DB LogToday Model"""
    def __init__(self, client):
        self.col = client[current_app.config['MONGODB_DB_NAME']]['log']

    def insert_one(self, document):
        ''' Insert Document '''
        self.col.insert_one(document)
        return True