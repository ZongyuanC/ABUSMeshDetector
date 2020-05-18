# Author :SiQi Chan
# -*- coding:utf8 -*-
import os
srcdir = 'JPEGImages/'
dstdir = 'JPEGImages1/'
# os.rename(src=srcdir,dst=dstdir)
filelist = os.listdir(srcdir)
print(filelist)
for file in filelist:
    newfile = file.replace('.png','')
    newsrcdir = srcdir + file
    newdstdir = dstdir + newfile
    os.rename(newsrcdir,newdstdir)