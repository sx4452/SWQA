#-*-coding:utf-8-*-
from selenium import webdriver
import time
import urllib
import os

# 爬取页面地址
url = 'http://pic.sogou.com/pics?query=RGBD&w=05009900&p=40030500&_asf=pic.sogou.com&_ast=1451309589&sc=index&sut=2241&sst0=1451309589162'

# 目标元素的xpath
xpath = '//div[@id="imgid"]/ul/li/a/img'

# 启动Firefox浏览器
driver = webdriver.Firefox()

# 最大化窗口，因为每一次爬取只能看到视窗内的图片
driver.maximize_window()

# 记录下载过的图片地址，避免重复下载
img_url_dic = {}

# 浏览器打开爬取页面

start = time.clock();
driver.get(url)
end = time.clock();
print 'web open time is:'
print end - start;
# 模拟滚动窗口以浏览下载更多图片
pos = 0
m = 0 # 图片编号
for i in range(10):
	pos += i*500 # 每次下滚500
	js = "document.documentElement.scrollTop=%d" % pos
	driver.execute_script(js)
	time.sleep(1)

	for element in driver.find_elements_by_xpath(xpath):
		img_url = element.get_attribute('src')
		# 保存图片到指定路径
		if img_url != None and not img_url_dic.has_key(img_url):
			img_url_dic[img_url] = ''
			m += 1
			ext = img_url.split('.')[-1]
			filename = str(m) + '.' +  'jpg'
			#保存图片数据
			data = urllib.urlopen(img_url).read()
            #tmpstr = 'C://Users/ben/Desktop/Output/' + filename
            #os.makedirs(tmpstr, 0o777, False)
			f = open('C://Users/ben/Desktop/Output/' + filename, 'wb')
			f.write(data)
			f.close()
driver.close()

print 'image data in C://Users/ben/Desktop/Output/'