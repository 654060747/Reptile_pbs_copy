#  coding= utf-8

import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

from dianping_address_pinglun_day import chinese_dict
from dianping_phone_time import number_dict

# # 中文字典
# chineses = chinese_dict()
# print(chineses)

# # 数字字典
# numbers = number_dict()
# print(numbers)




daili = {
    'http':'http://27.17.45.90:43411',
}

COOKIE = 'xxx'

# 随机产生User-Agent
ua = UserAgent()
User_Agent = ua.random
print(User_Agent)

def get_text(data, css):
    jcz_data = data.select(css)
    print(jcz_data)
    

jcz_one_url = 'http://www.dianping.com/shop/24294938'
headers = {
            'Cookie':COOKIE,
            'Referer':jcz_one_url,
            'Host':'www.dianping.com',
            'User-Agent':User_Agent,
         }
s=requests.session()
rs = requests.get(jcz_one_url, headers=headers, proxies=daili, verify=False)
rs.encoding = 'utf-8'
data_one_jcz = BeautifulSoup(rs.text, "lxml")
print(data_one_jcz)
css = '#basic-info > h1'
# get_text(data_one_jcz,css)


# def jcz_one_data(data,css,User_Agent):
#     jcz_href = data.select(css)
#     j = 0
#     for x in jcz_href:
#         j = j+1
#         if j > 1:
#             break
#         jcz_one_url = x.get('href')
       



# def jcz_list(url):
#     # 随机产生User-Agent
#     ua = UserAgent()
#     User_Agent = ua.random
#     print(User_Agent)

#     headers = {
#                 'Host':'www.dianping.com',
#                 'User-Agent':User_Agent,
#              }
#     rs = requests.get(url, headers=headers, verify=False)
#     rs.encoding = 'utf-8'
#     data_list_jcz = BeautifulSoup(rs.text, "lxml")
#     print(data_list_jcz)
#     css = '#shop-all-list > ul > li > div.txt > div.tit > a'
#     # jcz_one_data(data_list_jcz,css,User_Agent)



# for x in range(1,2):

#     url = 'http://www.dianping.com/search/keyword/1/0_车检站/p'+str(x)
#     jcz_list(url)
