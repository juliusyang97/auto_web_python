# coding=utf-8
# @Time:2022/2/28下午4:09 
# @Author: 放羊Wa
# @Github: juliusyang97

from selenium import webdriver

#设置自动化打开的浏览器访问网址
url = 'https://www.baidu.com'

#设置谷歌浏览器driver的目录所在
path = './chromedriver'

browser = webdriver.Chrome(executable_path=path)

#打开浏览器，并访问设置的网址。
browser.get(url)