'''
BWAI View Module
'''
from flask import g, request, Blueprint
from app.api import input_check
from app.api.bwai_v1 import bwai_v1 as api
from app.api.decorators import timer, api_required
from app.controllers.bwai import bwai_judge, bwai_probability, bwai_masking
from app.controllers.log import insert_log


@api.route("/probability", methods=['POST'])
@timer
@api_required
def api_get_probability():
    ''' BWAI Func 1 (욕설 확률 반환) '''
    data = request.get_json()
    input_check(data, "text", str)
    result = bwai_probability(data['text'])
    insert_log(g.mongo_cur,
               g.user,
               "probability",
               data['text'],
               result)
    return {
        "msg": "success",
        "result": result
    }


@api.route("/judge", methods=['POST'])
@timer
@api_required
def api_get_judge():
    ''' BWAI Func 2 (욕설 판단 반환) '''
    data = request.get_json()
    input_check(data, "text", str)
    result = bwai_judge(data['text'])
    insert_log(g.mongo_cur,
               g.user,
               "judge",
               data['text'],
               result)
    return {
        "msg": "success",
        "result": result
    }


@api.route("/masking", methods=['POST'])
@timer
@api_required
def api_get_masking():
    ''' BWAI Func 3 (욕설 마스킹 반환) '''
    data = request.get_json()
    input_check(data, "text", str)
    result = bwai_masking(data['text'])
    insert_log(g.mongo_cur,
               g.user,
               "masking",
               data['text'],
               result)
    return {
        "msg": "success",
        "result": result
    }


#=======================================================================


@api.route("/probability/demo", methods=['POST'])
@timer
def api_get_probability_demo():
    ''' BWAI Func 1 (욕설 확률 반환) '''
    data = request.get_json()
    input_check(data, "text", str)
    result = bwai_probability(data['text'])
    return {
        "msg": "success",
        "result": result
    }


@api.route("/judge/demo", methods=['POST'])
@timer
def api_get_judge_demo():
    ''' BWAI Func 2 (욕설 판단 반환) '''
    data = request.get_json()
    input_check(data, "text", str)
    result = bwai_judge(data['text'])
    return {
        "msg": "success",
        "result": result
    }


@api.route("/masking/demo", methods=['POST'])
@timer
def api_get_masking_demo():
    ''' BWAI Func 3 (욕설 마스킹 반환) '''
    data = request.get_json()
    input_check(data, "text", str)
    result = bwai_masking(data['text'])
    return {
        "msg": "success",
        "result": result
    }