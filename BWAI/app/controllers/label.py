'''
Label Controller Module
'''
from flask import current_app
from bson import ObjectId
from app.models.mongodb.post import Post


def get_posts_pagenation(mongo_cur, page, labeling_confirm, length):
    '''
    크롤링 데이터(Document) 불러오는 함수
    -> 페이지 네이션 기능

    Params
    ---------
    mongo_cur > 몽고디비 커넥션
    page > 페이지
    labeling_confirm > 라벨링 유/무
    '''
    post_model = Post(mongo_cur)
    posts = post_model.find_posts_pagenation_length(page, labeling_confirm, length)
    
    # Object _id to String convert
    for post in posts:
        post['_id'] = str(post['_id'])
        
    return posts

def set_label(mongo_cur, document_id, label):
    '''
    크롤링 데이터 라벨링 함수

    Params
    ---------
    mongo_cur > 몽고디비 커넥션
    label > 본문 라벨링
    '''
    post_model = Post(mongo_cur)
    post_model.update_label(ObjectId(document_id),
                            label,
                            1)
    return True

def get_label(mongo_cur):
    '''
    크롤링 데이터 라벨링 현황 반환 함수.

    Params
    ---------
    mongo_cur > 몽고디비 커넥션
    '''
    post_model = Post(mongo_cur)
    result = post_model.find_label_status(1)
    return result
