# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 17:12:00 2019
https://takazawa.github.io/hobby/pandas_append_fast/
@author: hfuji
"""

import pandas as pd
import time

df = pd.DataFrame()
df_add = pd.DataFrame([[1, 2, 3], [4, 5, 6]])

start = time.time()

#for i in range(10000):
#    df = df.append(df_add, ignore_index=True)

counter = 0
dict_tmp = {}

for i in range(10000):
    for _, row in df_add.iteritems():
        dict_tmp[counter] = row
        counter += 1
df = df.from_dict(dict_tmp, orient="index")

print('slapsed : ', time.time() - start)