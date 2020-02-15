#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 09:34:00 2020
https://teratail.com/questions/184798
@author: i2m
"""

import pandas as pd
import numpy as np

df1 = pd.DataFrame([[1,1,2],
                    [1,2,3]])  # この行がペアになる

df2 = pd.DataFrame([[1,2,4,5], # この行がペアになる
                    [2,3,3,3]])

# 先頭２列（タプルとして）のハッシュ値を得る
df1['hash'] = df1.apply(lambda r: hash((r[0],r[1])),axis=1)
df2['hash'] = df2.apply(lambda r: hash((r[0],r[1])),axis=1)

# ハッシュ値をインデックスとする
df1 = df1.set_index('hash',drop=True)
df2 = df2.set_index('hash',drop=True)

# インデックスで内部結合
# 重複列において右側はそのまま、左(M)側の重複列名には「_dup」を付加する
df = pd.merge(df1,df2,left_index=True,right_index=True, how='inner',suffixes=['_dup',''])

# 左(M)側の重複列は不要なので削除
for col in df.columns:
    if '_dup' in str(col):
        df = df.drop(str(col), axis=1)

df = df.reset_index(drop=True) # 通常のインデックスに戻す
print(df)
"""
   0  1  2  3
0  1  2  4  5
"""