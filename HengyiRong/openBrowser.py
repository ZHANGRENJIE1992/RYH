from login import login
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import requests
#开启网站完成登陆
def openBrowser(keyinfo,urlEntry):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])
    browser=webdriver.Chrome(chrome_options=chrome_options)

    browser.get(urlEntry)
    r = requests.get(urlEntry)
    print(r.status_code)
    print("打开浏览器并开始登陆")

    browser = login(keyinfo[0],keyinfo[1],browser)

    return browser



