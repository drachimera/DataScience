Directory for scripts and methods for exploratory data analysis (eda)

Simplistic procedure:
1. Google column names, ask questions or read articles to understand how the data was generated and what each column means.  Understand when specific data elements will be available based on the workflow.

2. Plot feature 1 vs feature 2 for all features in the dataset.  Compare test train validate and real-time datasets

3. Profile the data, determine which columns are categorical vs continuous, binary, counters and so on

4. Identify missing cells and convert the value to something else the algorithm needs (e.g. -999). Missing-ness is a complex topic!  More later.

5.  Use something like random forest classifier to investigate variable importance

6. Attempt to decode variables if they have been modified.  Transform variables into values that are more natural for numerical analytics (e.g. dates to days since 1970 or whatever)


Here is the overall procedure for a binary classification problem (expressed in R by Dennis Murphree originally):

Data Diagnostics:

#describe the data (literally, describe(rawData))

Look for factors with large numbers of levels, low level occupancy, variables imported with the wrong type, etc.  Check that numObs and numPredictors is what you expect from raw data file.

#count missing values

#print the factor contingency tables for categorical variables on the response

#print the factor proportional tables for categorical variables on the response

#report on near zero variance variables

#report near zero variance conditioned on the response. i.e. that are sparse within groups of the response

#plot the correlation matrix for numeric data, omitting zero variance predictors

#check for predictors that are linear combinations of other predictors (I use trim.matrix, and I currently don’t do this for categorical variables, but I could with a QR decomp on the cov(model.matrix(rawData))

#check the scales of all continuous variables (I use “summary”)

#check skewness and ratios of max/min of continuous variables (could also plot)

#plot the response, think about transforms

#check for factors with large numbers of levels (I report if more than four)

#check for correlations using PCA (I don’t routinely do this because I’m spoiled by trees)

#report class balance in response
Training:

#keep only predictors of interest

#center and scale continuous predictors

#resample if necessary (SMOTE, upSample, synthpop)

#optional – holdout set.  I only do this if I expect to need to tune a classification threshold, otherwise I just report cross-validation results

#create training parameters object and save all necessary vars to a “precompute file.”

#in parallel and using five fold cross-validation:

#train gbm

#train fda

#train glm

#train C5.0

Hyper-parameter Suggestions
#train gbm

	interaction depth:	1,2,3
	shrinkage:	0.01, 0.1
	n.trees:	100, 500, 1000, 2000

#train fda (assuming MARS)

	degree:	1,2,3	
	nprune:	2, 9, 17

#train glmnet

	alpha:		0.1 to 1 by 0.1
	lambda:	0.01 to 0.20 by 0.01 .  For problems with larger p consider higher 2, 4 maybe even 1000 (genomics)

#train C5.0

	model:		tree
	winnow:	false, true
	trials:		1, 25, 50, 75, 100


replace with naiveBayes


Here is the procedure for regression (expressed by Xuewei Wang originally)
Regression Modeling

Reporting:

#report AUC on out-of-sample CV observations along with bootstrapped confidence intervals (2000 passes)

Assumption 
•	Continuous predictors and response
•	No missing values
Out of scope: ordinal regression, passion regression
Data diagnostics
•	Explore dynamic ranges, skewness of distribution, co-linearity etc
•	Determine the need to transform data (predictors and response) or reduce data (predictors/observations)

Models
Models for quick test
Models                            |  hyperparameters    	       | Note
Ordinary linear regression        |	                               | Applies to cases where p < n
Qth-degree polynomial regression  |  Q (2 or higher)               |	
Elastic net	                      | Alpha, Lambda                  |	
Partial Least Square Regression   |	Number of latent components    |	
Principal component regression	  | Number of principal components |	

Other models: SVR, NN, CART
Other modeling considerations:
•	Observation weighting:  i.e. LOESS-based, density-based
•	Data transformation: i.e.  log, exp, sin etc
•	Observations selection: outliers, re-sampling 
Model training
•	Scaling predictors
•	5- or 10-fold Cross-validation
Model Reporting
•	Performance: RMSE, correlation (random model at 0), concordance index (random model at 0.5)
•	Predictors identified by models if necessary



Here is the procedure for multi-class classification problems (originally expressed by Eric Polley)
Binary and Multiclass Classification Outline
Introduction
This document assumes the data is a random sample of independent observations from the study population and that the data has been processed by the Data Quality pipeline. The goal of this pipeline is to take a classification scenario and quickly assess potential classification performance.
Pipeline overview
Let Y be the outcome class labels and X the N×P matrix with features. Rows are individual observations and columns are features/variables. The initial step is to assess the metrics in Table [tab:metadata]. The values of parameters will be used for selection of algorithms and ranges of tuning parameters. Individual algorithms may be run with different values of their tuning parameters. All algorithms will be run using V-fold cross validation for estimation of performance metrics. The value for V (number of folds) will be determined as a function of the number of observations, N. If performance is acceptable, an ensemble can be created by estimating a convex combination of the individual algorithms minimizing the cross-validated loss function.
For multinomial classification, the vector Y will be split into a series of binomial indictor variables. For example, if Y_i∈(A,B,C) create 3 new vectors:
■(Y_Ai=&1 if Y_i=A,otherwise 0@Y_Bi=&1 if Y_i=B,otherwise 0@Y_Ci=&1 if Y_i=C,otherwise 0)
Then treat each new vector as a binary classification problem. For a new observation, classification is performed by taking the maximal predicted probability across the series of binomial predicted probabilities.
Parameters of training data
Description	Notation	Values
Sample size	N	(1,2,…)
Number of features	P	(1,2,…)
Ratio of N and P	N/P	(0,∞)
Cardinality of Y	M	(2,3,…)
Diversity of Y	D^Y	(0,∞)
Number of categorial features	P_cat	(0,1,2,…,P)
Number of continuous features	P_con	(0,1,2,…,P)
Tuning parameters
Matching up variables from Table [tab:metadata] to give starting values for tuning parameters based on training a large and diverse set of classifiers and observing final optimal tuning parameter values. The selection of optimal tuning parameter ranges is based on the concept of AutoML.
Tuning parameters for classification algorithms
Algorithm	Description	Argument	Values
xgboost (Gradient boosting)			
	max number of iterations	nrounds	
	tree depth	max_depth	
	shrinkage parameter	eta	(0,1)
	minimum loss reduction for split	gamma	
	Min. samples per node	min_child_weight	
			
glmnet (Elastic Net)			
	mixture of L1 and L2 penalty	alpha	[0,1]
	weight of penalty term	lambda	
	number of lambda values	nlambda	
	smallest value of lambda	lambda.min.ratio	
			
randomForest (Random Forests)			
	number of variables selected	mtry	
	number of trees	ntree	
	minimum size of node	nodesize	
			
rpart (Recursive Partitioning)			
	minimum node size to split	minsplit	
	minimum terminal node size	minbucket	
	complexity parameter	cp	
	maximum depth	maxdepth	
Reports
Since each algorithm will be run using V-fold cross validation, estimates of performance metrics will be provided along with confidence intervals derived from the cross-validation procedure.

