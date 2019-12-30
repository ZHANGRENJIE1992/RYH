from convert import convert 
from openBrowser import openBrowser
import os,time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys #需要引入 keys 包
from selenium import webdriver

def operation(argv):    
    #notfindelementflag_A = True
    notfindelementflag_B = True
    notfindelementflag_C = True
    notfindelementflag_D = True
    notfindelementflag_E = True
    notfindelementflag_F = True
    notfindelementflag_G = True
    keyinfo=convert(argv)
    urlEntry="https://www.hengyirong.com/user/login"
    closenotificationbuttonpath = f"/html/body/div[1]/div[2]/div[1]/div/div[1]/button"
    provideLoanpath = f"/html/body/div[1]/div[1]/div[2]/div/div/div[2]/ul/li[2]"
    periodpath = f"/html/body/div[1]/div[1]/div[3]/div/div/div[2]/div/div[1]/div[1]/div/div/input"
    periodMonthpath = f"/html/body/div[2]/div[1]/div[1]/ul/li[{argv[3]}]"
    periodMoneypath = f"/html/body/div[1]/div[1]/div[3]/div/div/div[2]/div/div[1]/div[2]/div/input"
    loanButtonpath=f"/html/body/div[1]/div[1]/div[3]/div/div/div[2]/div/div[2]/div[1]/div[2]/ul[2]/li[4]/button"
    loanImdpath = f"/html/body/div/div[1]/div[3]/div[1]/div/div[2]/div[2]/div[2]/div[3]/button"
    #//span[contains(text(), month)]
    browser = openBrowser(keyinfo,urlEntry)
    time.sleep(1)

    #while notfindelementflag_A:
    try:#登陆后关闭弹框
        browser.find_element_by_xpath(closenotificationbuttonpath).send_keys(Keys.ENTER)
        #notfindelementflag_A = False
    except:
        time.sleep(0.5)

    while notfindelementflag_B:
        try:
            browser.find_element_by_xpath(provideLoanpath).click()#进入出借页面
            notfindelementflag_B = False
        except:
            time.sleep(0.5)

    #while findelement_periodpath:
    browser.execute_script('window.scrollBy(0,400)')#操作滚动条查找
    time.sleep(0.2)

    while notfindelementflag_C:
        try:
            browser.find_element_by_xpath(periodpath).click()#输入锁定期
            notfindelementflag_C = False
        except:
            time.sleep(0.5)

    while notfindelementflag_D:
        try:
            browser.find_element_by_xpath(periodMonthpath).click()#输入时间
            notfindelementflag_D = False
        except:
            time.sleep(0.5)

    while notfindelementflag_E:
        try:
            browser.find_element_by_xpath(periodMoneypath).send_keys(argv[4])#输入金额
            notfindelementflag_E = False
        except:
            time.sleep(0.5)  

    while notfindelementflag_F:
        try:
            browser.find_element_by_xpath(loanButtonpath).click()#点击提交
            notfindelementflag_F = False
        except:
            time.sleep(0.5)        

    while notfindelementflag_G:
        try:
            browser.find_element_by_xpath(loanImdpath).click()#点击提交（界面二）
            notfindelementflag_G = False
        except:
            time.sleep(0.5)   



    time.sleep(30)


