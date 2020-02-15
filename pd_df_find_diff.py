#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 09:49:53 2020
https://stackoverflow.com/questions/48647534/python-pandas-find-difference-between-two-data-frames
@author: i2m
"""

import pandas as pd
# given
df1 = pd.DataFrame({'Name':['John','Mike','Smith','Wale','Marry','Tom','Menda','Bolt','Yuswa',],
    'Age':[23,45,12,34,27,44,28,39,40]})
df2 = pd.DataFrame({'Name':['John','Smith','Wale','Tom','Menda','Yuswa',],
    'Age':[23,12,34,44,28,40]})

# Method1
# find elements in df1 that are not in df2
df_1notin2 = df1[~(df1['Name'].isin(df2['Name']) & df1['Age'].isin(df2['Age']))].reset_index(drop=True)

# output:
print('df1\n', df1)
print('df2\n', df2)
print('df_1notin2\n', df_1notin2)

# Method 2: merge with indicator
df_out = df1.merge(df2,indicator = True, how='left').loc[lambda x : x['_merge']!='both']
print(df_out)

# Method3
df_join = pd.concat([df1,df2])
df_result = df_join.drop_duplicates(keep=False)
print(df_result)