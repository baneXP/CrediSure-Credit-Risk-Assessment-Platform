# CrediSure – Credit Risk Assessment Platform

CrediSure is an end-to-end **credit risk assessment system** that predicts the probability of loan default using applicant financial and demographic data.  
The project demonstrates a complete **machine learning pipeline**, from data preprocessing and feature engineering to model evaluation and deployment.

---
## Dataset

The model was trained and evaluated using the **UCI Default of Credit Card Clients dataset**, a publicly available benchmark dataset for credit risk modeling.

- **Dataset :** Default of Credit Card Clients
- - **Source:** [UCI Machine Learning Repository – Default of Credit Card Clients](https://archive.ics.uci.edu/dataset/350/default+of+credit+card+clients)  
- **Description:** Contains financial, demographic, bill amount, and payment history features of credit card clients, along with a binary default label.
  
---
## Features

- End-to-end **credit risk prediction pipeline**
- Robust **data cleaning, EDA, and feature engineering**
- **Logistic Regression** with L1 (Lasso) and L2 (Ridge) regularization
- Handles **class imbalance using SMOTE**
- Model evaluation using **ROC-AUC, precision, recall**
- **Flask-based web application** for probability-based predictions

---

## Problem Statement

Financial institutions need to assess the **risk of loan default** accurately to minimize losses and make informed lending decisions.  
This project aims to build a **data-driven decision-support system** that outputs a probability score representing the applicant’s credit risk.

---

## Tech Stack

- **Language:** Python  
- **Libraries:** Pandas, NumPy, Scikit-learn, Imbalanced-learn (SMOTE)  
- **Modeling:** Logistic Regression (L1 & L2 Regularization)  
- **Visualization:** Matplotlib, Seaborn  
- **Deployment:** Flask  

---

## 📊 Data Pipeline

1. **Data Ingestion**
   - Load financial and demographic loan applicant data

2. **Data Cleaning**
   - Handle missing values
   - Encode categorical variables
   - Scale numerical features

3. **Exploratory Data Analysis (EDA)**
   - Distribution analysis
   - Correlation analysis
   - Identification of key risk-driving factors

4. **Feature Engineering**
   - Feature selection using regularization
   - Transformation for model stability

5. **Model Training**
   - Logistic Regression with:
     - L1 (Lasso) for feature selection
     - L2 (Ridge) for stability

6. **Handling Class Imbalance**
   - Applied **SMOTE** to balance minority and majority classes

7. **Model Evaluation**
   - ROC-AUC
   - Precision & Recall
   - Confusion Matrix

8. **Deployment**
   - Flask app serving probability-based predictions

---

## Model Evaluation Metrics

- **ROC-AUC**
- **Precision**
- **Recall**
- **Confusion Matrix**

These metrics ensure balanced evaluation, especially for imbalanced datasets.

---

## Application Output

- Takes applicant details as input
- Returns a **probability score** indicating loan default risk
- Designed as a **decision-support tool**, not a binary accept/reject system

---

## How to Run Locally

```bash
# Clone the repository
git clone https://github.com/baneXP/CrediSure-Credit-Risk-Assessment-Platform.git
cd CrediSure-Credit-Risk-Assessment-Platform

# Install dependencies
pip install -r requirements.txt

# Run the Flask app
python app.py

## Features

- End-to-end **credit risk prediction pipeline**
- Robust **data cleaning, EDA, and feature engineering**
- **Logistic Regression** with L1 (Lasso) and L2 (Ridge) regularization
- Handles **class imbalance using SMOTE**
- Model evaluation using **ROC-AUC, precision, recall**
- **Flask-based web application** for probability-based predictions

---

## Problem Statement

Financial institutions need to assess the **risk of loan default** accurately to minimize losses and make informed lending decisions.  
This project aims to build a **data-driven decision-support system** that outputs a probability score representing the applicant’s credit risk.

---

## Tech Stack

- **Language:** Python  
- **Libraries:** Pandas, NumPy, Scikit-learn, Imbalanced-learn (SMOTE)  
- **Modeling:** Logistic Regression (L1 & L2 Regularization)  
- **Visualization:** Matplotlib, Seaborn  
- **Deployment:** Flask  

---

## 📊 Data Pipeline

1. **Data Ingestion**
   - Load financial and demographic loan applicant data

2. **Data Cleaning**
   - Handle missing values
   - Encode categorical variables
   - Scale numerical features

3. **Exploratory Data Analysis (EDA)**
   - Distribution analysis
   - Correlation analysis
   - Identification of key risk-driving factors

4. **Feature Engineering**
   - Feature selection using regularization
   - Transformation for model stability

5. **Model Training**
   - Logistic Regression with:
     - L1 (Lasso) for feature selection
     - L2 (Ridge) for stability

6. **Handling Class Imbalance**
   - Applied **SMOTE** to balance minority and majority classes

7. **Model Evaluation**
   - ROC-AUC
   - Precision & Recall
   - Confusion Matrix

8. **Deployment**
   - Flask app serving probability-based predictions

---

## Model Evaluation Metrics

- **ROC-AUC**
- **Precision**
- **Recall**
- **Confusion Matrix**

These metrics ensure balanced evaluation, especially for imbalanced datasets.

---

## Application Output

- Takes applicant details as input
- Returns a **probability score** indicating loan default risk
- Designed as a **decision-support tool**, not a binary accept/reject system

---

## How to Run Locally

```bash
# Clone the repository
git clone https://github.com/baneXP/CrediSure-Credit-Risk-Assessment-Platform.git
cd CrediSure-Credit-Risk-Assessment-Platform

# Install dependencies
pip install -r requirements.txt

# Run the Flask app
python app.py
