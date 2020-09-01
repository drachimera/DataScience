"""."""
import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import load_digits
from sklearn.cross_validation import train_test_split
from sklearn.svm import LinearSVC
from sklearn.ensemble import RandomForestClassifier

# Load some data
digits = load_digits()

# split the data into training and testing
X_train, X_test, y_train, y_test = train_test_split(digits.data, digits.target)

# Apply Linear Classifier
svm = LinearSVC(C=0.1)
svm.fit(X_train, y_train)
print(svm.predict(X_train))
print(y_train)
# Score on training (should be near 1)
s_train = svm.score(X_train, y_train)
print(s_train)

# score on testing (should be worse!)
s_test = svm.score(X_test, y_test)
print(s_test)

# Lets do it with a different model...
# RandomForest
rf = RandomForestClassifier(n_estimators=50)
rf.fit(X_train, y_train)
rf.predict(X_test)
rf_test = rf.score(X_test, y_test)
print(rf_test)

# Labels can be anything!
numbers = np.array(["zero", "one", "two", "three",
                    "four", "five", "six", "seven",
                    "eight", "nine"])
y_train_string = numbers[y_train]
svm.fit(X_train, y_train_string)
text_predict = svm.predict(X_test)
print(text_predict)
