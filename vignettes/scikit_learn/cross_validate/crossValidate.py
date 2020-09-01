import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.cross_validation import train_test_split
from sklearn.cross_validation import cross_val_score
from sklearn.cross_validation import KFold
from sklearn.cross_validation import StratifiedKFold

iris = load_iris()
X, y = iris.data, iris.target
print (X.shape)
print (y.shape)
print(y)
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)
print(X_train.shape)
print(X_test.shape)

classifier = KNeighborsClassifier()
classifier.fit(X_train, y_train)
classifier.score(X_test, y_test)

# use cross validation instead of standard split into test/train

# KINDS OF CROSS validation
# 1. KFold divides all the samples in k groups of samples, called folds
# (if k = n, this is equivalent to the Leave One Out strategy), of equal sizes
# (if possible). The prediction function is learned using k - 1 folds, and the
# fold left out is used for test.
# THIS IS OK FOR REGRESSION PROBLEMS

scores = cross_val_score(classifier, X, y)
print(scores)
print(np.mean(scores))
# use ten groups for cross validation
cvscore = cross_val_score(classifier, X, y, cv=10)
print(cvscore)

# an alternate way to do KFold cross validation is as follows:
kf = KFold(4, n_folds=2)
for train, test in kf:
    print("%s %s" % (train, test))
# this shows how the generator function creates indexes for each subset
# generated in the cross validation procedure

print("##################################################")

# 2. StratifiedKFold - is a variation of k-fold which returns stratified folds:
# each set contains approximately the same percentage of samples of each target
# class as the complete set.
# USE THIS WHENEVER YOU DO A CLASSIFICATION PROBLEM!!!!
cv = StratifiedKFold(iris.target, n_folds=5)
for train, test in cv:
    print(test)

# LabelKFold is a variation of k-fold which ensures that the same label is not
# in both testing and training sets. This is necessary for example if you
# obtained data from different subjects and you want to avoid over-fitting
# (i.e., learning person specific features) by testing and training
# on different subjects.

print("##################################################")
