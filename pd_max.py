# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 19:42:38 2020
https://www.nysol.jp/nysol_python/dataset/randStock.html
@author: hfuji
"""

import os
import numpy as np
import pandas as pd

def mkData(oFile):
  np.random.seed(seed=32)

  with open(oFile,"w") as fpw:
    fpw.write("num,val\n")
    for loop in range(100):
        num = loop
        val = 2 ** (num % 32)
        fpw.write("%d,%d\n"%(num, val))

os.system("mkdir -p DATA")
fpath = "./DATA/val_power.csv"
mkData(fpath)

columns = ['num', 'val']
values = np.zeros(100, dtype='int32, int64')
values.dtype.names = columns
df2 = pd.DataFrame(values, columns=columns)


df = pd.DataFrame()
df = pd.read_csv(fpath, dtype = {'num':'int', 'val':'int64'})

max_val = df["val"].max()
print(max_val)
print(df.dtypes)
