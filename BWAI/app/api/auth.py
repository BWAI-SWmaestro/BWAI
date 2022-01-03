'''
Auth View Module
'''
from flask import g, request, Blueprint
from app.api import input_check
from app.api.decorators import timer, login_required
from app.controllers.auth import (signup,
                                  signin,
                                  get_userinfo,
                                  get_api_token)


auth = Blueprint('auth', __name__)


@auth.route("/signup", methods=['POST'])
@timer
def api_auth_signup():
    ''' 회원 가입 '''
    data = request.get_json()
    input_check(data, "id", str)
    input_check(data, "pw", str)
    return {
        "msg": "success",
        "result": signup(g.mongo_cur,
                         data['id'],
                         data['pw'])
    }


@auth.route("/signin", methods=['POST'])
@timer
def api_auth_signin():
    ''' 로그인 '''
    data = request.get_json()
    input_check(data, "id", str)
    input_check(data, "pw", str)
    return {
        "msg": "success",
        "result": signin(g.mongo_cur,
                         data['id'],
                         data['pw'])
    }


@auth.route("/info", methods=["GET"])
@timer
@login_required
def api_auth_info():
    ''' 회원 정보 반환 '''
    return {
        "msg": "success",
        "result": get_userinfo(g.user)
    }


@auth.route("/api_token", methods=["GET"])
@timer
@login_required
def api_auth_get_api_token():
    ''' API Token 발행 / 갱신 '''
    return {
        "msg": "success",
        "result": get_api_token(g.mongo_cur,
                                g.user)
    }