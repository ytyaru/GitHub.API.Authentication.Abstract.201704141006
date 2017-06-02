#!python3
#encoding:utf-8
import unittest
from authentication.OAuthTokenFromDatabaseAndCreateApiAuthentication import OAuthTokenFromDatabaseAndCreateApiAuthentication
class test_OAuthTokenFromDatabaseAndCreateApiAuthentication(unittest.TestCase):
    def test_GetRequestParameters(self):
        db = Database()
        db.Initialize()
        username = 'user1'
        password = 'pass1'
        two_factor_secret = 'base32secret3232'
        aut = OAuthTokenFromDatabaseAndCreateApiAuthentication(db, username, password, two_factor_secret)
        params = auth.GetRequestParameters()
        self.assertTrue('headers' in params)
        self.assertTrue('Time-Zone' in params['headers'])
        self.assertTrue('Accept' in params['headers'])
        self.assertTrue('Authorization' in params['headers'])
        self.assertEquals(params['headers']['Time-Zone'], 'Asia/Tokyo')
        self.assertEquals(params['headers']['Accept'], 'application/vnd.github.v3+json')
        self.assertEquals(params['headers']['Authorization'], 'token ' + 'token2')

