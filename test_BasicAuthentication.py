#!python3
#encoding:utf-8
import unittest
from authentication.BasicAuthentication import BasicAuthentication
class test_BasicAuthentication(unittest.TestCase):
    def test_GetRequestParameters(self):
        username = 'user'
        password = 'pass'
        auth = BasicAuthentication(username, password)
        params = auth.GetRequestParameters()
        print(params)
        self.assertTrue('headers' in params)
        self.assertTrue('Time-Zone' in params['headers'])
        self.assertTrue('Accept' in params['headers'])
        self.assertEqual(params['headers']['Time-Zone'], 'Asia/Tokyo')
        self.assertEqual(params['headers']['Accept'], 'application/vnd.github.v3+json')
        self.assertTrue('auth' in params)
        self.assertEqual(params['auth'], (username, password))

