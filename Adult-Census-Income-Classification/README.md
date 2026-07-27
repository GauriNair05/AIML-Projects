# Adult Census Income Classification

## Overview

This project implements a complete Machine Learning pipeline on the *Adult Census Income Dataset* to predict whether an individual's annual income exceeds *$50K* based on demographic and employment-related attributes. The project covers data understanding, preprocessing, feature engineering, model building, and performance evaluation using multiple classification algorithms.

---

## Dataset

The dataset contains demographic and employment information collected from the *1994 U.S. Census Database*. The objective is to classify whether a person's annual income is:

- *<=50K*
- *>50K*

### Dataset Source

- UCI Machine Learning Repository: https://archive.ics.uci.edu/ml/datasets/adult
- Kaggle: https://www.kaggle.com/datasets/uciml/adult-census-income

The dataset contains approximately *32,561 records* and *15 attributes*.

---

## Problem Statement

Predict whether an individual's annual income exceeds *$50,000* using demographic and employment-related features.

This is a *Supervised Binary Classification* problem.

---

## Features

- Age
- Workclass
- Final Weight (fnlwgt)
- Education
- Education Number
- Marital Status
- Occupation
- Relationship
- Race
- Sex
- Capital Gain
- Capital Loss
- Hours per Week
- Native Country
- Income (Target Variable)

---

## Technologies Used

- Python
- Google Colab
- Pandas
- NumPy
- Scikit-learn

---

## Machine Learning Workflow

### Task 1: Dataset Understanding

- Load dataset
- Explore dataset structure
- Check data types
- Identify missing values
- Analyze target variable

### Task 2: Data Cleaning

- Replace missing values
- Remove incomplete records
- Prepare clean dataset

### Task 3: Feature Engineering

- Label Encoding
- Feature Scaling
- Train-Test Split

### Task 4: Model Building

The following classification algorithms were implemented:

- Logistic Regression
- Decision Tree
- Random Forest
- K-Nearest Neighbors (KNN)
- Support Vector Machine (SVM)

### Task 5: Performance Evaluation

Each model is evaluated using:

- Accuracy
- Precision
- Recall
- F1 Score
- ROC-AUC Score

---

## Project Structure


Adult-Census-Income/
│
├── Adult_Census_Income.ipynb
├── adult_income_results.csv
├── README.md


---




## Results

The project compares five supervised machine learning algorithms for predicting income categories. Model performance is evaluated using standard classification metrics to identify the best-performing classifier for the Adult Census Income dataset.

---

## Future Improvements

- Hyperparameter Tuning
- Cross Validation
- Feature Selection
- Ensemble Learning
- XGBoost
- LightGBM
- CatBoost

---

## Learning Outcomes

- Data Preprocessing
- Feature Engineering
- Binary Classification
- Model Evaluation
- Machine Learning Workflow
- Performance Comparison

---

## References

1. UCI Machine Learning Repository – Adult Dataset
2. Kaggle – Adult Census Income Dataset
3. Scikit-learn Documentation
4. Pandas Documentation
