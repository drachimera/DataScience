Important documentation:

https://github.com/jpmml/jpmml-sklearn

https://github.com/jpmml/sklearn2pmml

pip install --user --upgrade git+https://github.com/jpmml/sklearn2pmml.git

#converting the pickles to xml:
java -jar jpmml-sklearn/target/converter-executable-1.0-SNAPSHOT.jar --pkl-input estimator.pkl --pmml-output estimator.pmml
  
java -jar jpmml-sklearn/target/converter-executable-1.0-SNAPSHOT.jar --pkl-mapper-input mapper.pkl --pkl-estimator-input estimator.pkl --pmml-output mapper-estimator.pmml
