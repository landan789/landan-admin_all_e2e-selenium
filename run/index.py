import sys
import time
import json
import unittest

sys.path.append('..')

from testcase.signup import SignupTestcase
from HtmlTestRunner import HTMLTestRunner

CHATSHIER = json.load(open('./../config/chatshier.json', encoding = 'utf8'))

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(SignupTestcase('signup'))
    suite.addTest(SignupTestcase('signupWithExistingUser'))

    args = {
        'output': CHATSHIER['HTML_TEST_RUNNER']['OUTPUT'],
        'report_title': CHATSHIER['HTML_TEST_RUNNER']['REPORT_TITLE'] + ' - ' + CHATSHIER['SELENIUM']['TYPE'],
        'verbosity': 1
    }
    runner = HTMLTestRunner(**args)
    runner.run(suite)