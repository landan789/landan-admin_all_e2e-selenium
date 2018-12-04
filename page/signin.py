# coding=utf-8
import sys
import json
import time
from selenium.webdriver.common.by import By
from helper.chatshier import WebdriverHelper

sys.path.append('..')

CHATSHIER = json.load(open('./../config/chatshier.json', encoding = 'utf8'))
users = json.load(open('./../data/users.json', encoding = 'utf8'))

class Signin:
    def signin(self):
        webdriverHlp = WebdriverHelper();
        browser = webdriverHlp.getInstance()

        browser.get(CHATSHIER['URL']['DEV'] + type(self).__name__.lower())
        browser.set_window_position(0, 0)
        time.sleep(0)

        user = users.pop()

        # form email
        browser.find_element(By.CSS_SELECTOR, 'form.signin-form fieldset > div:nth-child(1) input').send_keys(user['email'])

        # form password
        browser.find_element(By.CSS_SELECTOR, 'form.signin-form fieldset > div:nth-child(2) input').send_keys(user['password'])

        browser.find_element(By.CSS_SELECTOR, 'form.signin-form fieldset button[type="submit"]').click()

        time.sleep(5)

signin = Signin()
signin.signin()