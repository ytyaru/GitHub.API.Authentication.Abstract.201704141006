#!python3
#encoding:utf-8
import unittest
from authentication.TwoFactorAuthentication import TwoFactorAuthentication
class test_TwoFactorAuthentication(unittest.TestCase):
    def test_GetRequestParameters(self):
        db = Database()
        db.Initialize()
        username = 'user'
        password = 'pass'
        two_factor_secret = 'base32secret3232'
        auth = TwoFactorAuthentication(username, password, two_factor_secret)
        params = auth.GetRequestParameters()
        print(params)
        self.assertTrue('headers' in params)
        self.assertTrue('Time-Zone' in params['headers'])
        self.assertTrue('Accept' in params['headers'])
        self.assertTrue('X-GitHub-OTP' in params['headers'])
        self.assertEquals(params['headers']['Time-Zone'], 'Asia/Tokyo')
        self.assertEquals(params['headers']['Accept'], 'application/vnd.github.v3+json')
        self.assertEquals(params['headers']['X-GitHub-OTP'], auth.OneTimePassword)
        self.assertTrue('auth' in params)
        self.assertEquals(params['auth'], (username, password))

