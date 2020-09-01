import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_digits
import sys
sys.path.append('..')
import plotUtil

digits = load_digits()

plt.matshow(digits.images[0], cmap=plt.cm.Greys)
plt.show()
