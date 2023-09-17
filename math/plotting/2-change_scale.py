#!/usr/bin/env python3

# prerequisite package imports
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 28651, 5730)
r = np.log(0.5)
t = 5730
y = np.exp((r / t) * x)

# your code here

plt.plot(x, y)
plt.yscale('log')
plt.xlim(0, 28650)
plt.xlabel('Time (years)')
plt.ylabel('Fraction Remaining')
plt.title('Exponential Decay of C-14')  # This sets the plot title

plt.show()  # To display the plot
