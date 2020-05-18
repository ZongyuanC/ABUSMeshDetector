# Author :SiQi Chan
# -*- coding:utf8 -*-
import cv2
from PIL import Image
import os
import numpy as np

# img = cv2.imread('img.png',0)

def horizontal(img):
    rst = img.transpose(Image.FLIP_LEFT_RIGHT)
    return rst


raw_img_path = 'D:\\PYcode\\MachineLearning\\venv\\code\\AndrewNg_DeepLearning\\compressImg\\rstimg\\'
save_img_path = 'D:\\PYcode\\MachineLearning\\venv\\code\\AndrewNg_DeepLearning\\compressImg\\rstimg\\'

# 遍历某文件夹下所有文件名，包括子文件夹下的文件名
def rotate_imagine(raw_img_path, save_img_path):
    now_file_path = raw_img_path
    for dirpath, dirnames, filenames in os.walk(now_file_path):
        for filename in filenames:
            file_path = now_file_path + filename
            img = Image.open(file_path)
            # img = img.convert("1")  ##转为灰度图

            rst = img.transpose(Image.FLIP_LEFT_RIGHT)
            fileName = os.path.splitext(filename)[0]  # 分割，不带后缀名
            save_file_path = os.path.join(save_img_path + fileName + '_' + str(0))
            # cv2.imwrite(save_file_path, np.array(rst))
            rst.save(save_file_path + '.jpg', 'JPEG', quality=100)

'''
    调用
'''
rotate_imagine(raw_img_path,save_img_path)