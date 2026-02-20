from flask import Flask, request, render_template
import pandas as pd
import numpy as np
import pickle

app = Flask(__name__)

# Load Model + Scaler
model  = pickle.load(open('models/best_model.pkl', 'rb'))
scaler = pickle.load(open('models/standard_scaler.pkl', 'rb'))
print("Model + Scaler loaded")

# Currency converter
INR_TO_NT = 0.4   
NT_TO_INR = 2.5   

# Feature Engineering (same as training)
def engineer_features(df):
    df['TOTAL_BILL']         = df[['BILL_AMT1','BILL_AMT2','BILL_AMT3','BILL_AMT4','BILL_AMT5','BILL_AMT6']].sum(axis=1)
    df['TOTAL_PAID']         = df[['PAY_AMT1','PAY_AMT2','PAY_AMT3','PAY_AMT4','PAY_AMT5','PAY_AMT6']].sum(axis=1)
    df['PAYMENT_RATIO']      = df['TOTAL_PAID'] / (df['TOTAL_BILL'] + 1)
    df['CREDIT_UTILIZATION'] = (df['BILL_AMT1'] / (df['LIMIT_BAL'] + 1)).clip(0, 1)
    pay_cols                 = ['PAY_0','PAY_2','PAY_3','PAY_4','PAY_5','PAY_6']
    df['AVG_DELAY']          = df[pay_cols].mean(axis=1)
    df['MAX_DELAY']          = df[pay_cols].max(axis=1)
    df['MISSED_PAYMENTS']    = (df[pay_cols] > 0).sum(axis=1)
    df['BILL_TREND']         = df['BILL_AMT1'] - df['BILL_AMT6']
    df['RISK_SCORE']         = (df['MISSED_PAYMENTS']*2 + df['MAX_DELAY'] +
                                df['CREDIT_UTILIZATION']*3 - df['PAYMENT_RATIO']*2)
    return df

# Feature Order (must match training exactly)
FEATURE_COLS = [
    'LIMIT_BAL','EDUCATION','AGE','PAY_0','PAY_2','PAY_3','PAY_4','PAY_5','PAY_6',
    'BILL_AMT1','BILL_AMT2','BILL_AMT3','BILL_AMT4','BILL_AMT5','BILL_AMT6',
    'PAY_AMT1','PAY_AMT2','PAY_AMT3','PAY_AMT4','PAY_AMT5','PAY_AMT6',
    'TOTAL_BILL','TOTAL_PAID','PAYMENT_RATIO','CREDIT_UTILIZATION',
    'AVG_DELAY','MAX_DELAY','MISSED_PAYMENTS','BILL_TREND','RISK_SCORE'
]

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    try:
        raw = {
            # Monetary fields — convert ₹ to NT$ for model
            'LIMIT_BAL' : float(request.form['LIMIT_BAL']) * INR_TO_NT,
            'BILL_AMT1' : float(request.form['BILL_AMT1']) * INR_TO_NT,
            'BILL_AMT2' : float(request.form['BILL_AMT2']) * INR_TO_NT,
            'BILL_AMT3' : float(request.form['BILL_AMT3']) * INR_TO_NT,
            'BILL_AMT4' : float(request.form['BILL_AMT4']) * INR_TO_NT,
            'BILL_AMT5' : float(request.form['BILL_AMT5']) * INR_TO_NT,
            'BILL_AMT6' : float(request.form['BILL_AMT6']) * INR_TO_NT,
            'PAY_AMT1'  : float(request.form['PAY_AMT1'])  * INR_TO_NT,
            'PAY_AMT2'  : float(request.form['PAY_AMT2'])  * INR_TO_NT,
            'PAY_AMT3'  : float(request.form['PAY_AMT3'])  * INR_TO_NT,
            'PAY_AMT4'  : float(request.form['PAY_AMT4'])  * INR_TO_NT,
            'PAY_AMT5'  : float(request.form['PAY_AMT5'])  * INR_TO_NT,
            'PAY_AMT6'  : float(request.form['PAY_AMT6'])  * INR_TO_NT,

            # Non-monetary fields — no conversion needed
            'EDUCATION' : float(request.form['EDUCATION']),
            'AGE'       : float(request.form['AGE']),
            'PAY_0'     : float(request.form['PAY_0']),
            'PAY_2'     : float(request.form['PAY_2']),
            'PAY_3'     : float(request.form['PAY_3']),
            'PAY_4'     : float(request.form['PAY_4']),
            'PAY_5'     : float(request.form['PAY_5']),
            'PAY_6'     : float(request.form['PAY_6']),
        }

        # Build DataFrame + engineer features
        df = pd.DataFrame([raw])
        df = engineer_features(df)

        # Scale
        X        = df[FEATURE_COLS]
        X_scaled = scaler.transform(X)

        # Predict
        prob      = model.predict_proba(X_scaled)[0][1]
        threshold = 0.35
        risk      = 'HIGH' if prob >= 0.5 else 'MEDIUM' if prob >= threshold else 'LOW'

        # Risk color for UI
        color = '#e74c3c' if risk == 'HIGH' else '#f39c12' if risk == 'MEDIUM' else '#2ecc71'

        return render_template('result.html',
            probability = round(prob * 100, 2),
            risk_level  = risk,
            color       = color,
            limit_bal   = raw['LIMIT_BAL'] * NT_TO_INR,  # display in ₹
            age         = int(raw['AGE']),
            missed      = int(df['MISSED_PAYMENTS'].values[0]),
            pay_ratio   = round(float(df['PAYMENT_RATIO'].values[0]), 3)
        )

    except Exception as e:
        return render_template('result.html', error=str(e))


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
