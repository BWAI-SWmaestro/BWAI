import random
from tqdm import tqdm
from datetime import datetime, timedelta


def update_user_dashboard(db, config):
    fee = db['master_config'].find_one({'key': 'fee'})['value']
    today = datetime.now()
    yesterday = today - timedelta(1)

    today_int = int(today.strftime('%Y%m%d'))
    yesterday_int = int(yesterday.strftime('%Y%m%d'))
    
    users = list(db['user'].find({'subscribe_at': {'$gte': today_int}}))

    year = yesterday.year
    month = yesterday.month
    day = yesterday.day

    for user in tqdm(users):
        today_usage = user['today_usage']
        
        # 사용자 당일 API 사용량 초기화
        db['user'].update_one({'user_id': user['user_id']},
                              {'$set': {'today_usage': {'probability': 0, 'judge': 0, 'masking': 0}}})

        # 당일 요금 계산
        today_fee = 0
        for key, value in today_usage.items():
            today_fee += value * fee[key]

        log_object = {'user_id': user['user_id'],
                      'year': year,
                      'month': month,
                      'day': day,
                      'date': yesterday_int,
                      'usage': today_usage,
                      'fee': today_fee}

        db['usage_log'].insert_one(log_object)

    return len(users)


def dummy_input_dashboard(db, config):
    fee = db['master_config'].find_one({'key': 'fee'})['value']

    for year in tqdm(range(2018, 2021)):
        for month in range(1, 13):
            for day in range(1, 32):
                today_usage = {
                    'probability': random.randrange(100, 500),
                    'judge': random.randrange(100, 500),
                    'masking': random.randrange(100, 500)
                }
                # 당일 요금 계산
                today_fee = 0
                for key, value in today_usage.items():
                    today_fee += value * fee[key]
                date = str(year)
                if month < 10:
                    date += '0' + str(month)
                else:
                    date += str(month)
                if day < 10:
                    date += '0' + str(day)
                else:
                    date += str(day)
                
                log_object = {'user_id': "BWAI",
                              'year': year,
                              'month': month,
                              'day': day,
                              'date': int(date),
                              'usage': today_usage,
                              'fee': today_fee}

                db['usage_log'].insert_one(log_object)

    return True