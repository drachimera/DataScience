from sklearn.linear_model import SGDClassifier

X = [[0.,0.],[1.,1.]] #an array X of size [n_samples, n_features] holding the training samples
y = [0,1]             #an array Y of size [n_samples] holding the target values (class labels) for the training samples

clf = SGDClassifier(loss="hinge", penalty="l2", shuffle=True, fit_intercept=True)

#fit the model
print "fit..."
info = clf.fit(X,y)
print info 

#use the model to make a prediction
pred = clf.predict([[2., 2.]])
print pred[0] #only one result in the result array

print "Model params:"
model_params = clf.coef_
print model_params

print "Intercept"
intercept = clf.intercept_
print intercept

print "complete."
