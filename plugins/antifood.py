from nonebot import NLPSession, CommandSession, IntentCommand, on_natural_language, on_command
from urllib.request import urlretrieve
from utils.food_detect import isFood
from utils.get_image import getPic
import config

# 以暴制暴：从百度图片上拉一张食物图片怼回去
@on_command('send_food_back')
async def repeat_sign(session: CommandSession):
    getPic()
    returnPic = f'[CQ:image,file=send_back.png]'
    await session.send(returnPic)

# 如果对方发的消息中包含图片，则判断图片是否为食物图片
@on_natural_language(only_to_me = False)
async def _(session: NLPSession):
    if(session.msg_images != []):
        for image_path in session.msg_images:
            # 保存图片到本地
            urlretrieve(image_path, "qq_image.png")
            # 判断图片是否为食物图片
            if(isFood("qq_image.png") == True):
                return IntentCommand(100, 'send_food_back')