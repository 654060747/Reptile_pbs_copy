import requests
import re,csv
import json
# from contextlib import closing
# from pyquery import PyQuery as pq
from requests import RequestException

class bilibili():
    def __init__(self):
        self.getHtmlHeaders={
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q = 0.9'
        }

        self.downloadVideoHeaders={
            'Origin': 'https://www.bilibili.com',
            'Referer': 'https://www.bilibili.com/video',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
        }


    #一般这里得到的网页源码和F12查看看到的不一样，因为F12开发者工具里的源码经过了浏览器的解释
    def getHtml(self,url):
        try:
            response = requests.get(url=url, headers=self.getHtmlHeaders, verify=False)
            print(response.status_code)
            if response.status_code == 200:
                return response.text
        except RequestException:
            print('请求Html错误:')


    def parseHtml(self,html):
        #用pq解析得到视频标题
        # doc = pq(html)
        #用正则、json得到视频url;用pq失败后的无奈之举
        pattern = r'\<script\>window\.__playinfo__=(.*?)\</script\>'
        result = re.findall(pattern, html)[0]
        # print(result)
        temp = json.loads(result)
        # #temp['durl']是一个列表，里面有很多字典
        #video_url = temp['durl']
        
        if 'durl' in temp['data'].keys():
            for item in temp['data']['durl']:
                if 'url' in item.keys():
                    video_url = item['url']
        elif 'dash' in temp['data'].keys():
             for item in temp['data']['dash']:
                if 'base_url' in item.keys():
                    video_url = item['base_url']

        print(video_url)
        # return video_url


    def download_video(self,video_url,file_name):      
        # with open(filename, "wb") as f:
        #     f.write(requests.get(url=url, headers=self.downloadVideoHeaders, stream=True, verify=False).content)

        r = requests.get(url=video_url, headers=self.downloadVideoHeaders, stream=True, verify=False)
        with open('./B站视频/握手/'+file_name+'.mp4', 'wb') as f:
          for data in r.iter_content(chunk_size=1024):
              f.write(data)

        #closing适用于提供了 close() 实现的对象，比如网络连接、数据库连接
        # with closing(requests.get(video['url'], headers=self.downloadVideoHeaders, stream=True, verify=False)) as res:
        #     if res.status_code == 200:
        #         with open(filename, "wb") as f:
        #             for chunk in res.iter_content(chunk_size=1024):
        #                 if chunk:
        #                     f.write(chunk)

    def run(self,url,file_name):
        # self.download_video(self.parseHtml(self.getHtml(url)),file_name)
        self.parseHtml(self.getHtml(url))


    def red_csv(self,csv_path):
        # 读取csv文件
        csv_file = csv.reader(open(csv_path,'r'))
        for urls in csv_file: 
          i = 0   
          # 循环每一行内容
          for url_one in urls:
              i = i+1
              file_name = url_one.split('video/')[1]
              print(url_one)
              # print(file_name)
              self.run(url_one,file_name)


# csv路径
csv_path = "./B站.csv"
if __name__ == '__main__':
    bilibili().red_csv(csv_path)
