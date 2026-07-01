import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
import joblib

np.random.seed(42)
data = pd.DataFrame({
    'Income': np.random.randint(10, 100, 500),
    'Age': np.random.randint(18, 65, 500),
    'Spending_Amount': np.random.randint(1, 95, 500)
})

def label_spending(amount):
    if amount < 30: return 'Low'
    elif amount < 70: return 'Medium'
    else: return 'High'

data['Spending_Label'] = data['Spending_Amount'].apply(label_spending)

X = data[['Income', 'Age']]
y = data['Spending_Label']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print("--- Training RandomForest Model ---")
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)

y_pred = rf_model.predict(X_test)
print(f"Accuracy: {accuracy_score(y_test, y_pred) * 100:.2f}%")
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

joblib.dump(rf_model, 'model.pkl')
print("-> Model saved successfully as 'model.pkl'")