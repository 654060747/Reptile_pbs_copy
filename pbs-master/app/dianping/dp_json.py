# coding=utf-8
# http://www.dianping.com/ajax/json/shopDynamic/basicHideInfo?shopId=19658572
import requests
import json

headers = {
	"Accept": "application/json, text/javascript, */*; q=0.01",
	"Referer": "http://www.dianping.com/shop/19658572",
	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36",
	"X-Requested-With": "XMLHttpRequest",
}

url="http://www.dianping.com/ajax/json/shopDynamic/basicHideInfo?shopId=19658572"
rs = requests.get(url,headers=headers, verify=False)
print(rs)
rs.encoding = 'utf-8'
data = json.loads(rs.text)
data_list = data["msg"]
print(data_list)
for data_one in data_list:
	data_all = data_one["shopInfo"]
	print(data_all)
	for one in data_all:
		address = one["address"]
		print(address)
		crossRoad = one["crossRoad"]
		print(crossRoad)
		phoneNo2 = one["phoneNo2"]
		print(phoneNo2)

