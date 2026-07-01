import pandas as pd
import mysql.connector

# Đọc file CSV
df = pd.read_csv("finance_dataset_with_user_info.csv")

# Chỉ lấy các cột của bảng users
users = df[
    [
        "user_id",
        "age",
        "gender",
        "education_level",
        "employment_status",
        "job_title",
        "monthly_income_usd",
        "savings_usd",
        "has_loan",
        "loan_amount_usd",
        "credit_score",
    ]
].drop_duplicates(subset=["user_id"])

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",      # đổi nếu root có mật khẩu
    database="finance_ai"
)

cursor = conn.cursor()

sql = """
INSERT INTO users
(user_id,
age,
gender,
education_level,
employment_status,
job_title,
monthly_income_usd,
savings_usd,
has_loan,
loan_amount_usd,
credit_score)

VALUES
(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
"""

for row in users.itertuples(index=False):
    cursor.execute(sql, tuple(row))

conn.commit()

print("Import Users thành công!")

cursor.close()
conn.close()
