from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

# Đường dẫn tới thư mục hiện tại
current_folder = Path(__file__).parent

# Đọc file CSV
csv_file = current_folder / "personal_finance_dataset_8000_extended.csv"
df = pd.read_csv(csv_file)

# Đếm số lượng giao dịch theo Category
category = df["Category"].value_counts()

# Vẽ biểu đồ cột
plt.figure(figsize=(8,5))
category.plot(kind="bar")

plt.title("Transactions by Category")
plt.xlabel("Category")
plt.ylabel("Number of Transactions")

plt.tight_layout()
plt.show()
 
# Biểu đồ Payment Method
payment = df["PaymentMethod"].value_counts()

plt.figure(figsize=(6,6))
payment.plot(kind="pie", autopct="%1.1f%%")
plt.title("Payment Method Distribution")
plt.ylabel("")
plt.tight_layout()
plt.show()

# Biểu đồ Time Of Day
time = df["TimeOfDay"].value_counts()

plt.figure(figsize=(7,5))
time.plot(kind="bar")

plt.title("Transactions by Time of Day")
plt.xlabel("Time of Day")
plt.ylabel("Number of Transactions")

plt.tight_layout()
plt.show()