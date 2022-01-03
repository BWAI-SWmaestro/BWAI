'''
MongoDB post Collection Model
'''
from flask import current_app
from bson.objectid import ObjectId


class Post:
    """BWAI DB post Model"""
    def __init__(self, client):
        self.col = client[current_app.config['MONGODB_DB_NAME']]['posts_labeled_v3']

    def find_posts_pagenation_length(self, page, labeling_confirm, length):
        ''' 특정 string 길이 Document 가져오기 (페이지네이션) '''
        return list(self.col.find(
            {
                '$and':
                [
                    {'labeling_confirm': labeling_confirm},
                    {'length': {'$lte': length}}
                ]
            }
        ).skip((page-1)*10).limit(10))

    def find_label_status(self, labeling_confirm):
        ''' 라벨링 현황(개수) '''
        return self.col.find(
            {'labeling_confirm': labeling_confirm}
        ).count()

    def update_label(self, _id, label, labeling_confirm):
        ''' 라벨링 상태 업데이트 '''
        self.col.update_one(
            {'_id': _id},
            {
                '$set':
                {
                    'label': label,
                    'labeling_confirm': labeling_confirm
                }
            }
        )
        return True
