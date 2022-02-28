> 说明： 本教程适用于Linux、mac、Windows

## 环境要求

1. python
2. selenium库
3. 谷歌浏览器

## 环境配置

1. 安装selenium库
```python
pip install selenium
```

2. 安装谷歌浏览器、检查谷歌浏览器的版本

3. 根据所安装的浏览器版本下载对应的webdriver
下载地址：http://npm.taobao.org/mirrors/chromedriver/

## 测试环境

> 完成安装后，创建一个test.py的Python文件，看看能否自动启动谷歌浏览器。

```python
from selenium import webdriver

#设置自动化打开的浏览器访问网址
url = 'https://www.chenxiaohei.net'

#设置谷歌浏览器driver的目录所在
path = '/Users/chengf/Documents/Python/Project/selenium_chrome/chromedriver'

browser = webdriver.Chrome(executable_path=path)

#打开浏览器，并访问设置的网址。
browser.get(url)
```

