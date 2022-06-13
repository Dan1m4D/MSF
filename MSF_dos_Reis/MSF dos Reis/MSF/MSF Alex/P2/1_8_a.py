# -*- coding: utf-8 -*-
"""
Created on Sat Mar 26 21:33:15 2022

@author: Alexandre
"""

import matplotlib.pyplot as plt
import numpy as np

T = np.array([200.0, 300.0, 400.0, 500.0, 600.0, 700.0, 800.0, 900.0, 1000.0, 1100.0])
E = np.array([0.6950, 4.363, 15.53, 38.74, 75.08, 125.2, 257.9, 344.1, 557.4, 690.7])


## a)
plt.scatter(T,E)
plt.xlabel("T /(K)")
plt.ylabel("E /(J)")