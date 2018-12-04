# coding=utf-8
import sys
import json
import time
import re
from selenium.webdriver.common.by import By
from helper.chatshier import WebdriverHelper

sys.path.append('..')

CHATSHIER = json.load(open('./../config/chatshier.json', encoding = 'utf8'))

class SignupPage:
    def signup(self, user):
        """
        In /signup page, signup a user
        :param user:
        :return:
            string: '/chat', '/signup'
        """
        webdriver = WebdriverHelper.getInstance()
        webdriver.browser.get(CHATSHIER['URL']['DEV'] + type(self).__name__.lower())
        webdriver.browser.set_window_position(0, 0)
        time.sleep(0)

        # form name
        webdriver.browser.find_element(By.CSS_SELECTOR, 'form.signup-form fieldset > div:nth-child(1) input').send_keys(user['name'])

        # form email
        webdriver.browser.find_element(By.CSS_SELECTOR, 'form.signup-form fieldset > div:nth-child(2) input').send_keys(user['email'])

        # form password
        webdriver.browser.find_element(By.CSS_SELECTOR, 'form.signup-form fieldset > div:nth-child(3) input').send_keys(user['password'])

        # form password
        webdriver.browser.find_element(By.CSS_SELECTOR, 'form.signup-form fieldset > div:nth-child(4) input').send_keys(user['password'])

        webdriver.browser.find_element(By.CSS_SELECTOR, 'form.signup-form fieldset button[type="submit"]').click()

        time.sleep(1)
        match = re.search('\/[\w]*$', webdriver.browser.current_url)
        path = match.group()
        return path