# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 09:05:48 2019
https://stackoverflow.com/questions/36238478/plotting-a-stacked-histogram-with-pandas-with-group-by
@author: hfuji
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

np.random.seed(10)
df = pd.DataFrame({"Gender":np.random.choice(["Female", "Male"], 1000), 
                "Height": 30+np.random.randn(1000)*5,
                "Width": 5+np.random.randn(1000)})
df.loc[df["Gender"]=="Male", "Height"] = df.loc[df["Gender"]=="Male", "Height"] + 8

plt.hist(df[df["Gender"]=="Male"]["Height"].reset_index(drop=True), alpha=0.6, label="Male")
plt.hist(df[df["Gender"]=="Female"]["Height"].reset_index(drop=True), alpha=0.6, label="Female")
plt.legend()
plt.show()