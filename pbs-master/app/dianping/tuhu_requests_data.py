# encoding='utf-8'
import time,os
from selenium import webdriver
from pyquery import PyQuery as pq
from bs4 import BeautifulSoup

# root_path = "./down_car_data/"

# def CheckDir(dir):
#     if not os.path.exists(dir):
#       os.makedirs(dir)
#     pass


# def write_file(car,car_xh,url):
# 	CheckDir(root_path)
# 	file_name = root_path+"car.csv"
# 	# encoding='utf-8'
# 	with open(file_name, 'a+') as f:
# 		writer = f.write(car+","+car_xh+","+url+'\n')


def data_(driver):
	time.sleep(3)
	html = driver.page_source 
	data = str(pq(html))  
	data = BeautifulSoup(data,"lxml")
	data.encoding = 'utf-8'
	return data


def by_list(data,driver):
	dl_list = data.select("#package_baoyang > dl")
	print(len(dl_list))
	for i in range(1,len(dl_list)+1):
		baoyang_list_text = data.select("#package_baoyang > dl:nth-child("+str(i)+") > dt > span")[0].getText()
		print(baoyang_list_text+":::")
		dd_list = data.select("#package_baoyang > dl:nth-child("+str(i)+") > dd")
		for x in range(2,len(dd_list)+2):
			baoyang_text = data.select("#package_baoyang > dl:nth-child("+str(i)+") > dd:nth-child("+str(x)+") > div > span")[0].getText()
			print(baoyang_text)
			
			if "小保养服务" not in baoyang_text:
				driver.find_element_by_css_selector("#package_baoyang > dl:nth-child("+str(i)+") > dd:nth-child("+str(x)+")").click()
				time.sleep(2)


def by_tuhu_baoyang():
	driver = webdriver.Chrome()
	driver.get('https://by.tuhu.cn/baoyang/VE-ZAR-Giulia/pl2.0T-n2019.html')
	data = data_(driver)
	# 得到多少保养类型
	by_list(data,driver)
	

by_tuhu_baoyang()

