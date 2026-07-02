import joblib
import pandas as pd

def get_prediction(age, gender, education_level, employment_status, job_title, 
                   monthly_income_usd, savings_usd, has_loan, loan_amount_usd):
    try:
        model = joblib.load('model.pkl')
        model_columns = joblib.load('model_columns.pkl')
        
        input_dict = {
            'age': [float(age)], 
            'gender': [str(gender)], 
            'education_level': [str(education_level)],
            'employment_status': [str(employment_status)], 
            'job_title': [str(job_title)],
            'monthly_income_usd': [float(monthly_income_usd)], 
            'savings_usd': [float(savings_usd)],
            'has_loan': [str(has_loan)], 
            'loan_amount_usd': [float(loan_amount_usd)]
        }
        
        input_df = pd.DataFrame(input_dict)
        input_encoded = pd.get_dummies(input_df)
        
        final_input = pd.DataFrame(0, index=[0], columns=model_columns)
        
        for col in input_encoded.columns:
            if col in final_input.columns:
                final_input[col] = input_encoded[col].values
            else:
                prefix_col = f"{col}_{input_df[col].iloc[0]}"
                if prefix_col in final_input.columns:
                    final_input[prefix_col] = 1
                    
        prediction = model.predict(final_input)
        return prediction[0]
        
    except Exception as e:
        return f"Error: {str(e)}"