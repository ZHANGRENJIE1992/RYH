from selenium import webdriver
import os,time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys #需要引入 keys 包

def login(account,password,browser):
    #loginButton = "//*[@id=\"app\"]/div[1]/div[2]/div[2]/div/div/div[2]/button"
    browser.find_element_by_xpath("/html/body/div/div[1]/div[2]/div[2]/div/div/div[2]/form/div[1]/div/div/input").send_keys(account)
    time.sleep(0.4)
    browser.find_element_by_xpath("/html/body/div/div[1]/div[2]/div[2]/div/div/div[2]/form/div[1]/div/div/input").send_keys(Keys.TAB)
    time.sleep(0.4)
    browser.find_element_by_xpath("/html/body/div/div[1]/div[2]/div[2]/div/div/div[2]/form/div[2]/div/div/input").send_keys(password)
    time.sleep(0.4)
    browser.find_element_by_xpath("/html/body/div/div[1]/div[2]/div[2]/div/div/div[2]/button").send_keys(Keys.ENTER)
    time.sleep(0.4)

    return browser



