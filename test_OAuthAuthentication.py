#!python3
#encoding:utf-8
import unittest
from authentication.OAuthAuthentication import OAuthAuthentication
class test_OAuthAuthentication(unittest.TestCase):
    def test_GetRequestParameters(self):
        token = 'token000'
        auth = OAuthAuthentication(token)
        params = auth.GetRequestParameters()
        print(params)
        self.assertTrue('headers' in params)
        self.assertTrue('Time-Zone' in params['headers'])
        self.assertTrue('Accept' in params['headers'])
        self.assertTrue('Authorization' in params['headers'])
        self.assertEqual(params['headers']['Time-Zone'], 'Asia/Tokyo')
        self.assertEqual(params['headers']['Accept'], 'application/vnd.github.v3+json')
        self.assertEqual(params['headers']['Authorization'], 'token ' + token)

