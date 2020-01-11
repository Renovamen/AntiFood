# AntiFood

以暴制暴深夜放毒自动反击系统。

基于 [NoneBot](https://github.com/richardchien/nonebot) 的 QQ 机器人，用[百度云图像识别 API](https://cloud.baidu.com/product/imagerecognition) 识别别人发的图是否为放毒（食物）图片，如果是的话就在百度上随便爬一张食物图片怼回去，让对方也感受一下饥饿。（...）

&nbsp;
## Framework

- [NoneBot](https://github.com/richardchien/nonebot) ([Docs](https://nonebot.cqp.moe/))

- [CoolQ HTTP API](https://github.com/richardchien/coolq-http-api) ([Docs](https://cqhttp.cc/docs/4.13/#/))

- [酷 Q](https://cqp.cc/)

&nbsp;
## Config

在 `config.py` 中配置以下内容：

```python
# coolq
COOLQ_IMAGE_PATH = 'your_coolq_path/data/image/' # coolq 文件路径

# baidu image recognition api
# 申请 API: https://cloud.baidu.com/product/imagerecognition
# Docs: https://ai.baidu.com/ai-doc/IMAGERECOGNITION/vk3bcxiu2
# 在下面填入 AppID、API Key 和 Secret Key
appID = ''
apiKey = ''
secretKey = ''

# baidu image
keyword = '美食' # 百度图片搜索关键词
randomTotol = 100 # 在前多少张图片中随机拉取
```

&nbsp;

## Usage

```powershell
python bot.py
```