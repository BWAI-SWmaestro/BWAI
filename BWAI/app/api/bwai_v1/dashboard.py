'''
Dashboard View Module
'''
from flask import g, request, Blueprint
from app.api.bwai_v1 import bwai_v1 as api
from app.api.decorators import timer, login_required
from app.controllers.dashboard import (get_usagelog,
                                       get_usagelog_year,
                                       get_usagelog_month,
                                       get_usagelog_day)


@api.route("/dashboard/<int:year>", methods=['GET'])
@api.route("/dashboard/<int:year>/<int:month>", methods=['GET'])
@api.route("/dashboard/<int:year>/<int:month>/<int:day>", methods=['GET'])
@timer
@login_required
def api_dashboard(year=None, month=None, day=None):
    ''' 특정 날짜 사용량 반환 '''
    return {
        "msg": "success",
        "result": get_usagelog(g.mongo_cur,
                               g.user,
                               year,
                               month,
                               day)
    }


@api.route("/dashboard/year/<int:year>", methods=['GET'])
@timer
@login_required
def api_dashboard_year(year=None):
    ''' year ~ 현재 까지 사용량 반환 (연 기준) '''
    return {
        "msg": "success",
        "result": get_usagelog_year(g.mongo_cur,
                                    g.user,
                                    year)
    }


@api.route("/dashboard/year/<int:year>/month/<int:month>", methods=['GET'])
@timer
@login_required
def api_dashboard_month(year=None, month=None):
    ''' year/month ~ 현재 까지 사용량 반환 (달 기준) '''
    return {
        "msg": "success",
        "result": get_usagelog_month(g.mongo_cur,
                                     g.user,
                                     year,
                                     month)
    }


@api.route("/dashboard/year/<int:year>/month/<int:month>/day/<int:day>", methods=['GET'])
@timer
@login_required
def api_dashboard_day(year=None, month=None, day=None):
    ''' year/month/day ~ 현재 까지 사용량 반환 (일 기준) '''
    return {
        "msg": "success",
        "result": get_usagelog_day(g.mongo_cur,
                                   g.user,
                                   year,
                                   month,
                                   day)
    }