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

COOKIE = 'cy=1; cye=shanghai; _lxsdk_cuid=16938f9a6d9c8-05f60982781ead-414f0c2a-1fa400-16938f9a6d9c8; _lxsdk=16938f9a6d9c8-05f60982781ead-414f0c2a-1fa400-16938f9a6d9c8; _hc.v=88d5ae19-7073-2cf8-07c9-167d6b476292.1551439079; _dp.ac.v=595e6a10-6bc9-4bd6-bafe-407d36b02a65; ctu=eec2323cade50d7a0263c59259c00cd037262a08b51e5d6eaac81a4338ef0517; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; s_ViewType=10; dper=a50a97542609e7a8958e5e260f74debc7575e4823232d0931131382aeadfc7b99735c4f6ac85a412315d813f214201705b65e7d4a27221412e324b4efe9045a2f4cdd1e18b577f953b88b8e583b5afd5c139283419bc82b10ae819ffa5a1f2f3; ua=dpuser_4772089894; uamo=18321298725; ll=7fd06e815b796be3df069dec7836c3df; _lxsdk_s=16942f6c950-58d-396-c7%7C%7C89'

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