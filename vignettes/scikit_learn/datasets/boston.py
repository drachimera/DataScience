#!/usr/bin/env python
"""The Boston Dataset Included in ScikitLearn This is a perfect dataset for a regression problem."""
import numpy as np
from sklearn.datasets import load_boston
from sklearn.cross_validation import cross_val_predict
from sklearn import linear_model
from sklearn.ensemble import RandomForestRegressor
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import Imputer
from sklearn.cross_validation import cross_val_score
import matplotlib.pyplot as plt

# Load the data...
boston = load_boston()
print(boston.data.shape)
# Samples total 	506
# Dimensionality 	13
# Features 	real, positive
# Targets 	real 5. - 50.
# Returns:
#
# data : Bunch
#
# Dictionary-like object, the interesting attributes are:
#   "data", the data to learn, "target", the regression targets, and "DESCR",
#   the full description of the dataset.
print(len(boston.data))
print(boston.data)
print(len(boston.target))
print(boston.target)
print(boston.DESCR)
print(boston)
########################################
# Plotting Cross-Validated Predictions
########################################
lr = linear_model.LinearRegression()
y = boston.target

# cross_val_predict returns an array of the same size as `y` where each entry
# is a prediction obtained by cross validated:
predicted = cross_val_predict(lr, boston.data, y, cv=10)

fig, ax = plt.subplots()
ax.scatter(y, predicted)
ax.plot([y.min(), y.max()], [y.min(), y.max()], 'k--', lw=4)
ax.set_xlabel('Measured')
ax.set_ylabel('Predicted')
plt.show()

########################################
# Imputing missing values before building an estimator
########################################
rng = np.random.RandomState(0)

X_full, y_full = boston.data, boston.target
n_samples = X_full.shape[0]
n_features = X_full.shape[1]

# Estimate the score on the entire dataset, with no missing values
estimator = RandomForestRegressor(random_state=0, n_estimators=100)
score = cross_val_score(estimator, X_full, y_full).mean()
print("Score with the entire dataset = %.2f" % score)

# Add missing values in 75% of the lines
missing_rate = 0.75
n_missing_samples = np.floor(n_samples * missing_rate)
missing_samples = np.hstack((np.zeros(n_samples - n_missing_samples,
                                      dtype=np.bool),
                             np.ones(n_missing_samples,
                                     dtype=np.bool)))
rng.shuffle(missing_samples)
missing_features = rng.randint(0, n_features, n_missing_samples)

# Estimate the score without the lines containing missing values
X_filtered = X_full[~missing_samples, :]
y_filtered = y_full[~missing_samples]
estimator = RandomForestRegressor(random_state=0, n_estimators=100)
score = cross_val_score(estimator, X_filtered, y_filtered).mean()
print("Score without the samples containing missing values = %.2f" % score)

# Estimate the score after imputation of the missing values
X_missing = X_full.copy()
X_missing[np.where(missing_samples)[0], missing_features] = 0
y_missing = y_full.copy()
estimator = Pipeline([("imputer", Imputer(missing_values=0,
                                          strategy="mean",
                                          axis=0)),
                      ("forest", RandomForestRegressor(random_state=0,
                                                       n_estimators=100))])
score = cross_val_score(estimator, X_missing, y_missing).mean()
print("Score after imputation of the missing values = %.2f" % score)
