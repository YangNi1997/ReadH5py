#!/usr/bin/env python3
import numpy as np
import h5py

content=[]
hf=h5py.File('/home/ni/ReadData/c_H_in_CH2.h5','r')
for key in hf.keys():
    content.append(hf[key].name)
    subf=hf.get(key)
    print(hf[key].name)
    for key in subf.keys():
        content.append(subf[key].name)
        #print(subf[key].name)
        #print(subf[key].items())
        subff=hf.get(subf[key].name)
        for key in subff.keys():
            content.append(subff[key].name)
           #print(subff[key].name)
            #print(subff[key].items())
for var in content:
   print(var)
