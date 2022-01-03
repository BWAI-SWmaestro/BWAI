'''
Auth Controller Module
'''
from flask import current_app
from datetime import datetime, timedelta
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token
from app.models.mongodb.user import User


def signup(mongo_cur, user_id, user_pw):
    '''
    회원 가입

    Params
    ---------
    mongo_cur > 몽고디비 커넥션 Object
    user_id > 아이디
    user_pw > 비밀번호
    '''
    user_model = User(mongo_cur)
    if user_model.find_one(user_id):
        return False
    user_model.insert_one(
        {'user_id': user_id,
         'user_pw': generate_password_hash(user_pw),
         'today_usage': {'probability': 0, 'judge': 0, 'masking': 0},
         'subscribe_at': None,
         'created_at': datetime.now(),
         'api_token_time': None,
         'api_token_key': None})
    return {'user_token' :create_access_token(identity=user_id, expires_delta=False)}

def signin(mongo_cur, user_id, user_pw):
    '''
    로그인

    Params
    ---------
    mongo_cur > 몽고디비 커넥션 Object
    user_id > 아이디
    user_pw > 비밀번호
    '''
    user_model = User(mongo_cur)
    user = user_model.find_one(user_id)
    if not user:
        return False
    if check_password_hash(user['user_pw'], user_pw):
        return {'user_token': create_access_token(identity=user_id, expires_delta=False)}
    else:
        return False

def get_userinfo(user):
    '''
    사용자 정보 반환 (필요 없는 필드 제거)

    Params
    ---------
    mongo_cur > 몽고디비 커넥션 Object
    user > 사용자 정보
    '''
    result = {
        'user_id': user['user_id'],
        'created_at': user['created_at'],
        'subscribe_at': user['subscribe_at'],
        'today_usage': user['today_usage']
    }
    return result

def get_api_token(mongo_cur, user):
    '''
    API_Token 생성 / 갱신

    Params
    ---------
    user > 사용자 객체
    '''
    user_model = User(mongo_cur)
    
    api_token_time = datetime.now()
    api_token_key = user['user_id'] + str(api_token_time)
    api_token = create_access_token(identity=api_token_key, expires_delta=False)

    user_model.update_one(user['user_id'], {'api_token_time': api_token_time, 'api_token_key': api_token_key})
    
    return {'api_token': api_token}

def check_api_token(mongo_cur, api_token_key):
    '''
    API_Token 체크

    Params
    ---------
    mongo_cur > 몽고디비 커넥션 Object
    user_id > 아이디
    '''
    user_model = User(mongo_cur)
    user = user_model.find_api_token_key(api_token_key)
    if not user:
        return False
    
    check_time = datetime.now() + timedelta(hours=1)
    if check_time < user['api_token_time']:
        return False
    
    api_token_time = datetime.now()
    user_model.update_one(user['user_id'], {'api_token_time': api_token_time})
    
    return user