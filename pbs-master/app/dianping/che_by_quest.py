# coding=utf-8
import time,os,random
from random import choice
from selenium import webdriver
from pyquery import PyQuery as pq
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent

# 字典
# dict_list = {'&#xf147;':'1','&#xf0d2;':'2','&#xe208;':'3','&#xf273;':'4','&#xf33a;':'5','&#xe6c9;':'6','&#xf534;':'7','&#xf083;':'8','&#xf584;':'9','&#xf33b;':'O','&#xef1f;':'店','&#xe46d;':'中','&#xf43f;':'美','&#xf734;':'家','&#xe075;':'馆','&#xf8c0;':'小','&#xf01f;':'车','&#xf2cb;':'大','&#xe819;':'市','&#xea37;':'公','&#xe0e8;':'酒','&#xe671;':'行','&#xf363;':'国','&#xe394;':'品','&#xe5f2;':'发','&#xea98;':'电','&#xf86f;':'金','&#xf22a;':'心','&#xf127;':'业','&#xe803;':'商','&#xe57c;':'司','&#xe865;':'超','&#xeaaf;':'生','&#xf1a3;':'装','&#xf6a2;':'园','&#xece3;':'场','&#xef24;':'食','&#xe0a4;':'有','&#xe741;':'新','&#xe0c3;':'限','&#xf78d;':'天','&#xe0a2;':'面','&#xf418;':'工','&#xe779;':'服','&#xf279;':'海','&#xed94;':'华','&#xf20e;':'水','&#xef15;':'房','&#xea4e;':'饰','&#xf138;':'城','&#xf322;':'乐','&#xecd4;':'汽','&#xe4e9;':'香','&#xf7bd;':'部','&#xec35;':'利','&#xf609;':'子','&#xf7b3;':'老','&#xe69f;':'艺','&#xeecb;':'花','&#xe0b9;':'专','&#xe8e3;':'东','&#xf5f6;':'肉','&#xe55e;':'菜','&#xf499;':'学','&#xe873;':'福','&#xe60f;':'饭','&#xed91;':'人','&#xe137;':'百','&#xf8ef;':'餐','&#xf0c8;':'茶','&#xee9e;':'务','&#xf177;':'通','&#xf3d4;':'昧','&#xe493;':'所','&#xec3d;':'山','&#xe583;':'区','&#xf554;':'门','&#xeefc;':'药','&#xe25a;':'银','&#xe1ba;':'农','&#xe624;':'龙','&#xf735;':'停','&#xec20;':'尚','&#xf88e;':'安','&#xe31f;':'广','&#xf685;':'鑫','&#xe498;':'一','&#xf3b2;':'容','&#xe1da;':'动','&#xf8ec;':'南','&#xe094;':'具','&#xe0cc;':'源','&#xebee;':'兴','&#xf243;':'鲜','&#xe3f4;':'记','&#xe714;':'时','&#xe106;':'机','&#xf22e;':'烤','&#xef77;':'文','&#xe52e;':'康','&#xf359;':'信','&#xe237;':'果','&#xe4ae;':'阳','&#xee36;':'理','&#xe37f;':'锅','&#xe2f1;':'宝','&#xf632;':'达','&#xeb93;':'地','&#xe3ff;':'儿','&#xee49;':'衣','&#xf7ff;':'特','&#xe229;':'产','&#xf3a0;':'西','&#xe40c;':'批','&#xeadc;':'坊','&#xe964;':'州','&#xf07c;':'牛','&#xec70;':'佳','&#xf853;':'化','&#xe11c;':'五','&#xf749;':'米','&#xf6f7;':'修','&#xe93a;':'爱','&#xf23d;':'北','&#xecae;':'养','&#xe6a8;':'卖','&#xf4de;':'建','&#xe4ed;':'材','&#xf28e;':'三','&#xf7b4;':'会','&#xeb1a;':'鸡','&#xf08d;':'室','&#xf39d;':'红','&#xe122;':'站','&#xef57;':'德','&#xe914;':'王','&#xec4d;':'光','&#xe854;':'名','&#xec65;':'丽','&#xee40;':'油','&#xe642;':'院','&#xe8b5;':'堂','&#xe495;':'烧','&#xe32d;':'江','&#xe90d;':'社','&#xe038;':'合','&#xf354;':'星','&#xee75;':'货','&#xee86;':'型','&#xecfb;':'村','&#xf3a7;':'自','&#xead9;':'科','&#xe532;':'快','&#xe0b2;':'便','&#xe073;':'日','&#xf535;':'民','&#xf4bd;':'营','&#xe0c5;':'和','&#xf5ae;':'活','&#xf192;':'童','&#xea35;':'阴','&#xf103;':'器','&#xf731;':'烟','&#xe72c;':'盲','&#xee2e;':'宾','&#xe44e;':'精','&#xf34b;':'屋','&#xf221;':'经','&#xe1ab;':'居','&#xf597;':'庄','&#xea99;':'石','&#xeb03;':'顺','&#xe37b;':'林','&#xefff;':'尔','&#xe0c6;':'县','&#xf501;':'手','&#xe98a;':'厅','&#xecbb;':'销','&#xf151;':'用','&#xf551;':'好','&#xf056;':'害','&#xf71f;':'火','&#xf3e6;':'雅','&#xf287;':'盛','&#xf1d1;':'体','&#xe1cd;':'旅','&#xe86f;':'之','&#xf308;':'鞋','&#xf3bf;':'辣','&#xe886;':'作','&#xe158;':'粉','&#xe864;':'包','&#xec1f;':'楼','&#xe050;':'校','&#xe30a;':'鱼','&#xf2e1;':'平','&#xe90f;':'彩','&#xe689;':'上','&#xe89d;':'吧','&#xe72f;':'保','&#xea31;':'永','&#xee09;':'万','&#xf4da;':'物','&#xe1fb;':'教','&#xf09c;':'屹','&#xf0db;':'设','&#xe83a;':'医','&#xf2b5;':'正','&#xf250;':'造','&#xf591;':'丰','&#xebd3;':'健','&#xe456;':'点','&#xe9f4;':'汤','&#xe8ce;':'网','&#xef2a;':'庆','&#xebf1;':'技','&#xe2e0;':'斯','&#xee79;':'洗','&#xebce;':'料','&#xedaa;':'配','&#xe64d;':'汇','&#xe570;':'木','&#xe608;':'缘','&#xee78;':'加','&#xeecd;':'麻','&#xecfd;':'联','&#xefce;':'卫','&#xe53e;':'川','&#xe71e;':'泰','&#xe20b;':'色','&#xf81f;':'世','&#xf377;':'方','&#xf5f9;':'寓','&#xf745;':'风','&#xf02a;':'幼','&#xeb0b;':'羊','&#xf2dc;':'烫','&#xf66a;':'来','&#xf7ba;':'高','&#xf7cd;':'厂','&#xee3c;':'兰','&#xf509;':'阿','&#xf690;':'贝','&#xe2e5;':'皮','&#xf664;':'全','&#xeaea;':'女','&#xf0be;':'拉','&#xeda2;':'成','&#xf863;':'云','&#xf356;':'维','&#xecf3;':'贸','&#xf633;':'道','&#xe305;':'术','&#xef52;':'运','&#xe8c6;':'都','&#xe646;':'口','&#xe9bb;':'博','&#xe8f3;':'河','&#xeca7;':'瑞','&#xe43b;':'宏','&#xf2fc;':'京','&#xf1be;':'际','&#xf019;':'路','&#xf2e0;':'祥','&#xf376;':'胃','&#xee20;':'镇','&#xf357;':'厨','&#xe75f;':'培','&#xef3e;':'力','&#xf385;':'惠','&#xf7b7;':'连','&#xe702;':'马','&#xe5be;':'鸿','&#xf3b8;':'钢','&#xebab;':'训','&#xf294;':'影','&#xeb00;':'甲','&#xf679;':'助','&#xebc8;':'窗','&#xea2a;':'布','&#xee4b;':'富','&#xecc9;':'牌','&#xe84f;':'头','&#xf212;':'四','&#xf558;':'多','&#xf567;':'妆','&#xecf2;':'吉','&#xed89;':'苑','&#xe7a6;':'沙','&#xe518;':'恒','&#xf523;':'隆','&#xe573;':'春','&#xe380;':'干','&#xf274;':'饼','&#xf09d;':'氏','&#xe1dc;':'里','&#xe7df;':'二','&#xf739;':'管','&#xf5ab;':'诚','&#xe7a1;':'制','&#xe2be;':'售','&#xeaeb;':'嘉','&#xed5a;':'长','&#xf689;':'轩','&#xea8a;':'杂','&#xe817;':'副','&#xe1f4;':'清','&#xf6b0;':'计','&#xef47;':'黄','&#xeb12;':'讯','&#xf613;':'太','&#xe711;':'鸭','&#xe70e;':'号','&#xe423;':'街','&#xe565;':'交','&#xf1c1;':'与','&#xe35a;':'叉','&#xe9d4;':'附','&#xea55;':'近','&#xf89b;':'层','&#xf329;':'旁','&#xe7d0;':'对','&#xe58d;':'巷','&#xeb90;':'栋','&#xe015;':'环','&#xed5c;':'省','&#xee29;':'桥','&#xe226;':'湖','&#xf72a;':'段','&#xe2cc;':'乡','&#xee90;':'厦','&#xf1ff;':'府','&#xf5fa;':'铺','&#xf286;':'内','&#xebd5;':'侧','&#xf461;':'元','&#xe581;':'购','&#xf1b5;':'前','&#xe436;':'幢','&#xf561;':'滨','&#xe65e;':'处','&#xe833;':'向','&#xf328;':'座','&#xf032;':'下','&#xef93;':'禀','&#xeabc;':'凤','&#xf3f9;':'港','&#xeff2;':'开','&#xe277;':'关','&#xf0e3;':'景','&#xe098;':'泉','&#xefb1;':'塘','&#xf59c;':'放','&#xe5bd;':'昌','&#xf659;':'线','&#xefcd;':'湾','&#xeec7;':'政','&#xeee3;':'步','&#xe616;':'宁','&#xf179;':'解','&#xf68b;':'白','&#xe28c;':'田','&#xea67;':'町','&#xe025;':'溪','&#xebcd;':'十','&#xe32f;':'八','&#xeef0;':'古','&#xe6ec;':'双','&#xf24d;':'胜','&#xe3c1;':'本','&#xeb1d;':'单','&#xf0fc;':'同','&#xeab8;':'九','&#xef9a;':'迎','&#xe005;':'第','&#xf8b7;':'台','&#xe7e4;':'玉','&#xe95c;':'锦','&#xedfe;':'底','&#xf55a;':'后','&#xe809;':'七','&#xefd2;':'斜','&#xf484;':'期','&#xf306;':'武','&#xf642;':'岭','&#xedd9;':'松','&#xf55c;':'角','&#xf0ee;':'纪','&#xec39;':'朝','&#xf44f;':'峄','&#xe0bb;':'六','&#xe983;':'振','&#xeeff;':'珠','&#xe1b0;':'局','&#xf0f3;':'岗','&#xf0ad;':'洲','&#xed78;':'横','&#xe066;':'边','&#xe6d1;':'济','&#xf5d6;':'井','&#xe653;':'办','&#xef6a;':'汉','&#xe614;':'代','&#xf55b;':'临','&#xe036;':'弄','&#xe9d8;':'团','&#xf1b1;':'外','&#xf573;':'塔','&#xec5c;':'杨','&#xe481;':'铁','&#xe76d;':'浦','&#xf59e;':'字','&#xec15;':'年','&#xf374;':'岛','&#xf76f;':'陵','&#xe848;':'原','&#xe5ea;':'梅','&#xe600;':'进','&#xec31;':'荣','&#xf80c;':'友','&#xf2c8;':'虹','&#xf157;':'央','&#xeb5a;':'桂','&#xf3d5;':'沿','&#xea22;':'事','&#xed2c;':'津','&#xef2f;':'凯','&#xeb84;':'莲','&#xedec;':'丁','&#xe8fe;':'秀','&#xe33d;':'柳','&#xe037;':'集','&#xe6e1;':'紫','&#xee73;':'旗','&#xf081;':'张','&#xf3ae;':'谷','&#xe930;':'的','&#xf24e;':'是','&#xeddf;':'不','&#xed0c;':'了','&#xe054;':'很','&#xf1e5;':'还','&#xe825;':'个','&#xe02f;':'也','&#xe37e;':'这','&#xf7a5;':'我','&#xed83;':'就','&#xeca6;':'在','&#xf0f2;':'以','&#xefd5;':'可','&#xf85a;':'到','&#xe528;':'错','&#xec0a;':'没','&#xe490;':'去','&#xf786;':'过','&#xef3d;':'感','&#xf3dc;':'次','&#xe236;':'耍','&#xe5fc;':'比','&#xef4f;':'觉','&#xf4ba;':'看','&#xf8d5;':'得','&#xe4b3;':'说','&#xf4cd;':'常','&#xed02;':'真','&#xf025;':'们','&#xf759;':'但','&#xe88c;':'最','&#xed73;':'善','&#xe843;':'眙','&#xf7c4;':'么','&#xe564;':'别','&#xe1e4;':'位','&#xf61a;':'能','&#xf8c2;':'较','&#xea25;':'境','&#xf7c8;':'非','&#xeab7;':'为','&#xe969;':'欢','&#xf0cd;':'然','&#xebb9;':'他','&#xf7fe;':'挺','&#xe37d;':'着','&#xeb05;':'价','&#xe46b;':'那','&#xf115;':'意','&#xeeb7;':'种','&#xe970;':'想','&#xf29a;':'出','&#xea6a;':'员','&#xeee2;':'两','&#xe140;':'推','&#xe6bf;':'做','&#xf70f;':'排','&#xf470;':'实','&#xe1c2;':'分','&#xe1cb;':'间','&#xe059;':'甜','&#xf575;':'度','&#xf56b;':'起','&#xe9fd;':'满','&#xeabb;':'给','&#xf1bb;':'热','&#xe42a;':'完','&#xe7da;':'格','&#xe132;':'荐','&#xf887;':'蝎','&#xe1a1;':'等','&#xe552;':'其','&#xe892;':'再','&#xedcf;':'几','&#xf857;':'只','&#xf23f;':'现','&#xe01a;':'朋','&#xf0cb;':'候','&#xe86d;':'样','&#xe8d5;':'直','&#xf488;':'而','&#xf557;':'买','&#xf8e5;':'于','&#xebfe;':'般','&#xe452;':'豆','&#xe678;':'量','&#xf038;':'选','&#xe6f7;':'奶','&#xf8ab;':'打','&#xf436;':'每','&#xe62e;':'评','&#xed6d;':'少','&#xe478;':'算','&#xf7ab;':'又','&#xed0a;':'因','&#xf643;':'情','&#xf4a3;':'找','&#xf04d;':'些','&#xf6ec;':'份','&#xece0;':'置','&#xe321;':'适','&#xe729;':'什','&#xf2f8;':'蛋','&#xe7cd;':'师','&#xe81d;':'气','&#xe617;':'你','&#xf6aa;':'姐','&#xee9b;':'棒','&#xf2e2;':'试','&#xe13c;':'总','&#xec2c;':'定','&#xee35;':'峒','&#xe44a;':'足','&#xe525;':'级','&#xed80;':'整','&#xe292;':'带','&#xf347;':'虾','&#xec97;':'如','&#xe752;':'态','&#xe938;':'且','&#xe323;':'尝','&#xee19;':'主','&#xe792;':'话','&#xeb11;':'强','&#xf69d;':'当','&#xed5f;':'更','&#xe203;':'板','&#xf2c4;':'知','&#xed96;':'己','&#xf1c0;':'无','&#xe0b8;':'酸','&#xf048;':'让','&#xf03e;':'入','&#xf0f4;':'啦','&#xeafd;':'式','&#xe6b3;':'笑','&#xf291;':'赞','&#xf42e;':'片','&#xeb88;':'酱','&#xe66e;':'差','&#xe594;':'像','&#xead6;':'提','&#xe86a;':'队','&#xefc4;':'走','&#xee85;':'嫩','&#xe9e9;':'才','&#xf3d1;':'刚','&#xe2e1;':'午','&#xe7e1;':'接','&#xf4f0;':'重','&#xebd8;':'串','&#xe73d;':'回','&#xe099;':'晚','&#xed70;':'微','&#xf576;':'周','&#xe43f;':'值','&#xe041;':'费','&#xf5ad;':'性','&#xf28a;':'桌','&#xf016;':'拍','&#xead7;':'跟','&#xe5ab;':'块','&#xe6a2;':'调','&#xe915;':'糕',}

# 代理ip
proxys = ["111.11.100.13:8060","45.221.77.82:8080","112.109.198.106:3128","60.9.1.80:80","47.106.216.42:8000","116.196.115.209:8080"]
#1.使用python random模块的choice方法随机选择某个元素
proxy = choice(proxys)

proxy_d = "http://"+proxy

proxies = {
	"http":proxy_d
}

# 实例化代理对象
ops = Options()

# 随机产生User-Agent
User_Agent = UserAgent()
ua = User_Agent.random

# 拿加密需要的cookie
cookie =  "cy=1; cye=shanghai; _lxsdk_cuid=16c8b100f19c8-01cbe648f3d2a6-5f123917-1fa400-16c8b100f1ac8; _lxsdk=16c8b100f19c8-01cbe648f3d2a6-5f123917-1fa400-16c8b100f1ac8; _hc.v=ae79baa6-5372-4d49-e7e4-4f6b7f976e59.1565701181; s_ViewType=10; _dp.ac.v=27965664-c25d-4923-9e12-c959c90a9088; dper=b20ed38bbb26c76c38c315d5334fc1df1b5863b887494c52e605081861bece046904a5993165e68711f96f6820586e8688779401c12caffdc8e2a7147edc197783f9b2082d2044257b8763523091c1603c077cf6824e44ee58421a340cc18cab; ua=dpuser_4772089894; ctu=6ac4f4c6008f8ac7384c56fdb83150b3e832354ecc039485a11330efea317474; ll=7fd06e815b796be3df069dec7836c3df; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; _lxsdk_s=16c950a1014-669-878-ba2%7C%7C57",


def select_css(count,data,css,title):
	if count == 1:
		return data.select(css)
	if count == 2:
		return data.select(css)[0].getText().strip()
	if count == 3:
		return data.select(css)[0].get(title)


def data_(driver):
	time.sleep(10)
	html = driver.page_source 
	data = str(pq(html))  
	data = BeautifulSoup(data,"lxml")
	data.encoding = 'utf-8'
	return data



# 拿到加密地址电话
def address_phone(shop_id):

	headers = {
		"Accept": "application/json, text/javascript, */*; q=0.01",
		"Accept-Encoding": "gzip, deflate",
		"Accept-Language": "zh-CN,zh;q=0.9",
		"Connection": "keep-alive",
		"cookie": cookie,
		"Host": "www.dianping.com",
		"Referer": "http://www.dianping.com/shop/"+shop_id,
		"User-Agent": ua,
		"X-Requested-With": "XMLHttpRequest",
	}

	url="http://www.dianping.com/ajax/json/shopDynamic/basicHideInfo?shopId="+shop_id
	rs = requests.get(url,headers=headers,proxies=proxies,verify=False)
	print(rs)
	rs.encoding = 'utf-8'
	data = json.loads(rs.text)
	# 地址
	data_address = data["msg"]["shopInfo"]["address"]
	# 电话
	data_phone_one = data["msg"]["shopInfo"]["phoneNo"]
	data_phone_two = data["msg"]["shopInfo"]["phoneNo2"]

	# res = re.compile(r"<.*?>(.*?)<.*?>")
	# i = 0
	# for x in data_address.split("<"):
	# 	# print(x)
	# 	for y in x.split(">"):
	# 		if i == 0 or i%2 == 0:
	# 			print(y)
	# 		i = i+1
	# list_y = re.findall(res, data_address)

	print("地址::"+data_address)
	print("电话1::"+data_phone_one)
	print("电话2::"+data_phone_two)



def by_list(data,driver,url_one,shop_id):
	# 店名
	css_img = "#aside-photos > div > a > img"
	if len(select_css(1,data,css_img,"")) > 0:

		css = "#basic-info > h1"
		name = select_css(2,data,css,"")
		print("店名:::"+name.split("手机")[0])
		# 店家图片连接
		img = select_css(3,data,css_img,"src")
		print("店家图片连接:::"+img)

		address_phone(shop_id)

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

				# 点击跳转网页
				css = "#sales > div:nth-child(2) > div:nth-child("+str(x)+") > a"			
				driver.find_element_by_css_selector(css).click()
				d_data = data_(driver)
				# print(d_data)
				css = "#tab_show_1 > div:nth-child(4)"
				p_list = select_css(1,d_data,css,"")
				if len(p_list) > 0:
					# 团购详情
					tuan_text = select_css(2,d_data,css,"")
					print("团购详情::"+tuan_text)

				css = "#tab_show_6 > div > div > dl"
				gm_list = select_css(1,data,css,"")
				if len(gm_list) > 0:
					for z in range(1,len(gm_list)+1):
						# 购买须知
						css = "#tab_show_6 > div > div > dl:nth-child("+str(z)+") > dt"
						gm_name = select_css(2,data,css,"")
						print("须知名::"+gm_name)
						# 须知正文
						css = "#tab_show_6 > div > div > dl:nth-child("+str(z)+") > dd > p"
						gm_text = select_css(2,data,css,"")
						print("须知正文::"+gm_text)


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


	else:
		os.system("python che_quest.py")


def by_dp_baoyang_data(url_one,shop_id):

	# print('--proxy-server=http://%s' % proxy)
	ops.add_argument('--user-agent=%s' % ua)
	# ops.add_argument('--user-data-dir=C:/Users/Administrator/AppData/Local/Google/Chrome/User Data')
	ops.add_argument('--proxy-server=http://%s' % proxy)
	driver = webdriver.Chrome(chrome_options=ops)
	# driver = webdriver.Chrome(options=option)
	# driver = webdriver.Chrome()
	driver.get(url_one)
	data = data_(driver)

	by_list(data,driver,url_one,shop_id)


url = ["http://www.dianping.com/shop/110283404"]


for url_one in url:
	shop_id = url_one.split("/")[-1]
	by_dp_baoyang_data(url_one,shop_id)	
