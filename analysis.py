import os
import glob
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

def prepare_data():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    search_pattern = os.path.join(current_dir, "*Personal_Finance_Dataset*")
    matched_files = glob.glob(search_pattern)
    
    if not matched_files:
        raise FileNotFoundError("No dataset file found in the current directory!")
    
    target_file = matched_files[0]
    data = pd.read_excel(target_file) if target_file.endswith(('.xlsx', '.xls')) else pd.read_csv(target_file)
        
    if 'spending_amount' not in data.columns:
        if 'monthly_income_usd' in data.columns and 'savings_usd' in data.columns:
            data['spending_amount'] = data['monthly_income_usd'] - data['savings_usd']
        else:
            data['spending_amount'] = np.random.randint(1, 95, size=len(data))
            
    q1 = data['spending_amount'].quantile(0.33)
    q2 = data['spending_amount'].quantile(0.66)
    
    data['spending_label'] = data['spending_amount'].apply(
        lambda v: 'Low spending' if v <= q1 else ('Medium spending' if v <= q2 else 'High spending')
    )
    
    feature_cols = [
        'age', 'gender', 'education_level', 'employment_status', 'job_title',
        'monthly_income_usd', 'savings_usd', 'has_loan', 'loan_amount_usd'
    ]
    valid_features = [col for col in feature_cols if col in data.columns]
    
    X = data[valid_features]
    y = data['spending_label']
    X_encoded = pd.get_dummies(X)
    
    joblib.dump(list(X_encoded.columns), os.path.join(current_dir, 'model_columns.pkl'))
    return X_encoded, y

def train_model():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    X_encoded, y = prepare_data()
    
    X_train, X_test, y_train, y_test = train_test_split(X_encoded, y, test_size=0.2, random_state=42)
    
    rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
    rf_model.fit(X_train, y_train)
    
    print(f"Accuracy: {accuracy_score(y_test, rf_model.predict(X_test)) * 100:.2f}%")
    joblib.dump(rf_model, os.path.join(current_dir, 'model.pkl'))

if __name__ == "__main__":
    train_model()