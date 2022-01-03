'''
Dashbaord Controller Module
'''
from flask import current_app
from datetime import datetime, timedelta
from app.models.mongodb.usage_log import UsageLog



def get_usagelog(mongo_cur, user, year, month, day):
    '''
    특정 날짜 사용량 반환

    Params
    ---------
    mongo_cur > 몽고디비 커넥션 Object
    user > 사용자 객체
    year > 연
    month > 달
    day > 일
    '''
    usage_log_model = UsageLog(mongo_cur)
    find_object = {'user_id': user['user_id']}
    if year: find_object['year'] = year
    if month: find_object['month'] = month
    if day: find_object['day'] = day
    return usage_log_model.find_date(find_object)

def get_usagelog_year(mongo_cur, user, year):
    '''
    year ~ 현재 까지 사용량 반환 (연 기준)

    Params
    ---------
    mongo_cur > 몽고디비 커넥션 Object
    user > 사용자 객체
    year > 연
    '''
    usage_log_model = UsageLog(mongo_cur)
    total_usage = usage_log_model.find_year(user['user_id'], year)

    result = {}
    for usage in total_usage:
        year = str(usage['year'])
        if year not in result:
            result[year] = {}
        
        if not result[year]:
            result[year]['year_fee'] = 0
            for key, value in usage['usage'].items():
                result[year][key] = 0
        
        for key, value in usage['usage'].items():
            result[year][key] += value

        result[year]['year_fee'] += usage['fee']
    return result

        
def get_usagelog_month(mongo_cur, user, year, month):
    '''
    year/month ~ 현재 까지 사용량 반환 (달 기준)

    Params
    ---------
    mongo_cur > 몽고디비 커넥션 Object
    user > 사용자 객체
    year > 연
    month > 달
    '''
    usage_log_model = UsageLog(mongo_cur)
    total_usage = usage_log_model.find_month(user['user_id'], year, month)

    result = {}
    for usage in total_usage:
        year = str(usage['year'])
        month = str(usage['month'])
        if year not in result:
            result[year] = {}
        
        if not result[year]:
            result[year]['year_fee'] = 0
                
        if month not in result[year]:
            result[year][month] = {}

        if not result[year][month]:
            result[year][month]['month_fee'] = 0
            for key, value in usage['usage'].items():
                result[year][month][key] = 0

        for key, value in usage['usage'].items():
            result[year][month][key] += value

        result[year][month]['month_fee'] += usage['fee']
        result[year]['year_fee'] += usage['fee']
    return result
    
def get_usagelog_day(mongo_cur, user, year, month, day):
    '''
    year/month/day ~ 현재 까지 사용량 반환 (일 기준)

    Params
    ---------
    mongo_cur > 몽고디비 커넥션 Object
    user > 사용자 객체
    year > 연
    month > 달
    day > 일
    '''
    usage_log_model = UsageLog(mongo_cur)
    total_usage = usage_log_model.find_day(user['user_id'], year, month, day)

    result = {}
    for usage in total_usage:
        year = str(usage['year'])
        month = str(usage['month'])
        day = str(usage['day'])
        if year not in result:
            result[year] = {}
        
        if not result[year]:
            result[year]['year_fee'] = 0
                
        if month not in result[year]:
            result[year][month] = {}
            result[year][month]['month_fee'] = 0

        if day not in result[year][month]:
            result[year][month][day] = {}

        if not result[year][month][day]:
            result[year][month][day]['day_fee'] = 0
            for key, value in usage['usage'].items():
                result[year][month][day][key] = 0

        for key, value in usage['usage'].items():
            result[year][month][day][key] += value
        
        result[year][month][day]['day_fee'] += usage['fee']
        result[year][month]['month_fee'] += usage['fee']
        result[year]['year_fee'] += usage['fee']

    return result