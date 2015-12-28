#-*-coding:gbk-*-
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0

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
driver.find_element_by_id("q").send_keys('如何看待知乎搜索')
driver.find_element_by_css_selector("button.zu-top-search-button").click()
'''

'''
base_url = 'http://mcg.nju.edu.cn'
driver.get(base_url)
driver.find_element_by_link_text(u"论著").click()
'''


#driver.quit()

'''
# Create a new instance of the Firefox driver
driver = webdriver.Firefox()

# go to the google home page
driver.get("http://www.baidu.com")

# the page is ajaxy so the title is originally this:
print driver.title

# find the element that's name attribute is q (the google search box)
inputElement = driver.find_element_by_name("q")

# type in the search
inputElement.send_keys("cheese!")

# submit the form (although google automatically searches now without submitting)
inputElement.submit()

try:
    # we have to wait for the page to refresh, the last thing that seems to be updated is the title
    WebDriverWait(driver, 10).until(EC.title_contains("cheese!"))

    # You should see "cheese! - Google Search"
    print driver.title

finally:
    driver.quit()
'''