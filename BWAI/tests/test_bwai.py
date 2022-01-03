'''
Bwai API 관련 테스트 케이스
'''
import unittest
from json import loads
from flask import current_app
from app import create_app
from flask_jwt_extended import create_access_token


class BwaiAPITestCase(unittest.TestCase):
    ''' Bwai 테스트 케이스 클래스 '''
    def setUp(self):
        '''전처리 메소드'''
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client()
        self.access_token = create_access_token(
            identity=self.app.config['ADMIN_ID'],
            expires_delta=False
        )

    def tearDown(self):
        ''' 후처리 메소드 '''
        self.app_context.pop()

    def get_headers(self):
        '''API Header 생성 메소드'''
        result = {
            'Accept': 'application/json',
            'Authorization': "Bearer " + self.access_token,
            #'Content-Type': 'application/json',
        }
        return result

    def test_probability(self):
        ''' BWAI probability API 검증 테스트 '''

        resp = self.client.get(
            '/api/auth/api_token',
            headers=self.get_headers(),
            json={}
        )
        self.assertEqual(resp.status_code, 200)
        api_token = loads(resp.data)['result']['api_token']

        token_result = {
            'Accept': 'application/json',
            'Authorization': "Bearer " + api_token,
        }

        resp = self.client.post(
            '/api/bwai/v1/probability',
            headers=token_result,
            json={
                "text": "욕설 테스트 문장"
            }
        )
        self.assertEqual(resp.status_code, 200)

    def test_judge(self):
        ''' BWAI judge API 검증 테스트 '''

        resp = self.client.get(
            '/api/auth/api_token',
            headers=self.get_headers(),
            json={}
        )
        self.assertEqual(resp.status_code, 200)
        api_token = loads(resp.data)['result']['api_token']

        token_result = {
            'Accept': 'application/json',
            'Authorization': "Bearer " + api_token,
        }

        resp = self.client.post(
            '/api/bwai/v1/judge',
            headers=token_result,
            json={
                "text": "욕설 테스트 문장"
            }
        )
        self.assertEqual(resp.status_code, 200)
    
    def test_masking(self):
        ''' BWAI masking API 검증 테스트 '''

        resp = self.client.get(
            '/api/auth/api_token',
            headers=self.get_headers(),
            json={}
        )
        self.assertEqual(resp.status_code, 200)
        api_token = loads(resp.data)['result']['api_token']

        token_result = {
            'Accept': 'application/json',
            'Authorization': "Bearer " + api_token,
        }

        resp = self.client.post(
            '/api/bwai/v1/masking',
            headers=token_result,
            json={
                "text": "욕설 테스트 문장"
            }
        )
        self.assertEqual(resp.status_code, 200)
