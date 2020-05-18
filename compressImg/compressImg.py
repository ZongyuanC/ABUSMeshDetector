# Author :SiQi Chan
# -*- coding:utf8 -*-
from PIL import Image
import os
import sys

in_dir = 'img'  # 存放待压缩图像的文件夹，需要自行按此设置的名字新建，并于代码在同一目录下
ou_dir = 'rstimg\\'  # 输出结果所在文件夹，程序会自动新建
quality = 60  # 设置压缩后质量, 应设置为 1(worst)-95(best)的数值

def load_images():
    if not os.path.exists(in_dir):
        print('请新建待压缩图像文件夹，并命名为：“Inputs”！')
        sys.exit(0)
    names = os.listdir(in_dir)
    return names

def Image_PreProcessing(names):
    for name in names:
        # 待处理图片存储路径
        im = Image.open(in_dir + '\\'+name)
        # Resize图片大小，入口参数为一个tuple，新的图片大小
        imBackground = im.resize((600, 660))
        # 处理后的图片的存储路径，以及存储格式
        imBackground.save(ou_dir + str(names.index(name))+'.jpg', 'JPEG',quality = 100)

if __name__ == "__main__":
    name_list = load_images()
    Image_PreProcessing(name_list)