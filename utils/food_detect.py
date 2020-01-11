'''
使用百度云图像识别 API，判断图片是否为食物图片
API: https://cloud.baidu.com/product/imagerecognition
Docs: https://ai.baidu.com/ai-doc/IMAGERECOGNITION/vk3bcxiu2
'''

from aip import AipImageClassify
import config

# 通用物体识别 API
def generalDetect(imagePath):
    client = AipImageClassify(config.appID, config.apiKey, config.secretKey)

    with open(imagePath, 'rb') as fp:
        image = fp.read()

    result = client.advancedGeneral(image)
    print(result)

    for item in result["result"]:
        print(item['root'], item['keyword'])
        if(item['root'].find('食物') > -1 or item['keyword'].find('食物') > -1):
            return True
    return False


# 菜品识别 API
def dishDetect(imagePath):
    client = AipImageClassify(config.appID, config.apiKey, config.secretKey)

    with open(imagePath, 'rb') as fp:
        image = fp.read()

    result = client.dishDetect(image)
    print(result)
    return result["result"][0]["has_calorie"]


# 判断是否为食物图片
def isFood(imagePath):
    if(dishDetect(imagePath) or generalDetect(imagePath)):
        return True
    else:
        return False