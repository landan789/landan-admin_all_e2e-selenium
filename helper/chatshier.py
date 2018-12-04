from selenium import webdriver
import json

CHATSHIER = json.load(open('../config/chatshier.json'))

class WebdriverHelper:
    __instance = None
    def __init__(self):
        if WebdriverHelper.__instance != None:
            raise Exception("This class is a singleton!")
        elif 'CHROME' == CHATSHIER['SELENIUM']['TYPE']:
            self.browser = webdriver.Chrome(executable_path = './../ext/chromedriver.exe')
        elif 'FIREFOX' == CHATSHIER['SELENIUM']['TYPE']:
            self.browser = webdriver.Firefox(executable_path = './../ext/geckodriver.exe')
        elif 'EDGE' == CHATSHIER['SELENIUM']['TYPE']:
            self.browser = webdriver.Edge(executable_path = './../ext/edgedriver.exe')
        elif 'OPERA' == CHATSHIER['SELENIUM']['TYPE']:
            options = webdriver.ChromeOptions()
            options.binary_location = "C:/Program Files/Opera/52.0.2871.40/opera.exe"  # It needs to set the directory of opera.exe
            self.browser = webdriver.Opera(options=options)
        elif 'IE' == CHATSHIER['SELENIUM']['TYPE']:
            self.browser = webdriver.Ie(executable_path = './../ext/IEDriverServer.exe')
        elif 'SAFARI' == CHATSHIER['SELENIUM']['TYPE']:
            self.browser = webdriver.Safari()
        else:
            capabilities = {
                'platform':          'ANY',
                'browserName':       'chrome',
                'version':           '',
                'javascriptEnabled': True
            }
            self.browser = webdriver.Remote(command_executor = 'http://127.0.0.1:4444/wd/hub', desired_capabilities = capabilities)
        WebdriverHelper.__instance = self
    @staticmethod
    def getInstance():
        """ Static access method. """
        if WebdriverHelper.__instance == None:
            WebdriverHelper()
        return WebdriverHelper.__instance
