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
	
	
	
	
	
	
	
# conding=utf-8
import time,os,random
from random import choice
from selenium import webdriver
from pyquery import PyQuery as pq
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent

# 代理ip
proxys = ["114.99.19.246:61234","117.191.11.113:8080","49.51.70.42:1080","182.108.44.89:3128","180.118.128.123:9000","218.95.50.108:9000","47.101.36.129:8118","117.90.2.89:9000","120.194.42.157:38185","122.242.85.157:9000","106.9.169.41:808","1.202.193.26:59212","116.196.115.209:8080","122.143.83.118:8080","180.118.128.195:9000","121.10.139.226:3128","221.2.175.238:8060","101.27.20.157:61234"]
#1.使用python random模块的choice方法随机选择某个元素
proxy = choice(proxys)

# 实例化代理对象
ops = Options()

# 随机产生User-Agent
User_Agent = UserAgent()
ua = User_Agent.random


def select_css(count,data,css,title):
	if count == 1:
		return data.select(css)
	if count == 2:
		return data.select(css)[0].getText().strip()
	if count == 3:
		return data.select(css)[0].get(title)


def data_(driver):
	time.sleep(7)
	html = driver.page_source 
	data = str(pq(html))  
	data = BeautifulSoup(data,"lxml")
	data.encoding = 'utf-8'
	return data


def by_list(data,driver,url_one):
	# 店名
	css = "#basic-info > h1"
	name = select_css(2,data,css,"")
	print("店名:::"+name.split("手机")[0])
	# 店家图片连接
	css = "#aside-photos > div > a > img"
	img = select_css(3,data,css,"src")
	print("店家图片连接:::"+img)

	# 去加密字体
	# b = data.select("#address")
	# div = data.select("#address")[0].getText()
	# print(b)
	# print(div)

	# 没加密
	css = "#sales > div:nth-child(2) > div"
	div_list = select_css(1,data,css,"")
	if len(div_list) > 0:
		for x in range(1,len(div_list)+1):
			css = "#sales > div:nth-child(2) > div:nth-child("+str(x)+") > p"
			# 促销优惠的项目名
			yh_name = select_css(2,data,css,"")
			print("项目名:::"+yh_name)

			# 团价
			css = "#sales > div:nth-child(2) > div:nth-child("+str(x)+") > span.price"
			price_tuan = select_css(2,data,css,"")
			print("团价:::"+price_tuan)

			# 门店价
			css = "#sales > div:nth-child(2) > div:nth-child("+str(x)+") > del"
			price_md = select_css(2,data,css,"")
			print("门店价:::"+price_md)

			time.sleep(2)
			# 点击跳转网页
			css = "#sales > div:nth-child(2) > div:nth-child("+str(x)+") > a"			
			driver.find_element_by_css_selector(css).click()
			d_data = data_(driver)
			# print(d_data)
			css = "#tab_show_1 > div:nth-child(4) > p"
			p_list = select_css(1,d_data,css,"")
			print(p_list)
			if len(p_list) > 0:
				# 团购详情
				tuan_text = select_css(2,d_data,css,"")
				print("团购详情::"+tuan_text)

			# css = "#tab_show_6 > div > div > dl"
			# gm_list = select_css(1,data,css,"")
			# if len(gm_list) > 0:
			# 	for z in range(1,len(gm_list)+1):
			# 		# 购买须知
			# 		css = "#tab_show_6 > div > div > dl:nth-child("+str(z)+") > dt"
			# 		gm_name = select_css(2,data,css,"")
			# 		print("须知名::"+gm_name)
			# 		# 购买须知
			# 		css = "#tab_show_6 > div > div > dl:nth-child("+str(z)+") > dt"
			# 		gm_text = select_css(2,data,css,"")
			# 		print("须知正文::"+gm_text)


	# css = "#sales > div:nth-child(3) > a"
	# a_list = select_css(1,data,css,"")
	# if len(a_list) > 0:
	# 	for y in range(1,len(a_list)+1):
	# 		# # 团价
	# 		# css = "#sales > div:nth-child(3) > a:nth-child("+str(y)+") > span"
	# 		# price_tuan = select_css(2,data,css,"")
	# 		# print("团价:::"+price_tuan)
	# 		# # 门店价
	# 		# css = "#sales > div:nth-child(3) > a:nth-child("+str(y)+") > del"
	# 		# price_md = select_css(2,data,css,"")
	# 		# print("门店价:::"+price_md)
	# 		css = "#sales > div:nth-child(3) > a"
	# 		yh_name = select_css(2,data,css,"")
	# 		print("项目名:::"+yh_name)




def by_dp_baoyang_data(url_one):

	# print('--proxy-server=http://%s' % proxy)
	ops.add_argument('--user-agent=%s' % ua)
	# ops.add_argument('--user-data-dir=C:/Users/Administrator/AppData/Local/Google/Chrome/User Data')
	ops.add_argument('--proxy-server=http://%s' % proxy)
	driver = webdriver.Chrome(chrome_options=ops)
	# driver = webdriver.Chrome()
	driver.get(url_one)
	data = data_(driver)

	by_list(data,driver,url_one)


url = ["http://www.dianping.com/shop/19658572"]	


for url_one in url:
	by_dp_baoyang_data(url_one)	
	
	
	
	
	
	
	
	
	
	
	

