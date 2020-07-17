#!/usr/bin/env python3
import numpy as np
import h5py

def readKeys(content, file):
    try:
        for key in file.keys():
            content.append(file[key].name)
            subfile=file.get(file[key].name)
            readKeys(content,subfile)
    except AttributeError as e:
        pass
