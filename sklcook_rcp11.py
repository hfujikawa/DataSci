# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 10:40:51 2019

@author: hfuji
"""

from sklearn import preprocessing
from sklearn import datasets
#import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# datasets.load_*?
boston = datasets.load_boston()
X, y = boston.data, boston.target
print(X[:, :3].mean(axis=0))
print(X[:, :3].std(axis=0))

X_2 = preprocessing.scale(X[:, :3])
print(X_2.mean(axis=0))
print(X_2.std(axis=0))

pd.Series(X[:, 2]).hist(bins=50)
plt.show()
pd.Series(preprocessing.scale(X[:, 2])).hist(bins=50)
plt.show()

std_scaler = preprocessing.StandardScaler()
std_scaler.fit(X[:, :3])
print(std_scaler.transform(X[:, :3]).mean(axis=0))

mm_scaler = preprocessing.MinMaxScaler()
mm_scaler.fit(X[:, :3])
print(mm_scaler.transform(X[:, :3]).max(axis=0))
print(mm_scaler.transform(X[:, :3]).min(axis=0))

odd_scaler = preprocessing.MinMaxScaler(feature_range=(-3.14, 3.14))
odd_scaler.fit(X[:, :3])
print(odd_scaler.transform(X[:, :3]).max(axis=0))
print(odd_scaler.transform(X[:, :3]).min(axis=0))

norm_X =preprocessing.normalize(X[:, :3])
print((norm_X * norm_X).sum(axis=1))


df_X = pd.DataFrame.from_records(X)
plt.hist(df_X[3].reset_index(drop=True), alpha=0.6, label="0")
plt.show()
