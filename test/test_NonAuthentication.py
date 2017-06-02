#!python3
#encoding:utf-8
import unittest
from authentication.NonAuthentication import NonAuthentication
class test_NonAuthentication(unittest.TestCase):
    def test_GetRequestParameters(self):
        auth = NonAuthentication()
        params = auth.GetRequestParameters()
        print(params)
        self.assertTrue('headers' in params)
        self.assertTrue('Time-Zone' in params['headers'])
        self.assertTrue('Accept' in params['headers'])
        self.assertEquals(params['headers']['Time-Zone'], 'Asia/Tokyo')
        self.assertEquals(params['headers']['Accept'], 'application/vnd.github.v3+json')

