# CrediSure — Credit Risk Assessment Platform

> An end-to-end ML platform predicting loan default probability using applicant financial and demographic data.

 **Live Demo:** [credisure.me](http://credisure.me:5000) &nbsp;|&nbsp;  **GitHub:** [baneXP/CrediSure](https://github.com/baneXP/CrediSure-Credit-Risk-Assessment-Platform)

---

## Tech Stack

| Layer | Tools |
|-------|-------|
| Language | Python |
| ML Libraries | Pandas, NumPy, Scikit-learn, Imbalanced-learn |
| Models | Logistic Regression, Random Forest, XGBoost, LightGBM |
| Class Imbalance | SMOTE |
| Web App | Flask + Gunicorn |
| Deployment | AWS EC2 (ap-south-1) |
| Domain | credisure.me |

---

## Features

- End-to-end credit risk prediction pipeline on **29,925 real-world records**
- **9 custom engineered features** (payment ratio, credit utilization, missed payments, risk score)
- Handles **78:22 class imbalance** using SMOTE
- Compared **4 models** evaluated on ROC-AUC, Precision and Recall
- **Flask web app** deployed on AWS EC2 with Gunicorn — accessible live at [credisure.me](http://credisure.me:5000)

---

## ML Pipeline

```
Raw Data → Cleaning → EDA → Feature Engineering
→ SMOTE → Model Training → Evaluation → Flask API → EC2 Deployment
```

1. **Data Cleaning** — missing values, encoding, scaling
2. **EDA** — distribution, correlation, risk factor analysis
3. **Feature Engineering** — 9 custom features added on top of original 21
4. **Modelling** — Logistic Regression, Random Forest, XGBoost, LightGBM
5. **Evaluation** — ROC-AUC, Precision, Recall, Confusion Matrix
6. **Deployment** — Flask + Gunicorn on AWS EC2, live at credisure.me

---

## Model Results

| Model | ROC-AUC |
|-------|---------|
| Random Forest | 0.760 |
| XGBoost | 0.749 |
| LightGBM | 0.746 |
| Logistic Regression | 0.724 |

---

## Run Locally

```bash
git clone https://github.com/baneXP/CrediSure-Credit-Risk-Assessment-Platform.git
cd CrediSure-Credit-Risk-Assessment-Platform
pip install -r requirements.txt
python app.py
```

Open `http://localhost:5000`

---

## Dataset

UCI Default of Credit Card Clients — 29,925 records, 23 features  
Source: [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/default+of+credit+card+clients)

---

*Built by [Satyam Sharma](https://linkedin.com/in/sharmasatyam01) • Deployed on AWS EC2*
