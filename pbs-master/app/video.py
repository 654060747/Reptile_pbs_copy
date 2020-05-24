# coding=utf-8
import requests
import csv
from bs4 import BeautifulSoup
import threading,time


def by_title(data_text, css, title):
	lenght = len(data_text.select(css))
	print(lenght)
	if lenght != 0:
		data = data_text.select(css)[0].get(title)
		return data


def video_load(video_url, file_name):
	# url = 'https://vdept.bdstatic.com/73543177483165473638524345317459/7738755349486274/d5a747783bac493f9aa6c89fb15f737ec083dc3899d6adcabcd8e5398d68b7e898cc6bef267b91d39fe7e969a62dc2bd.mp4?auth_key=1590257422-0-0-d84293e86c00674b415fd6552d59c832'
	r = requests.get(video_url, stream=True)
	with open('./好看视频/握手视频/'+file_name+'.mp4', 'wb') as f:
		for data in r.iter_content(chunk_size=1024):
			f.write(data)


class MyThread(threading.Thread):
    """docstring for MyThread"""
    def __init__(self, arg, url, file_name):
        super(MyThread, self).__init__()
        self.arg = arg
        self.url = url
        self.file_name = file_name
      
    def run(self):        
        print("开始下载图片==="+threading.current_thread().getName())
        video_load(self.url, self.file_name)
        # time.sleep(2)
        print("OK==="+threading.current_thread().getName()+"此线程等待关闭")

# 测试
# url_one = 'https://haokan.baidu.com/v?vid=12210693398593428408'
# file_name = '12210693398593428408'


def get_video_url(url_one, file_name):
# def get_video_url(url_one, file_name, i):
	rs = requests.get(url_one, verify=False)
	data = BeautifulSoup(rs.text, "lxml")
	# print(data)
	css = '#rooot > div > div.page-left > div.videos > div.hkplayer > video.video'
	title = 'src'
	video_url = by_title(data, css, title)
	if video_url != None:
		video_load(video_url, file_name)
	# thread = MyThread(str(i), video_url, file_name)
	# thread.start()
	# if i%10 == 0:
	# 	print(i)
	# 	time.sleep(5)


# csv路径
csv_path = "./woshou_电视剧.csv"
# 读取csv文件
csv_file = csv.reader(open(csv_path,'r'))
for urls in csv_file:	
	i = 0	
	# 循环每一行内容
	for url_one in urls:
		i = i+1
		file_name = url_one.split('=')[1]
		print(url_one)
		get_video_url(url_one, file_name)
		# get_video_url(url_one, file_name, i)


# 测试
# get_video_url(url_one, file_name)
