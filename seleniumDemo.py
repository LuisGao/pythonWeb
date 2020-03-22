from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# browser = webdriver.Chrome()


# 打开百度 搜索特定文本，获取结果
# browser.get('https://www.baidu.com')
# input = browser.find_element_by_id('kw')
# input.send_keys('极客挖掘机')
# input.send_keys(Keys.ENTER)
# print(browser.current_url)
# print(browser.get_cookies())
# print(browser.page_source)

# 打开京东
# browser.get('https://www.jd.com/')
# input_Key = browser.find_element_by_id('key')
# lis = browser.find_elements_by_css_selector('.cate_menu li a')

# for i in range (len(lis)):
#     print(lis[i].text)

# print(browser.page_source)

# browser.close()

# AJAX 技术相关的适配
# 1. 等待数据的控制

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
# 隐式推送
driver.implicitly_wait(10) # seconds

# driver.get("https://www.jd.com/")
# try:
#     element = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.ID, "key"))
#     )
# finally:
#     driver.quit()

# 节点交互
driver.get('https://www.taobao.com/')
input = driver.find_element_by_id('q')
input.send_keys('IPad')
time.sleep(1)
input.clear()
input.send_keys('Surface Pro')
button = driver.find_element_by_class_name('btn-search')
button.click()
print(1)