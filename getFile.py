from selenium import webdriver
driver = webdriver.Firefox()
base_url = 'http://mcg.nju.edu.cn/publication.html'
driver.get(base_url)
xpath = '//div[@class="njumcg_text"]/ul/li';
f = open('C://Users/ben/Desktop/Output_test/getFileOut.txt', 'w+');

for element in driver.find_elements_by_xpath(xpath):
    txt = element.text;
    img_url = txt.encode('UTF-8');
    f.write(img_url + '\r\n');

f.close()