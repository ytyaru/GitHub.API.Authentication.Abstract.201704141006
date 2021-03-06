#!python3
#encoding:utf-8
import unittest
from authentication.OAuthTokenFromDatabaseAuthentication import OAuthTokenFromDatabaseAuthentication
from Database import Database
class test_OAuthTokenFromDatabaseAuthentication(unittest.TestCase):
    def test_GetRequestParameters(self):
        db = Database()
        db.Initialize()
        username = 'user0'
        auth = OAuthTokenFromDatabaseAuthentication(db, username)
        params = auth.GetRequestParameters()
        print(params)
        self.assertTrue('headers' in params)
        self.assertTrue('Time-Zone' in params['headers'])
        self.assertTrue('Accept' in params['headers'])
        self.assertTrue('Authorization' in params['headers'])
        self.assertEqual(params['headers']['Time-Zone'], 'Asia/Tokyo')
        self.assertEqual(params['headers']['Accept'], 'application/vnd.github.v3+json')
        self.assertIn(params['headers']['Authorization'].replace('token ', ''), ['token0', 'token1'])

