from selenium import webdriver
from selenium.webdriver.support.select import Select
import time



if __name__ == '__main__':
    driver = webdriver.Chrome('../chromedriver/chromedriver.exe')
    driver.maximize_window()

    # 打开浏览器
    driver.get('http://qa.yansl.com')
    time.sleep(2)
    # 清除原用户名
    yfm = driver.find_element_by_xpath("//input[@type='text']").clear()
    # 输入用户名
    driver.find_element_by_xpath("//input[@type='text']").send_keys('admin')
    # 清除原密码
    driver.find_element_by_xpath('//input[@type ="password"]').clear()
    # 输入密码
    driver.find_element_by_xpath('//input[@type ="password"]').send_keys('123456')
    # 点击登录
    driver.find_element_by_xpath("//span[contains(text(),'登录')]").click()
    # 点击残忍拒绝
    driver.find_element_by_xpath("//span[contains(text(),'残忍拒绝')]").click()
    time.sleep(2)
    # 再次点击登录
    driver.find_element_by_xpath("//span[contains(text(),'登录')]").click()

    # time.sleep(2)
    # driver.close()