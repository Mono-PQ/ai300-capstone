# AI300: Capstone Project - Telco Customer Churn Prediction (May23-Team05)

## Table of Contents
- [AI300: Capstone Project - Telco Customer Churn Prediction (May23-Team05)](#ai300-capstone-project---telco-customer-churn-prediction-may23-team05)
  - [Table of Contents](#table-of-contents)
  - [Website of Deployed Web Application](#website-of-deployed-web-application)
  - [Chosen Model and Features](#chosen-model-and-features)
  - [Offline AUC metrics of above model](#offline-auc-metrics-of-above-model)

## Website of Deployed Web Application
- Deployed machine learning model via a flask web application to predict whether customer would churn. 
- Database connection was established to AWS RDMS to extract relevant data via SQL query. Data exploration was conduction before modeling. Codes can be found in the `notebooks` folder. 
- Flask web application was created to wrap the ML model for deployment enabling users to interact with the ML model via an online form or an API call.
- Cloud deployment to AWS EC2 using a public docker image. However, due to limitations of the free-tier in AWS, an alternative deployment was made to `onrender` free-tier account. 
- [Deployed Capstone Website @ https://ai300-capstone-project.onrender.com/](https://ai300-capstone-project.onrender.com/) *Website takes some time to load due to resource allocation and start up required for free-tier.*
- API address resource: `https://ai300-capstone-project.onrender.com/api/predict` 
  - Parameters documentation can be found [here](https://ai300-capstone-project.onrender.com/doc#apicall)

## Chosen Model and Features
- A list of features can be found [here](https://ai300-capstone-project.onrender.com/doc#inputfeatures)
- After using `pycaret` for model comparison and shortlisting both gradient boosting classifier and catboost classifier for model training and evaluation. The final chosen model is the following `catboost classifier`. 
- Hyperparameters of `catboost classifier`: `{'learning_rate': 0.025, 'depth': 4}`

![Pycaret Model Comparison](img/pycaret_modelcomparison.png)

## Offline AUC metrics of above model
- Both `gradient boosting classifier` and `catboost classifier` achieved an offline AUC of 0.90 for the test data. However, based on the confusion matrix below, `catboost classifier` performs slightly better. 

- **Gradient Boosting Classifier Confusion Matrix Plot**

![Gradient Boosting Classifier Confusion Matrix](img/gradboost_classifier_cm.png)

- **CatBoost Classifier Confusion Matrix Plot**

![CatBoost Classifer Confusion Matrix](img/catboost_classifer_cm.png)