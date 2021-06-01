# Challenge 2
# Write a NumPy program to compute the histogram of nums against the bins.
#  Label your x-axis with nums and y-axis with bins. Add a title to the histogram: Histogram of nums against bins.
# Sample Output:
# nums: [0.5 0.7 1. 1.2 1.3 2.1]
# bins: [0 1 2 3]
# Result: (array([2, 3, 1], dtype=int64), array([0, 1, 2, 3]))

import numpy as np
import matplotlib.pyplot as plt

nums = [0.5, 0.7, 1, 1.2, 1.3, 2.1]
bins = [0, 1, 2, 3]

plt.title("Num vs Bins")
plt.xlabel("Numbers")
plt.ylabel("Bins")
plt.hist(nums, bins,)
plt.style.use('seaborn-white')
plt.show()

