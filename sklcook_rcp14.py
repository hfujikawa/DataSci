# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 10:40:51 2019

@author: hfuji
"""

from sklearn import datasets
import numpy as np

# datasets.load_*?
iris = datasets.load_iris()
iris_X = iris.data
masking_array = np.random.binomial(1, .25, iris_X.shape).astype(bool)
iris_X[masking_array] = np.nan
