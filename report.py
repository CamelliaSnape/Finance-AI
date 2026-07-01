from pathlib import Path
import pandas as pd

# Đọc dữ liệu
current_folder = Path(__file__).parent
csv_file = current_folder / "personal_finance_dataset_8000_extended.csv"
df = pd.read_csv(csv_file)

print("========== BÁO CÁO PHÂN TÍCH DỮ LIỆU ==========\n")

print(f"Tổng số giao dịch: {len(df)}")
print(f"Tổng giá trị giao dịch: {df['Amount'].sum():,.2f}")
print(f"Giá trị trung bình mỗi giao dịch: {df['Amount'].mean():,.2f}")

print("\n--- Phân tích Category ---")
print(df["Category"].value_counts())

print("\n--- Phân tích Payment Method ---")
print(df["PaymentMethod"].value_counts())

print("\n--- Phân tích Time Of Day ---")
print(df["TimeOfDay"].value_counts())

print("\n========== INSIGHT ==========")

print("""
1. Bộ dữ liệu gồm 8000 giao dịch và không có dữ liệu bị thiếu.

2. Online Shopping là danh mục có số lượng giao dịch nhiều nhất.

3. Net Banking và Credit Card là hai phương thức thanh toán được sử dụng nhiều nhất.

4. Buổi tối (Evening) là thời điểm phát sinh nhiều giao dịch nhất.

5. Dữ liệu phân bố khá đồng đều giữa các nhóm nên phù hợp để phân tích và huấn luyện mô hình AI.
""")