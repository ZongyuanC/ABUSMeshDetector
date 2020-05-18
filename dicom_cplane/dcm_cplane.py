# Author :SiQi Chan
# -*- coding:utf8 -*-
import os
import pydicom
import numpy as np
import SimpleITK
import matplotlib.pyplot as plt
import matplotlib
import scipy
import datetime
# 用lstFilesDCM作为存放DICOM files的列表
PathDicom = "./DicomResource/"  # 与python文件同一个目录下的文件夹
lstFilesDCM = []

for dirName, subdirList, fileList in os.walk(PathDicom):
    for filename in fileList:
        if ".dcm" in filename.lower():  # 判断文件是否为dicom文件
            print(filename)
            lstFilesDCM.append(os.path.join(dirName, filename))  # 加入到列表中
print('fileList',fileList)
## 将第一张图片作为参考图
# RefDs = pydicom.read_file(lstFilesDCM[0])  # 读取第一张dicom图片
# # print(RefDs)
# print(RefDs.pixel_array.shape)
# print(lstFilesDCM)
# # 建立三维数组
# ConstPixelDims = (int(RefDs.Rows), int(RefDs.Columns), int(RefDs.NumberOfFrames))
# print('RefDs.Rows',int(RefDs.Rows))
# print('RefDs.Cols',int(RefDs.Columns))
# print('RefDs.Lens',int(RefDs.NumberOfFrames))
# # 得到spacing值 (mm为单位)
# print('RefDs.PixelSpacingY',float(RefDs.PixelSpacing[0]))
# print('RefDs.PixelSpacingX',float(RefDs.PixelSpacing[1]))
# print('RefDs.SliceThickness',float(RefDs.SpacingBetweenSlices))
# ConstPixelSpacing = (float(RefDs.PixelSpacing[0]), float(RefDs.PixelSpacing[1]), float(RefDs.SpacingBetweenSlices))
#
# # 三维数据
# y = np.arange(0.0, (ConstPixelDims[0] + 1) * ConstPixelSpacing[0],
#                  ConstPixelSpacing[0])  # 0到（第一个维数加一*像素间的间隔），步长为constpixelSpacing
# x = np.arange(0.0, (ConstPixelDims[1] + 1) * ConstPixelSpacing[1], ConstPixelSpacing[1])  #
# z = np.arange(0.0, (ConstPixelDims[2] + 1) * ConstPixelSpacing[2], ConstPixelSpacing[2])  #
#
# ArrayDicom = np.zeros(ConstPixelDims, dtype=RefDs.pixel_array.dtype)
# print('ArrayDicom.size=',ArrayDicom.shape)


def createArray(filenameDCM):
    RefDs = pydicom.read_file(filenameDCM)  # 读取第一张dicom图片
    # print(RefDs)
    # print(RefDs.pixel_array.shape)
    # print(lstFilesDCM)
    # 建立三维数组
    ConstPixelDims = (int(RefDs.Rows), int(RefDs.Columns), int(RefDs.NumberOfFrames))
    # print('RefDs.Rows', int(RefDs.Rows))
    # print('RefDs.Cols', int(RefDs.Columns))
    # print('RefDs.Lens', int(RefDs.NumberOfFrames))
    ## 得到spacing值 (mm为单位)
    # print('RefDs.PixelSpacingY', float(RefDs.PixelSpacing[0]))
    # print('RefDs.PixelSpacingX', float(RefDs.PixelSpacing[1]))
    # print('RefDs.SliceThickness', float(RefDs.SpacingBetweenSlices))
    ConstPixelSpacing = (float(RefDs.PixelSpacing[0]), float(RefDs.PixelSpacing[1]), float(RefDs.SpacingBetweenSlices))
    print('ConstPixelSpacing',ConstPixelSpacing)
    ConstPixelSpacing = (round(ConstPixelSpacing[0],2),round(ConstPixelSpacing[1],2),round(ConstPixelSpacing[2],2))
    print('ConstPixelSpacing', ConstPixelSpacing)

    # 三维数据
    y = np.arange(0.0, (ConstPixelDims[0] ) * ConstPixelSpacing[0], ConstPixelSpacing[0])  # 0到（第一个维数加一*像素间的间隔），步长为constpixelSpacing
    x = np.arange(0.0, (ConstPixelDims[1] ) * ConstPixelSpacing[1], ConstPixelSpacing[1])  #
    z = np.arange(0.0, (ConstPixelDims[2] ) * ConstPixelSpacing[2], ConstPixelSpacing[2])  #

    ArrayDicom = np.zeros(ConstPixelDims, dtype=RefDs.pixel_array.dtype)
    print('ArrayDicom',ArrayDicom.shape)
    print('y,x,z',len(y),len(x),len(z))
    return ArrayDicom,RefDs,x,y,z
def mkdir(path):
    # 去除首位空格
    path = path.strip()
    # 去除尾部 \ 符号
    path = path.rstrip("\\")
    isExists = os.path.exists(path)
    # 判断结果
    if not isExists:
        os.makedirs(path)
        print(path + ' 创建成功')
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        return False

def Dcm2Cplane(ArrayDicom,index):
    startIndex = 0
    #将DICOM数据冠状面抽出，并保存
    for i in range(startIndex,ArrayDicom.shape[0]-100,3): #步长为3
    # for i in range(startIndex,ArrayDicom.shape[0],1): #测试没一例病人抽取C平面的时间为0.142秒
        currentSlice = ArrayDicom[i,:,:]
        print('currentSilice',currentSlice.shape)
        currentSlice = currentSlice.transpose()
        print('currentSilice', currentSlice.shape)
        filePath = 'G:\\DOCX\\GraduationProj\\img_data\\3Ddata\\bodymesh_test\\'+fileList[index]+'\\'
        if i == startIndex:
            mkdir(filePath)
            fig = plt.gcf()
            # fig.set_size_inches(int(x[-1]),int(z[-1]))
            fig.set_size_inches(int(x[-1]) / 32 * 5, int(z[-1]) / 32 * 5)  # 输出width*height像素
            plt.subplots_adjust(top=1, bottom=0, left=0, right=1, hspace=0, wspace=0)  # 输出图像#边框设置
            plt.margins(0, 0)
            plt.axes().set_aspect('equal', 'datalim')
            plt.axis('off')
            plt.set_cmap(plt.gray())
        # print('x',len(x))
        # print('z',len(z))
        # plt.figure(figsize=(int(x[-1]),int(z[-1])))
        plt.pcolormesh(x,z,currentSlice)
        plt.savefig(filePath+str(i)+'.jpg',dpi = 32,pad_inches = 0)
    return None


# 遍历所有的dicom文件，读取图像数据，存放在numpy数组中
startTime = datetime.datetime.now()
for filenameDCM in lstFilesDCM:
    # startTime = datetime.datetime.now()
    print(startTime)
    print('filenameDCM',filenameDCM)
    ArrayDicom,RefDs,x,y,z = createArray(filenameDCM)
    # ds = pydicom.read_file(filenameDCM)
    # print('ds.pexe_array.shape=', ds.pixel_array.shape)
    array = RefDs.pixel_array.swapaxes(0,1)
    array = array.swapaxes(1,2)
    # print('ds.pexe_array.shape=', array.shape)
    ArrayDicom = array
    index = lstFilesDCM.index(filenameDCM)
    Dcm2Cplane(ArrayDicom,index)
endTime = datetime.datetime.now()
print(endTime)
time = endTime - startTime

print('平均耗时',time/11)
# 冠状面显示
# fig = plt.gcf()
# # print('x',int(x[-1]))
# # print('z',int(z[-1]))
# fig.set_size_inches(int(x[-1]) / 32, int(z[-1]) /32)  # 输出width*height像素
# plt.subplots_adjust(top=1, bottom=0, left=0, right=1, hspace=0, wspace=0)  # 输出图像#边框设置
# plt.margins(0, 0)
# plt.axes().set_aspect('equal', 'datalim')
# plt.axis('off')
# plt.set_cmap(plt.gray())
# # print('第300层冠状面=', ArrayDicom[300,:,:].shape)
# # print('ArrayDicom.shape[0]=', ArrayDicom.shape[0])
# plt.pcolormesh(x, z, np.flipud(ArrayDicom[350, :, :]).transpose())  # 第三个维度表示现在展示的是第几层
# # matplotlib.image.imsave('a.jpg',ArrayDicom[550,:,:])
# plt.savefig('b.jpg',dpi=32,pad_inches = 0)
# plt.show()




# Dcm2Cplane(ArrayDicom)