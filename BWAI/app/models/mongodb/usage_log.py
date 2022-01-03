'''
MongoDB usage_log Collection Model
'''
from flask import current_app
from bson.objectid import ObjectId


class UsageLog:
    """BWAI DB LogToday Model"""
    def __init__(self, client):
        self.col = client[current_app.config['MONGODB_DB_NAME']]['usage_log']

    def insert_one(self, document):
        ''' Insert Document '''
        self.col.insert_one(document)
        return True
    
    def find_date(self, find_object):
        ''' 특정 날짜 반환 '''
        return list(self.col.find(
            find_object,
            {'_id': 0, 'date': 1, 'usage': 1, 'fee': 1}
        ))

    def find_year(self, user_id, year):
        ''' year ~ 지금 반환 '''
        return list(self.col.find(
            {
                '$and':
                [
                    {'user_id': user_id},
                    {'year': {'$gte': year}}
                ]
            }
        ))
    
    def find_month(self, user_id, year, month):
        ''' month ~ 지금 반환 '''
        return list(self.col.find(
            {
                '$and':
                [
                    {'user_id': user_id},
                    {'year': {'$gte': year}},
                    {'month': {'$gte': month}},
                ]
            }
        ))
    
    def find_day(self, user_id, year, month, day):
        ''' day ~ 지금 반환 '''
        return list(self.col.find(
            {
                '$and':
                [
                    {'user_id': user_id},
                    {'year': {'$gte': year}},
                    {'month': {'$gte': month}},
                    {'day': {'$gte': day}}
                ]
            }
        ))