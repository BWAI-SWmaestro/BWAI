'''
Log Controller Module
'''
from flask import current_app
from datetime import datetime
from app.models.mongodb.user import User
from app.models.mongodb.log import Log


def insert_log(mongo_cur, user, api, text, result):
    '''
    API 사용 로깅
    -> Bwai Main function 호출 로깅

    Params
    ---------
    mongo_cur > 몽고디비 커넥션
    user > 사용자 객체
    api > 요청 API
    text > 입력 문장
    result > 결과 값
    '''
    user_model = User(mongo_cur)
    log_model = Log(mongo_cur)

    today_usage = user['today_usage']
    today_usage[api] += 1

    log_object = {
        'user_id': user['user_id'],
        'api': api,
        'text': text,
        'result': result,
        'date': datetime.now()
    }

    user_model.update_one(user['user_id'], {'today_usage': today_usage})
    log_model.insert_one(log_object)

    return True