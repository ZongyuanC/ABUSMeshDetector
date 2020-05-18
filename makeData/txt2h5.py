# Author :SiQi Chan
# -*- coding:utf8 -*-

# -*- coding: utf-8 -*-
'''
hdf5数据源
'''
import math
import numpy as np
import random
import re
import os
import h5py
import cv2

#图片的绝对路径路径
root_path = 'D:/PYcode/MachineLearning/venv/code/AndrewNg_DeepLearning/makeData/all_data/'
with open('all_data/all_data_list.txt','r') as f:
    lins = f.readlines()

num = len(lins)                              #数据长度

random.shuffle(lins)                         #把数据洗牌
imgAccu = 0
#图片输入
# #制作Data,造一个50*50*3*图片个数的矩阵
imgs = np.zeros([num , 3 , 50 ,50])
# 制作label,造一个10(每个图像的标签数)×图片个数的矩阵
labels = np.zeros([num , 1])
for i in range(num):
    line = lins[i]
    line = line.replace(" (","(")
    #使用正则表达式把串给分割开来，取第一个图片的名字  \s就是一个回车或者空格
    segment = re.split('\s+',line)
    #找到图片
    fileID = segment[0].replace("("," (")
    image = cv2.imread(os.path.join(root_path , fileID))
    #得到图片对应标签
    label = segment[1]
    #图片整形
    image = cv2.resize(image , (50,50))
    # #调整图片通道顺序为(num,50,50,3)
    image = image.transpose(2 , 0 , 1)
    #转类型,float32
    #把数据和标签分别存在imgs和labels中
    imgs[i , : , : , :] = image.astype(np.float32)
    labels[i,:] = label

# print(imgs.shape)
imgs = imgs.transpose(0,3,2,1)  #调整图像通道顺序为(3,50,50)
imgs = np.array(imgs)
labels = np.array(labels)
imgs = imgs.astype(np.uint8)
labels = labels.astype(np.uint8)

print(imgs.shape)
print(labels.shape)

train_data_x_index = list(tuple(range(round(num*0.8))))
test_data_x_index = list(tuple(range(round(num))))[round(num*0.8):]

train_data_x = imgs[train_data_x_index,:,:,:]
test_data_x = imgs[test_data_x_index,:,:,:]

train_data_y = labels[train_data_x_index,:]
test_data_y = labels[test_data_x_index,:]

print(train_data_x_index)
print(test_data_x_index)

print(train_data_x.shape)
print(train_data_y.shape)

print(test_data_x.shape)
print(test_data_y.shape)

if not os.path.exists('D:/PYcode/MachineLearning/venv/code/AndrewNg_DeepLearning/makeData/train.h5'):
    with h5py.File('D:/PYcode/MachineLearning/venv/code/AndrewNg_DeepLearning/makeData/train.h5') as train_file:
        train_file['data'] = train_data_x
        train_file['labels'] = train_data_y

if not os.path.exists('D:/PYcode/MachineLearning/venv/code/AndrewNg_DeepLearning/makeData/test.h5'):
    with h5py.File('D:/PYcode/MachineLearning/venv/code/AndrewNg_DeepLearning/makeData/test.h5') as test_file:
        test_file['data'] = test_data_x
        test_file['labels'] = test_data_y
# 创建HDF5文件
train_file = h5py.File('D:/PYcode/MachineLearning/venv/code/AndrewNg_DeepLearning/makeData/train.h5','w')
test_file = h5py.File('D:/PYcode/MachineLearning/venv/code/AndrewNg_DeepLearning/makeData/test.h5','w')
# 写入
train_file.create_dataset('train_set_x', data = train_data_x)
train_file.create_dataset('train_set_y', data = train_data_y)
test_file.create_dataset('test_set_x', data = test_data_x)
test_file.create_dataset('test_set_y', data = test_data_y)

train_file.close()
test_file.close()
