# Author :SiQi Chan
# -*- coding:utf8 -*-

# !/usr/bin/python
# -*- coding:utf-8 -*-

import os
def generate(dir, label):
    files = os.listdir(dir)
    files.sort()
    print('****************')
    print('input :', dir)
    print('start...')
    listText = open('all_data_list.txt', 'a')
    for file in files:
        fileType = os.path.split(file)
        if fileType[1] == '.txt':
            continue
        name = file + ' ' + str(int(label)) + '\n'
        listText.write(name)
    listText.close()
    print('down!')
    print('****************')

outer_path = 'G:/DOCX/GraduationProj/graduation_proj/data/data/cnn_sigmoid_data/'  # 这里是你的图片的目录//这个目录为包含了各类文件夹的父目录，决定各个分类的标签Y值
# outer_path = 'D:/PYcode/MachineLearning/venv/code/AndrewNg_DeepLearning/makeData/all_data/'  # 这里是你的图片的目录

if __name__ == '__main__':
    i = 0
    folderlist = os.listdir(outer_path)  # 列举文件夹
    for folder in folderlist:
        dir = os.path.join(outer_path, folder)
        generate( dir , i)
        i += 1


