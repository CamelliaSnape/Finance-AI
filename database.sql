DROP DATABASE IF EXISTS finance_ai;
CREATE DATABASE finance_ai;
USE finance_ai;

-- =====================================
-- USERS
-- =====================================

CREATE TABLE users (
    user_id INT PRIMARY KEY,

    age INT NOT NULL,

    gender ENUM('Male','Female'),

    education_level VARCHAR(50),

    employment_status VARCHAR(50),

    job_title VARCHAR(100),

    monthly_income_usd DECIMAL(12,2),

    savings_usd DECIMAL(12,2),

    has_loan ENUM('Yes','No'),

    loan_amount_usd DECIMAL(12,2),

    credit_score INT
);

-- =====================================
-- TRANSACTIONS
-- =====================================

CREATE TABLE transactions (

    transaction_id INT AUTO_INCREMENT PRIMARY KEY,

    user_id INT NOT NULL,

    transaction_date DATE,

    description VARCHAR(255),

    category VARCHAR(100),

    amount DECIMAL(12,2),

    payment_method VARCHAR(50),

    location VARCHAR(100),

    account_type VARCHAR(50),

    transaction_type ENUM('Income','Expense'),

    device_used VARCHAR(50),

    currency VARCHAR(20),

    merchant_type VARCHAR(100),

    loyalty_program VARCHAR(50),

    weekday VARCHAR(20),

    month INT,

    year INT,

    day INT,

    day_of_week VARCHAR(20),

    time_of_day VARCHAR(30),

    FOREIGN KEY(user_id)
        REFERENCES users(user_id)
);
CREATE TABLE budget(

    budget_id INT AUTO_INCREMENT PRIMARY KEY,

    user_id INT,

    month INT,

    year INT,

    budget_amount DECIMAL(12,2),

    FOREIGN KEY(user_id)
    REFERENCES users(user_id)
);
CREATE TABLE ai_prediction(

    prediction_id INT AUTO_INCREMENT PRIMARY KEY,

    user_id INT,

    predicted_expense DECIMAL(12,2),

    spending_level ENUM(
        'Saver',
        'Normal',
        'Overspending'
    ),

    predict_date DATE,

    FOREIGN KEY(user_id)
    REFERENCES users(user_id)
);
