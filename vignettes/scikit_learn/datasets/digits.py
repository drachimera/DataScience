#!/usr/bin/env python
"""
The MNIST Digits ScikitLearn.

This is a perfect dataset for a classification problem.
"""
import matplotlib.pyplot as plt
import pylab
import numpy as np
from sklearn.datasets import load_digits
digits = load_digits()
print(digits.images.shape)
print(digits.images[0])
plt.matshow(digits.images[0], cmap=plt.cm.Greys)
pylab.draw()
