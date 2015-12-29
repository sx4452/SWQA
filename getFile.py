from selenium import webdriver
import time
driver = webdriver.Firefox()
base_url = 'http://mcg.nju.edu.cn/publication.html'
start = time.clock()
driver.get(base_url)
end = time.clock();
print 'web open time is:'
print end - start;
xpath = '//div[@class="njumcg_text"]/ul/li';
f = open('C://Users/ben/Desktop/Output_test/getFileOut.txt', 'w+');

for element in driver.find_elements_by_xpath(xpath):
    txt = element.text;
    img_url = txt.encode('UTF-8');
    f.write(img_url + '\r\n');

f.close()

print 'text data in C://Users/ben/Desktop/Output_test/getFileOut.txt'