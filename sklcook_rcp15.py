# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 10:40:51 2019

@author: hfuji
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression, TheilSenRegressor
from sklearn.metrics import r2_score, mean_absolute_error

num_points = 100
x_vals = np.arange(num_points)
y_truth = 2 * x_vals
plt.plot(x_vals, y_truth)

y_noisy = y_truth.copy()
y_noisy[20:40] = y_noisy[20:40] * (-4 * x_vals[20:40]) - 100
plt.title("Noise in y-direction")
plt.xlim([0,100])
plt.scatter(x_vals, y_noisy, marker='x')


named_estimators = [('OLS', LinearRegression()), ('TSR', TheilSenRegressor())]
for num_index, est in enumerate(named_estimators):
    y_pred = est[1].fit(x_vals.reshape(-1,1), y_noisy).predict(x_vals.reshape(-1,1))
    print(est[0], "R-squared: ", r2_score(y_truth, y_pred))
    plt.plot(x_vals, y_pred, label=est[0])
#    plt.show()
    
    plt.plot(x_vals, y_truth, label='True line')
    plt.legend(loc='upper left')
