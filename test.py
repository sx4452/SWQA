#-*-coding:utf-8-*-
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
import os

driver = webdriver.Firefox()

'''
base_url = 'http://image.baidu.com'
driver.get(base_url)
driver.find_element_by_id("kw").clear()
driver.find_element_by_id("kw").send_keys("RGBD")
driver.find_element_by_css_selector("input.s_btn.s_btn_down").click()
driver.find_element_by_css_selector("a.down").click()
driver.find_element_by_css_selector("a.down").click()
'''

'''
base_url = 'http://www.zhihu.com'
driver.get(base_url)
driver.find_element_by_id("q").clear()
driver.find_element_by_id("q").send_keys('��ο���֪������')
driver.find_element_by_css_selector("button.zu-top-search-button").click()
'''

'''
base_url = 'http://mcg.nju.edu.cn'
driver.get(base_url)
driver.find_element_by_link_text(u"����").click()
'''


base_url = 'http://www.twitch.tv/directory/game/World%20of%20Warcraft'
driver.get(base_url)
xpath = '//div[@class="thumb"]/a';
f = open('C://Users/ben/Desktop/Output_test/testOut.txt', 'wb');
for element in driver.find_elements_by_xpath(xpath):
    img_url = element.get_attribute('href');
    f.write(img_url + '\r\n');

f.close()




