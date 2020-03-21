from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()


# 打开百度 搜索特定文本，获取结果
browser.get('https://www.baidu.com')
input = browser.find_element_by_id('kw')
input.send_keys('极客挖掘机')
input.send_keys(Keys.ENTER)
print(browser.current_url)
print(browser.get_cookies())
print(browser.page_source)

# 打开京东
browser.get('https://www.jd.com/')
print(browser.page_source)
browser.close()

