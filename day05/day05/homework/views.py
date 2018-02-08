from django.shortcuts import render

# Create your views here.
def getVerifyCode(request):
    return None


import random

from PIL import Image, ImageDraw
from django.db import models


# Create your models here.


def getVerifyCode(request):
    size = (200, 100)
    red = random.randrange(0, 256)
    green = random.randrange(0, 256)
    blue = random.randrange(0, 256)
    background = (red, green, blue)
    # 画布
    image = Image.new("RGB", size, background)
    # 画笔
    imageDraw = ImageDraw.Draw(image, "RGB")
    # 导入字体
    from PIL import ImageFont
    imagefont = ImageFont.truetype(os.path.join(settings.BASE_DIR, r'static/fonts/ADOBEARABIC-BOLD.OTF'), 50)
    # 绘制
    RAND = "abcdefghijklmnopqrstuvwxyzQWERTYUIOPASDFGHJKLZXCVBNM1234567890"
    msg = ""

    for i in range(0, 4):
        num = random.randrange(0, len(RAND))
        msg += RAND[num]

    request.session["verifycode"] = msg

    for i in range(0, 4):
        red = random.randrange(0, 256)
        green = random.randrange(0, 256)
        blue = random.randrange(0, 256)
        background = (red, green, blue)
        imageDraw.text((18 + 50 * i, 20), msg[i], font=imagefont, fill=background)

    for i in range(0, 2000):
        x = random.randrange(0, 200)
        y = random.randrange(0, 100)
        red = random.randrange(0, 256)
        green = random.randrange(0, 256)
        blue = random.randrange(0, 256)
        background = (red, green, blue)
        imageDraw.point((x, y), fill=background)

    # bytes 流，支持输入输出， 内存流
    bytesio = BytesIO()
    # 将image输出到内存流中
    image.save(bytesio, "png")
    # 指定返回类型       从内存流中获取数据
    return HttpResponse(bytesio.getvalue(), content_type="image/png")


def doLogin(request):
    verifycode = request.POST.get("verifycode")
    username = request.POST.get("username")
    print(verifycode)
    print(username)
    getcode = request.session.get("verifycode")
    if getcode != verifycode:
        return HttpResponse("验证失败啦！哈哈")
    return HttpResponse("验证成功")


def login(request):
    return render(request, 'login.html')