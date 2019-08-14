# conding=utf-8
import time,os,random
from random import choice
from selenium import webdriver
from pyquery import PyQuery as pq
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent

# 代理ip
proxys = ["119.190.146.177:8060","117.191.11.112:80","121.10.139.226:3128","221.2.175.238:8060","117.191.11.71:80"]
#1.使用python random模块的choice方法随机选择某个元素
proxy = choice(proxys)

# 实例化代理对象
ops = Options()

# 随机产生User-Agent
User_Agent = UserAgent()
ua = User_Agent.random


def data_(driver):
	time.sleep(0.5)
	html = driver.page_source 
	data = str(pq(html))  
	data = BeautifulSoup(data,"lxml")
	data.encoding = 'utf-8'
	return data


def by_list(data,driver,url_one):
	a = data.select("#address > e:nth-child(1)")
	dl_list = data.select("#address > e:nth-child(1)")[0].getText()
	print(a)
	print(dl_list)

def by_dp_baoyang_data(url_one):

	# print('--proxy-server=http://%s' % proxy)
	ops.add_argument('--user-agent=%s' % ua)
	# ops.add_argument('--user-data-dir=C:/Users/Administrator/AppData/Local/Google/Chrome/User Data')
	ops.add_argument('--proxy-server=http://%s' % proxy)
	driver = webdriver.Chrome( chrome_options=ops)
	driver.get(url_one)
	data = data_(driver)
	# 得到保养类型
	by_list(data,driver,url_one)


# url = ["http://www.dianping.com/shop/67241624"]	
url = ["view-source:http://www.dianping.com/shop/67241624"]	


for url_one in url:
	by_dp_baoyang_data(url_one)
