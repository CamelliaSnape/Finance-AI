import prediction

def predict_spending(age, gender, education_level, employment_status, job_title, 
                    monthly_income_usd, savings_usd, has_loan, loan_amount_usd):
    return prediction.get_prediction(
        age, gender, education_level, employment_status, job_title,
        monthly_income_usd, savings_usd, has_loan, loan_amount_usd
    )

if __name__ == "__main__":
    result = predict_spending(30, 'Male', 'Bachelor', 'Employed', 'Engineer', 2500, 10000, 'No', 0)
    print(f"Test result: {result}")