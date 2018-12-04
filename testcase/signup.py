# coding=utf-8
import sys
sys.path.append('..')

import json
import unittest
from page.signup import SignupPage

CHATSHIER = json.load(open('./../config/chatshier.json', encoding = 'utf8'))
users = json.load(open('./../data/users.json', encoding = 'utf8'))


class SignupTestcase(unittest.TestCase):
    def signup(self):
        signupPage = SignupPage()
        args = {
            'user': users[0] # new user
        }
        path = pageSignupSignup.signup(**args)
        self.assertEqual(path, '/chat')

    def signupWithExistingUser(self):
        signupPage = SignupPage()
        args = {
            'user': users[1] # existing user
        }
        path = signupPage.signup(**args)
        self.assertEqual(path, '/signup')