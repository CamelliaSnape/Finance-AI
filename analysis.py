import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

def prepare_data():
    data = pd.read_csv("Personal_Finance_Dataset.csv")
    
    feature_cols = [
        'age', 'gender', 'education_level', 'employment_status', 'job_title',
        'monthly_income_usd', 'savings_usd', 'has_loan', 'loan_amount_usd'
    ]
    
    X = data[feature_cols]
    y = data['credit_score']
    
    X_encoded = pd.get_dummies(X)
    
    model_columns = list(X_encoded.columns)
    joblib.dump(model_columns, 'model_columns.pkl')
    
    return X_encoded, y

def train_model():
    X_encoded, y = prepare_data()
    
    X_train, X_test, y_train, y_test = train_test_split(X_encoded, y, test_size=0.2, random_state=42)
    
    rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
    rf_model.fit(X_train, y_train)
    
    y_pred = rf_model.predict(X_test)
    print(f"Accuracy: {accuracy_score(y_test, y_pred) * 100:.2f}%")
    
    joblib.dump(rf_model, 'model.pkl')

if __name__ == "__main__":
    train_model()