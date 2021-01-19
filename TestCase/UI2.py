from selenium import webdriver
from selenium.webdriver.support.select import Select

import time

def input_demo(driver):
    # 定位元素
    input_el = driver.find_element_by_xpath("/html/body/table/tbody/tr[2]/td[2]/input")
    # 输入值
    input_el.send_keys("只要E的够快,队友的问号就追不上你")
    time.sleep(2)
    # clear : 清除
    input_el.clear()
    time.sleep(2)

def input_demo2(driver):
    # 定位元素 通过 ID 去定位
    file_el = driver.find_element_by_id('file1')
    file_el.send_keys('C:/Users/YSL/Pictures/TIM图片20190323105826.png')
    time.sleep(2)

    # 定位元素 通过 name 去定位
    radio_els = driver.find_elements_by_name('radio')
    print(type(radio_els))
    # 操作元素 , 点击
    radio_els[0].click()
    time.sleep(1)
    radio_els[1].click()
    time.sleep(2)

def check_box(driver):
    checkbox_els = driver.find_elements_by_class_name('checkbox')
    print(checkbox_els)
    checkbox_els[0].click()
    time.sleep(1)
    checkbox_els[1].click()
    time.sleep(1)
    checkbox_els[2].click()
    time.sleep(1)

def alter(driver):
    button_el = driver.find_element_by_xpath('//input[@value="普通按钮"]')
    button_el.click()
    time.sleep(1)
    # 确认弹框
    alert = driver.switch_to.alert
    alert.send_keys("周龙")
    driver.switch_to.alert.accept()
    time.sleep(1)
    # 取消弹框
    # driver.switch_to.alert.dismiss()

def input_demo3(driver):
    driver.find_element_by_xpath('//input[@type="password"]').send_keys("123456")
    number_el = driver.find_element_by_xpath('//input[@type="number"]')
    number_el.send_keys('20')

    driver.find_element_by_xpath('//textarea').send_keys('只要E的够快,队友的问号就追不上你')
    time.sleep(2)

def select_demo(driver):
    select_el = driver.find_element_by_css_selector(
        'body > table > tbody > tr:nth-child(12) > td:nth-child(2) > select')

    s = Select(select_el)
    # 通过索引选择
    s.select_by_index(1)
    time.sleep(1)
    # 通过value属性 选择
    s.select_by_value('z1')
    time.sleep(1)
    # 通过 展示的文本 选择
    s.select_by_visible_text('周龙3')
    time.sleep(1)
def time_demo(driver):
    js = '''var xpath = "//input[@type='date']";var element = document.evaluate(xpath,document,null,XPathResult.ANY_TYPE,null).iterateNext();element.setAttribute("value","2018-07-12");'''
    driver.execute_script(js)
def scroll_demo(driver):
    # a = driver.find_element_by_xpath("//input[@type=\"reset\"]")
    # js = "arguments[0].scrollIntoView();"
    # driver.execute_script(js, a)
    js = "var q=document.documentElement.scrollTop=10000"
    driver.execute_script(js)
def iframe_demo(driver):
    driver.get("http://www.guoyasoft.com:8080/guoya-client-qa/")
    cxms = driver.find_element_by_xpath("//a[contains(text(),'查询面试')]")
    cxms.click()
    time.sleep(3)
    #定位iframe
    iframe = driver.find_element_by_id("iframepage")
    driver.switch_to.frame(iframe)
    custmer_name = driver.find_element_by_xpath("//input[@name='custmerName']")
    custmer_name.clear()
    custmer_name.send_keys('sdfasdfasdf')
    #退出当前iframe
    driver.switch_to.parent_frame()
    #跳回最外层页面
    driver.switch_to.default_content()

    time.sleep(2)


if __name__ == '__main__':
    # driver = webdriver.Chrome('../chromedriver/chromedriver.exe')
    # driver.maximize_window()
    # iframe_demo(driver)

    # driver.get 打开一个指定网页
    # driver.get("http://localhost:8082/xuepl/demo1.html")

    # # 等待几秒
    # time.sleep(2)
    # time_demo(driver)
    # time.sleep(2)
    # scroll_demo(driver)
    # time.sleep(2)

    # input_demo(driver)

    # 定位超链接 (超链接的名字全写)
    # driver.find_element_by_link_text('当当').click()
    # time.sleep(3)
    # # 后退
    # driver.back()
    # time.sleep(1)
    # # 定位超链接 (超链接的名字写一部分 就可以)
    # driver.find_element_by_partial_link_text('度娘').click()
    # time.sleep(3)
    # driver.back()
    # time.sleep(1)
    # # 前进
    # driver.forward()
    # time.sleep(3)
    # # 刷新
    # driver.refresh()
    # time.sleep(3)
    # alter(driver)


    # 关闭浏览器
    # driver.quit()
    # driver.close()  也可以关闭浏览器,但是无法关闭驱动程序 ,一般用quit ,关闭的更彻底
    a = 'adf,gjkjk,ckokoa,sjodjo'
    #find 查找
    print(a.find("ackokoa"))
    #split 切割
    print(a.split(','))
    #replace 替换
    print(a.replace('a','1'))
    pass