from aip import AipOcr
def image_recognition():
    # 百度图片识别文档地址：https://cloud.baidu.com/doc/OCR/s/Rjwvxzm3n/
    # 使用代码时需要在：https://console.bce.baidu.com/ai/?_=1569201737678#/ai/ocr/overview/index 创建一个应用
    APP_ID = 'xxx' # 应用的AppID
    API_KEY = 'xxxxx' # API Key
    SECRET_KEY = 'xxxxxxxxx' Secret Key
    client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
    img_path = '/home/ubuntu/桌面/timg.jpg' # 图片路径
    with open(img_path, 'rb') as f:
        image = f.read()
        text = client.basicAccurate(image) # 通用文字识别（高精度版）
        return text

text = image_recognition() # 返回值是一个字典
words = text['words_result']
for word in words:
    print(word['words'], end=' ')
