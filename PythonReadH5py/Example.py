#!/usr/bin/env python3
import h5py
from ReadKeys import readKeys

file_content=[]
hf=h5py.File('/.../.../c_H_in_CH2.h5','r')
readKeys(file_content, hf)
for var in file_content:
    print(var)
