import numpy as np
import re

def save_as(string, z):
    np.savetxt(string, z)
    return 0

def save_head_as(string, dic):
    savebuff = []
    for key in list(dic):
        tem = [key, dic[key]]
        savebuff.append(tem)
    np.savetxt(string, savebuff, fmt = '%s')
    return 0

def save_vol_as(string, vol):
    # tem = [vol] 
    split_str = '(C+[0-9]+[0-9]|C+[ ]+[0-9])'
    retem = re.split(split_str, vol)
    np.savetxt(string, retem, fmt = '%s')
    return 0