from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
import joblib
import analysis  # Import from analysis.py

def train_model():
    data = analysis.prepare_data()
    
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

    # Save model
    joblib.dump(rf_model, 'model.pkl')
    print("-> Model saved successfully as 'model.pkl'")

if __name__ == "__main__":
    train_model()