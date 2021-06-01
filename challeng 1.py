# Challenge 1
# Write a NumPy program to compute the mean,
# standard deviation, and variance of a given array along the second axis. Use
# np.arange function to generate 20 numbers starting from 0.


import matplotlib.pyplot as plt
import numpy
import numpy as np
import matplotlib.pyplot as plt

numbers = np.arange(0, 20)

my_mean = numpy.mean(numbers)  # mean
my_std = numpy.std(numbers)
my_var = numpy.var(numbers)
x = [my_mean, my_std, my_var]
print("The mean is : ", my_mean)
print("The standard deviation : ", my_std)
print("The variances  : ", my_var)

