from pathlib import Path
import pandas as pd

current_folder = Path(__file__).parent
csv_file = current_folder / "personal_finance_dataset_8000_extended.csv"
df = pd.read_csv(csv_file)
print(df.head())
print("\n===== THÔNG TIN DỮ LIỆU =====")
print(df.info())
print("\n===== THỐNG KÊ =====")
# Tổng số giao dịch
print("Tổng số giao dịch:", len(df))
# Tổng số tiền
print("Tổng số tiền:", df["Amount"].sum())
# Số tiền trung bình
print("Số tiền trung bình:", df["Amount"].mean())
# Giao dịch lớn nhất
print("Giao dịch lớn nhất:", df["Amount"].max())
# Giao dịch nhỏ nhất
print("Giao dịch nhỏ nhất:", df["Amount"].min())

print("\n===== THỐNG KÊ CATEGORY =====")
print(df["Category"].value_counts())

print("\n===== PHƯƠNG THỨC THANH TOÁN =====")
print(df["PaymentMethod"].value_counts())

print("\n===== THỜI GIAN GIAO DỊCH =====")
print(df["TimeOfDay"].value_counts())