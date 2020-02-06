from selenium import webdriver
import time
driver = webdriver.Chrome(r'd:\chromedriver.exe')

#文件路径配置
URL1 = 'http://we.gobestsoft.com/'
URL2 = 'http://bug.gobestsoft.com:81/zentao/user-login-L3plbnRhby8=.html'

#浏览器全屏操作
def interface():
    driver.maximize_window()

#打开访问新网站地址
def open1(URL1):
    driver.get(URL1)

#直接访问网站地址
def open2(URL2):
    driver.get(URL2)

#多网页登录操作，输入账号/密码
def login1():
    driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/div/div[1]/figure/a").click()
    driver.find_element_by_xpath("//input[@name='account']").send_keys('zhangjiawei')
    driver.find_element_by_xpath("//input[@name='password']").send_keys('zhangjiawei')

#单网页登录操作，输入账号/密码
def login2():
    time.sleep(1)
    driver.find_element_by_xpath("//input[@name='account']").send_keys('zhangjiawei')
    time.sleep(1)
    driver.find_element_by_xpath("//input[@name='password']").send_keys('zhangjiawei')
    time.sleep(1)
    driver.find_element_by_xpath("//button[@type='submit']").click()

#单网页直接点击登录操作
def GO2():
    interface()
    open2(URL2)
    login2()
    time.sleep(5)

#跳转新网页点击操作
def GO1():
    open1(URL1)
    login1()
    time.sleep(5)

#调用方法    
GO2()




