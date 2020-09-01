import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import load_boston
from sklearn.cross_validation import train_test_split
from sklearn.linear_model import Ridge
# %matplotlib inline

# Load Dataset
boston = load_boston()
# boston.keys()
# see ../datasets/boston.py for a description of the dataset
# standard test/train split
X_train, X_test, y_train, y_test = train_test_split(boston.data, boston.target)

# Learning a regressor
ridge = Ridge()
ridge.fit(X_train, y_train)
pred_test = ridge.predict(X_test)
print(pred_test)
