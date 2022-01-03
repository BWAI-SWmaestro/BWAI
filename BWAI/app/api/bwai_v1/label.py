'''
Label View Module
'''
from flask import g, request, Blueprint
from app.api import input_check
from app.api.bwai_v1 import bwai_v1 as api
from app.api.decorators import timer
from app.controllers.label import (get_posts_pagenation,
                                   set_label,
                                   get_label)


@api.route("/posts/<int:page>/<int:labeling_confirm>/<int:length>", methods=['GET'])
@timer
def api_get_posts(page, labeling_confirm, length=30):
    ''' 크롤링 포스트 반환 '''
    return {
        "msg": "success",
        "result": get_posts_pagenation(g.mongo_cur,
                                       page,
                                       labeling_confirm,
                                       length)
    }


@api.route("/label", methods=['PATCH'])
@timer
def api_patch_label():
    ''' 라벨링 '''
    data = request.get_json()
    input_check(data, "document_id", str)
    input_check(data, "label", int)
    return {
        "msg": "success",
        "result": set_label(g.mongo_cur,
                            data['document_id'],
                            data['label'])
    }


@api.route("/label", methods=["GET"])
@timer
def api_get_label():
    ''' 라벨링 현황 반환 '''
    return {
        "msg": "success",
        "result": get_label(g.mongo_cur)
    }
