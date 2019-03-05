#  coding= utf-8

import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from login import ElementProxyGetCookie
from dianping_address_pinglun_day import chinese_dict
from dianping_phone_time import number_dict

# # 中文字典
# chineses = chinese_dict()
# print(chineses)

# # 数字字典
# numbers = number_dict()
# print(numbers)

# 拿到COOKIE
lgtoken = ElementProxyGetCookie().get('lgtoken')
print(lgtoken)


<<<<<<< HEAD
# daili = {
#     'http':'http://27.17.45.90:43411',
# }
COOKIE = 'cy=1; cye=shanghai; _lxsdk_cuid=169425426d455-0048b06f7bdea1-6b111b7e-1fa400-169425426d5c8; _lxsdk=169425426d455-0048b06f7bdea1-6b111b7e-1fa400-169425426d5c8; _hc.v=8aa962dd-2d6b-ecdf-dcc0-e2a1f3b4114e.1551596006; s_ViewType=10; ctu=eec2323cade50d7a0263c59259c00cd05d6842c451656cadb1685908aece1e77; _dp.ac.v=3b4a9bfc-f35b-4e14-ad4f-ff09246e69fe; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; vivi8dd=y; dkwlsn3=y; lgtoken='+lgtoken+'; dper=a50a97542609e7a8958e5e260f74debc928f3475defc60fc5a5ebc5fdbaed73e34023e4eb80b03d7d69785522c5be327519b09cce8483c636e5250285641c0b40316369be98cc7beab4b490d384f4eeb218c49694870c092024a356248ec85d9; ll=7fd06e815b796be3df069dec7836c3df; ua=dpuser_4772089894; uamo=18321298725; _lxsdk_s=16949757f9e-41c-f34-94f%7C%7C62'
=======

daili = {
    'http':'http://27.17.45.90:43411',
}

COOKIE = 'xxx'
>>>>>>> 09958babb656ff18242b6390071c7fb5e97d7928

# 随机产生User-Agent
ua = UserAgent()
User_Agent = ua.random
print(User_Agent)

def get_text(data, css):
    data_css = data.select(css)
    return data_css
    

jcz_one_url = 'http://www.dianping.com/shop/24294938'
headers = {
			'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Cookie':COOKIE,
            'Referer':jcz_one_url,
            'Host':'www.dianping.com',
            'User-Agent':User_Agent,
         }
s=requests.session()
rs = requests.get(jcz_one_url, headers=headers, verify=False)
rs.encoding = 'utf-8'
data_one_jcz = BeautifulSoup(rs.text, "lxml")
print(data_one_jcz)

css = '#basic-info > h1'
name_data = get_text(data_one_jcz,css)
name = name_data[0].getText().split("手机")[0].strip()
print("名称："+name)

css = '#address'
address_data = get_text(data_one_jcz,css)
print(address_data)
# for tag_class in address_data:
# 	tag = tag_class.get('class')
# 	print(tag)
	
# css = '#reviewlist-wrapper'
# pl_data = get_text(data_one_jcz,css)
# for pl_one_data in pl_data:
# 	a_list = pl_one_data.find_all('a')
		


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
