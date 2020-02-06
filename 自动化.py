from selenium import webdriver
import time
driver = webdriver.Chrome(r'd:\chromedriver.exe')

#文件路径配置
#url = 'http://we.gobestsoft.com/'
url = 'http://bug.gobestsoft.com:81/zentao/user-login-L3plbnRhby8=.html'


driver.get(url)

#登录操作，输入账号/密码
#driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/div/div[1]/figure/a").click()
driver.find_element_by_xpath("//input[@name='account']").send_keys('zhangjiawei')
time.sleep(1)
driver.find_element_by_xpath("//input[@name='password']").send_keys('zhangjiawei')
time.sleep(1)
driver.find_element_by_xpath("//button[@type='submit']").click()






