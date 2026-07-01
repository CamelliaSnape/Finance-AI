import joblib
import numpy as np

def predict_spending(income, age, model_path='model.pkl'):
    try:
        model = joblib.load(model_path)
        input_data = np.array([[income, age]])
        prediction = model.predict(input_data)
        return prediction[0]
    except FileNotFoundError:
        return "Error: model.pkl file not found."
    except Exception as e:
        return f"Error occurred: {str(e)}"

if __name__ == "__main__":
    result = predict_spending(50, 30)
    print(f"Test prediction result: {result}")