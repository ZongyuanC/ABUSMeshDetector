# Author :SiQi Chan
# -*- coding:utf8 -*-

from xml.dom.minidom import parse
import os
def readXML(file):
    domTree = parse("Annotations/"+file)
    # 文档根元素
    rootNode = domTree.documentElement
    print('rootName:',rootNode.nodeName)
    filename = rootNode.getElementsByTagName('filename')[0]
    print(filename.childNodes[0].data)
    filename1 = filename.childNodes[0].data
    print(type(filename1))
    # new_filename = filename1.replace('.png','')
    filenamelist = filename1.split('.')
    new_filename = filenamelist[0]+'.jpg'
    print(new_filename)
    filename.childNodes[0].data = new_filename#更新名字

    path = rootNode.getElementsByTagName('path')[0]
    path1 = path.childNodes[0].data
    # new_path = path1.replace('.png','')
    pathlist = path1.split('.')
    new_path = pathlist[0]+'.jpg'
    print(new_path)
    path.childNodes[0].data = new_path  # 更新名字
    '''
        保存
    '''
    new_file = file.replace('.png','')
    with open("Annotation/"+new_file, 'w') as f:
        # 缩进 - 换行 - 编码
        domTree.writexml(f, addindent='  ', encoding='utf-8')
if __name__ == '__main__':
    xmlfilepath = "Annotations/"
    filelist = total_xml = os.listdir(xmlfilepath)
    print(filelist)
    for file in filelist:
        readXML(file)




# if __name__ == '__main__':
#     inputpath = 'D:\\PYcode\\MachineLearning\\venv\\code\\AndrewNg_DeepLearning\\week12_Voc\\keras-yolo3-master\\VOCdevkit\\VOC2020\\Annotations\\'
#     updateXML()