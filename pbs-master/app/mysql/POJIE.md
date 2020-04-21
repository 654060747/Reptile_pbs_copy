## pojie.py
破解极验验证的滑块验证
```python
# 使用方法：
url = 'https://www.geetest.com/demo/slide-popup.html' # 出现滑动解锁的网站
left = 57  # 起始位置 # 一般不变
# 每个网站deviation值不同，根据网站调试
# deviation = 3  # 偏移量，误差
str_xpath = '//*[@id="captcha"]/div[3]/div[2]/div[1]/div[3]' # xpath匹配滑动解锁的div标签
Crack = CrackGeetest(url, proxy='http://xxx', str_xpath=str_xpath)
Crack.crack()
```

## baiduwzsb.py
图片文字识别

