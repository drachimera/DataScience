import pandas
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn_pandas import DataFrameMapper
from sklearn2pmml.decoration import ContinuousDomain
from sklearn.externals import joblib
from sklearn.ensemble import RandomForestClassifier

#Obtain the data!
iris_df = pandas.read_csv("Iris.csv")

# Describe data and data pre-processing actions by creating an appropriate sklearn_pandas.DataFrameMapper object:
iris_mapper = DataFrameMapper([
    (["Sepal.Length", "Sepal.Width", "Petal.Length", "Petal.Width"], [ContinuousDomain(), StandardScaler(), PCA(n_components = 3)]),
    ("Species", None)
])

iris = iris_mapper.fit_transform(iris_df)

# Train an appropriate estimator object:

iris_X = iris[:, 0:3]
iris_y = iris[:, 3]

iris_forest = RandomForestClassifier(min_samples_leaf = 5)
iris_forest.fit(iris_X, iris_y)

# Serialize the sklearn_pandas.DataFrameMapper object and estimator object in pickle data format
joblib.dump(iris_mapper, "mapper.pkl", compress = 9)
joblib.dump(iris_forest, "estimator.pkl", compress = 9)
