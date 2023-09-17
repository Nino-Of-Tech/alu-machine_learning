#!/usr/bin/env python3

# prerequisite package imports
import numpy as np
import matplotlib.pyplot as plt

y = np.arange(0, 11) ** 3

# your code here

x = np.arange(0, 11)
plt.plot(x, y, color='red', linestyle='-')
plt.xlim((0, 10))

plt.show()
