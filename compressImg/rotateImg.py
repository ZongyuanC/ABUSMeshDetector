# Author :SiQi Chan
# -*- coding:utf8 -*-
import cv2
import os
import numpy as np

# img = cv2.imread('img.png',0)

def rotate90_180_270(img,index):
    rows, cols = img.shape

    # cols-1 and rows-1 are the coordinate limits.
    M = cv2.getRotationMatrix2D(((cols - 1) / 2.0, (rows - 1) / 2.0), -90*index, 1)
    rst = cv2.warpAffine(img, M, (cols, rows))

    # cv2.imwrite(os.path.join('img_'+str(index)+'.png'), rst, [int(cv2.IMWRITE_PNG_COMPRESSION), 0])
    return rst


raw_img_path = 'D:\\PYcode\\MachineLearning\\venv\\code\\AndrewNg_DeepLearning\\compressImg\\rstimg\\'
save_img_path = 'D:\\PYcode\\MachineLearning\\venv\\code\\AndrewNg_DeepLearning\\compressImg\\rstimg\\'

# 遍历某文件夹下所有文件名，包括子文件夹下的文件名
def rotate_imagine(raw_img_path, save_img_path):
    now_file_path = raw_img_path
    for dirpath, dirnames, filenames in os.walk(now_file_path):
        for filename in filenames:
            file_path = now_file_path + filename
            img = cv2.imread(file_path)
            img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)  ##转为灰度图
            # img_rotate = rotate_bound(img, angle)
            for i in range(1,4):
                rst = rotate90_180_270(img, i)
                fileName = os.path.splitext(filename)[0]  # 分割，不带后缀名
                save_file_path = os.path.join(save_img_path + fileName + '_' + str(i)+'.jpg')
                cv2.imwrite(save_file_path, rst)

'''
    调用
'''
rotate_imagine(raw_img_path,save_img_path)