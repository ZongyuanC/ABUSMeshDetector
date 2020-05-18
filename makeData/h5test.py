# Author :SiQi Chan
# -*- coding:utf8 -*-
import h5py
import numpy as np
file = 'train.h5'
f = h5py.File(file,'r')
print(f.keys())

for key in f.keys():
    print(f[key].name)
    print(f[key].shape)
    print(np.array(f[key].value).transpose())