# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 19:42:38 2020
https://www.nysol.jp/nysol_python/dataset/randStock.html
@author: hfuji
"""

from datetime import datetime,timedelta
import os
import numpy as np
import pandas as pd

def mkData(oFile):
  np.random.seed(seed=32)
  startDate=datetime(2018, 6, 29)
  delta=timedelta(days=1)

  with open(oFile,"w") as fpw:
    fpw.write("num,val\n")
    for loop in range(100):
        num = loop
        val = 2 ** (num % 32)
        fpw.write("%d,%d\n"%(num, val))
    '''
#    fpw.write("id,date,o,h,l,c\n")
    fpw.write("id,date,o\n")
#    for id in range(1000,7000):
    for id in range(1000,1002):
#      period=int(np.random.normal(4600,2000))
      period=int(np.random.normal(4600,10))
      if period<1000:
        period=1000
      print("id",id,"period",period)
      date=startDate
#      c=np.random.randint(500,100000)
      c=np.random.randint(0,32)
      for days in range(period):
#        if c<10:
#          break
#        c=np.random.normal(1.00,0.02)*c
#        o=np.random.normal(1.00,0.02)*c
#        h=np.random.normal(1.04,0.02)*c
#        l=np.random.normal(0.96,0.02)*c
#        hh=max(c,o,h,l)
#        ll=min(c,o,h,l)
#        h=hh
#        l=ll
        o = 2 ** (c % 32)
        date=date-delta
#        fpw.write("%d,%s,%d,%d,%d,%d\n"%(id,date.strftime("%Y%m%d"),o,h,l,c))
        fpw.write("%d,%s,%d\n"%(id,date.strftime("%Y%m%d"),o))
    '''
os.system("mkdir -p DATA")
fpath = "./DATA/val_power.csv"
mkData(fpath)

df = pd.DataFrame()
df = pd.read_csv(fpath, dtype = {'num':'int', 'val':'int64'})
#df = df.astype(float)
#df = df.astype(int64)

max_val = df["val"].max()
print(max_val)
print(df.dtypes)
