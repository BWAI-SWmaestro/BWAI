'''
BWAI Application Config Setting
'''
import os
import sys
from datetime import datetime
from logging.config import dictConfig

BASEDIR = os.path.abspath(os.path.dirname(__file__))


class Config:
    '''공통 Config'''
    # Authorization
    SECRET_KEY = os.environ['BWAI_SECRET_KEY']
    ADMIN_ID = os.environ['BWAI_ADMIN_ID']
    ADMIN_PW = os.environ['BWAI_ADMIN_PW']

    # Database
    MONGODB_URI = os.environ['BWAI_MONGODB_URI']
    MONGODB_DB_NAME = 'BWAI'

    # Maximum API time
    SLOW_API_TIME = 0.5

    # BWAI bad word set
    BWAI_BAD_WORDS = ['^^ㅣ', 'ㅂㅅ', 'D쥐고', 'D지고', 'tlqkf', 'wlfkf', '관.종', '관종', '기레기', '김치녀', '껒여', '나빼썅', '노무노무', '노알라', '늬믜', '니애미', '니애비', '닥2', '도라이', '뒈져', '뒤졌', '뒤지겠', '디졌', '또라인', '똘아이', '럼들', '맘충', '버짓물', '보즤', '보지걸', '보지털', '보짓물', '보짖물', '뵤즤', '붕딱', '붕딲', '붕뛴', '뷍슨', '븽딱', '븽쉬', '븽시', '빙신', '빠걸', '빠굴', '빠큐', '빡큐', '빨어핥어박어', '뺑신', '뺑쒼', '뺑씬', '뺘큐', '뻐규', '뻐큐', '뻐킹', '뻑유', '뻑큐', '뼈큐', '뽀쥐', '뽀지', '뽀쮜', '뽄새', '뽄세', '뿅씬', '뿡알', '삐걱', '삐꾸', '삥쒼', '삽쥘', '삿깟시', '쉑캬', '시방새', '시부렬', '시부울', '시키가', '싸가지', '싸물어', '싸줄께', '쌉', '쌍념', '쌍뇽', '쌍연', '쌕', '쌕갸', '쌕걸', '씨벧', '씨부렬', '씻끼', '씻뻘', '씻퐁', '엄창', '에믜', '엠생', '엿먹', '젼낰', '졀라', '졀리', '조녜', '조온', '조카툰', '존낙', '존싫', '존쎼', '좀물', '죵나', '쥰니', '폰색', '폰세엑', '폰섹', '폰쉑', '폰쌕', '폰쎅', 'ㄱㅐ새끼', '새꺄', '^ㅣ발', '빡대가리', '엠창', '느금마', 'ㄴㄱㅁ', '느금', '니앰', '니엠']

    @staticmethod
    def init_app(app):
        '''전역 init_app 함수'''


class TestingConfig(Config):
    '''Test 전용 Config'''
    DEBUG = True
    TESTING = True


class DevelopmentConfig(Config):
    '''개발 환경 전용 Config'''
    DEBUG = True
    TESTING = False


class ProductionConfig(Config):
    ''' 상용환경 전용 Config'''
    DEBUG = False
    TESTING = False

    @staticmethod
    def init_app(app):
        '''로거 등록 및 설정'''
        dictConfig({
            'version': 1,
            'formatters': {
                'default': {
                    'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
                }
            },
            'handlers': {
                'file': {
                    'level': 'WARNING',
                    'class': 'logging.handlers.RotatingFileHandler',
                    'filename': os.getenv('RAAS_ERROR_LOG_PATH') or './server.error.log',
                    'maxBytes': 1024 * 1024 * 5,
                    'backupCount': 5,
                    'formatter': 'default',
                },
            },
            'root': {
                'level': 'WARNING',
                'handlers': ['file']
            }
        })


config = {
    'development':DevelopmentConfig,
    'production':ProductionConfig,
    'testing':TestingConfig,
    'default':DevelopmentConfig,
}
