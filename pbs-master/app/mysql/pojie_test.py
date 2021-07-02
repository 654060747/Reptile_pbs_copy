import io
import time
from io import  BytesIO
from PIL import Image
import random, base64
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import cv2
from matplotlib import pyplot as plt
import numpy as np
from PIL import ImageOps



threshold = 60  # 验证码图片对比中RGB的差值，6
left = 50  # 验证码图片的对比中的起始坐标，即拖动模块的右边线位置
deviation = 7

def MovePictureToLocation(srcPath, objPath, match_res):
    im = Image.open(srcPath)
    im1 = Image.open(objPath)
    # im1.thumbnail((700, 100))
    im.paste(im1, match_res)
    im.show()

def get_distance(image1, image2):
    """
    拿到滑动验证码需要移动的距离
    :param image1: 没有缺口的图片对象
    :param image2: 带缺口的图片对象
    :return: 需要移动的距离
    """
    i = 0 # image1.size图片长宽
    for i in range(left, image1.size[0]):
        for j in range(image1.size[1]):
            rgb1 = image1.load()[i, j]
            rgb2 = image2.load()[i, j]
            res1 = abs(rgb1[0] - rgb2[0])
            res2 = abs(rgb1[1] - rgb2[1])
            res3 = abs(rgb1[2] - rgb2[2])
            res4 = abs(rgb1[3] - rgb2[3])
            # 如果rgb差值大于threshold，滑动的距离会等于i-误差
            if not (res1 < threshold and res2 < threshold and res3 < threshold and res4 < threshold):
                print('=============================')
                # distance = i - deviation
                distance = i
                return distance
    print('未识别出验证码中的不同位置，或图片定位出现异常')
    return i  # 如果没有识别出不同位置，则象征性的滑动，以刷新下一张验证码

def get_image():

    # 缺口图
    image_path = 'C:\\Users\\dell\\Desktop\\guigui\\qqqqqqqqqqqqqqqqqqqqqq.png'
    image_byte01 = Image.open(image_path).convert('RGBA')
    print(image_byte01)

    # 完整图
    # all_image = cv2.imread("C:\\Users\\dell\\Desktop\\guigui\\a.png", 1)
    # cv2.imwrite("C:\\Users\\dell\\Desktop\\guigui\\b.png", all_image)
    image_path = 'C:\\Users\\dell\\Desktop\\guigui\\wwwwwwwwwwwwwwwwwwwwwwww.png'
    image_byte02 = Image.open(image_path).convert('RGBA')
    print(image_byte02)
    return image_byte01, image_byte02

if __name__ == '__main__':
    image1, image2 = get_image()
    distance = get_distance(image1, image2)
    print('需要移动的距离：', distance)
    MovePictureToLocation('C:\\Users\\dell\\Desktop\\guigui\\qqqqqqqqqqqqqqqqqqqqqq.png','C:\\Users\\dell\\Desktop\\guigui\\wwwwwwwwwwwwwwwwwwwwwwww.png',(distance, 0))
