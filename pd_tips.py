# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 06:36:20 2019

@author: hfuji
"""

import pandas as pd

# https://stackoverflow.com/questions/34397982/pandas-dataframe-access-multiple-items-with-not-equal-to

dtypesDict1 = {'Train': 'O', 'Origin': 'O', 'DayOfWeek': 'int64'}
dtypesDict2 = {'Train': 'O', 'Origin': 'O', 'DayOfWeek': 'float'}

fpath = 'D:/Develop/DataSci/TableSample_withNaN.csv'

try:
    df = pd.read_csv(fpath, dtype=dtypesDict1)
except:
    df = pd.read_csv(fpath)
    print("num of NaN: ", df.isnull().sum())
    df_rm = df.dropna(how='any')
    print(df_rm.dtypes)
    df_rm = df_rm.astype(dtypesDict1)
    print(df_rm.dtypes)

#
#df1 = df[(df['Train'] != 'DeutscheBahn') & (df['Train'] != 'SNCF')]
#
#df2 = df.query("Train not in ['DeutscheBahn', 'British Rails', 'SNCF']")
#
#df3 = df[(df['DayofMonth'] == 2) & (df['DayOfWeek'] == 6)]
