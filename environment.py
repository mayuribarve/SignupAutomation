import os
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

gecko = os.path.normpath(os.path.join(os.path.dirname(__file__), 'geckodriver'))
binary = FirefoxBinary(r'C:\Program Files\Mozilla Firefox\firefox.exe')
browser = webdriver.Firefox()
browser.maximize_window()
browser.implicitly_wait(60)
# def before_all(context):
#     context.browser = webdriver.Firefox()
#     context.browser.implicitly_wait(60)
#     context.browser.maximize_window()


# def after_all(context):
#     context.browser.quit()
