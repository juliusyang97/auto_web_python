# coding=utf-8
# @Time:2022/2/28下午4:38 
# @Author: 放羊Wa
# @Github: juliusyang97

#!/usr/bin/env python3
# coding=utf-8

import time
from selenium import webdriver

print("初始化 ChromeDriver，并打开 Chrome")
path = './chromedriver'
driver = webdriver.Chrome(executable_path=path)
print("打开 shixuen.com 网址")
driver.get("https://rohm.eefocus.com/module/forum/plugin.php?id=xbigwheel:frontend&bigwheel_id=8")
# time.sleep(5)
# print("关闭浏览器")
# driver.close()

# print("初始化 geckodriver 并打开 Firefox 浏览器")
# driver = webdriver.Firefox()
# driver.get("https://www.shixuen.com")
# time.sleep(5)
# driver.close()
