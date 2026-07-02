import joblib
import pandas as pd

def get_prediction(age, gender, education_level, employment_status, job_title, 
                   monthly_income_usd, savings_usd, has_loan, loan_amount_usd):
    try:
        model = joblib.load('model.pkl')
        model_columns = joblib.load('model_columns.pkl')
        
        input_dict = {
            'age': [age], 'gender': [gender], 'education_level': [education_level],
            'employment_status': [employment_status], 'job_title': [job_title],
            'monthly_income_usd': [monthly_income_usd], 'savings_usd': [savings_usd],
            'has_loan': [has_loan], 'loan_amount_usd': [loan_amount_usd]
        }
        
        input_df = pd.DataFrame(input_dict)
        input_encoded = pd.get_dummies(input_df)
        final_input = input_encoded.reindex(columns=model_columns, fill_value=0)
        
        prediction = model.predict(final_input)
        return prediction[0]
        
    except Exception as e:
        return f"Error: {str(e)}"