'''
从百度图片上（按 config.py 中设置的关键词）随机爬取一张图片
'''

import re
import requests
from urllib import error
from urllib.request import urlretrieve
import random
import math
import config

def getPicList():
    baseURL = 'http://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word=' + config.keyword + '&pn='

    while True:
        pn = random.randint(0, math.ceil(config.randomTotol/60))
        pn *= 60

        try:
            url = baseURL + str(pn)
            result = requests.get(url, timeout = 10)
        except error.HTTPError as e:
            print('Network Error')
        else:
            picList = re.findall('"objURL":"(.*?)",', result.text, re.S)
            return picList


def getPic():
    
    picList = getPicList()

    while True:
        picID = random.randint(0, len(picList)-1)

        try:
            if picList[picID] is not None:
                pic = requests.get(picList[picID], timeout=7)
            else:
                continue
        except BaseException:
            print('Download Error')
            continue
        else:
            # 保存图片到本地
            save_path = config.COOLQ_IMAGE_PATH + 'send_back.png'
            urlretrieve(picList[picID], save_path)
            return