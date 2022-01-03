'''
MongoDB user Collection Model
'''
from flask import current_app
from bson.objectid import ObjectId


class User:
    """BWAI DB user Model"""
    def __init__(self, client):
        self.col = client[current_app.config['MONGODB_DB_NAME']]['user']

    def insert_one(self, user_obj):
        ''' 유저 추가 '''
        self.col.insert_one(user_obj)
        return True

    def find_one(self, user_id, projection=None):
        ''' 특정 유저 반환 '''
        return self.col.find_one(
            {"user_id": user_id},
            projection
        )

    def find_many(self, projection=None):
        ''' 모든 유저 반환 '''
        return list(self.col.find(
            {},
            projection
        ))
    
    def find_api_token_key(self, api_token_key):
        ''' 해당 api token key를 가지고 있는 회원 반환'''
        return self.col.find_one(
            {'api_token_key': api_token_key}
        )
    
    def update_one(self, user_id, update_object):
        ''' 회원 정보 수정 '''
        self.col.update_one(
            {"user_id": user_id},
            {"$set": update_object}
        )
        return True
