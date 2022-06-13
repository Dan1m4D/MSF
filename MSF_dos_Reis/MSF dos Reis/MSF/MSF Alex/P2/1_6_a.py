# -*- coding: utf-8 -*-
"""
Created on Sat Mar 26 19:04:15 2022

@author: Alexandre
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

y = np.array([0.00, 0.735, 1.363, 1.739, 2.805, 3.814, 4.458, 4.955, 5.666, 6.329])
x = np.linspace(0,9,len(y))

reg = stats.linregress(x,y) 

plt.plot(x, y, "o", label = "Original data")
plt.plot(x, reg.intercept + reg.slope*x, "r", label="Regression line")
plt.xlabel("t(min)")
plt.ylabel("d(km)")
plt.legend()
plt.show()