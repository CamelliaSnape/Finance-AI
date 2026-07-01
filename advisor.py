from pathlib import Path
import pandas as pd

# Đọc dữ liệu
current_folder = Path(__file__).parent
csv_file = current_folder / "personal_finance_dataset_8000_extended.csv"
df = pd.read_csv(csv_file)

print("===== PERSONAL FINANCIAL ADVISOR =====\n")

# Danh mục chi tiêu nhiều nhất
top_category = df["Category"].value_counts().idxmax()

print(f"Danh mục chi tiêu nhiều nhất: {top_category}")

if top_category == "Online Shopping":
    print("Lời khuyên: Bạn nên kiểm soát việc mua sắm trực tuyến để tránh vượt ngân sách.")
elif top_category == "Food":
    print("Lời khuyên: Hãy lập kế hoạch ăn uống hợp lý để tiết kiệm chi phí.")
elif top_category == "Entertainment":
    print("Lời khuyên: Có thể giảm một phần chi phí giải trí nếu muốn tiết kiệm.")
else:
    print("Lời khuyên: Hãy theo dõi các khoản chi tiêu thường xuyên.")

# Phương thức thanh toán phổ biến
top_payment = df["PaymentMethod"].value_counts().idxmax()
print(f"\nPhương thức thanh toán được sử dụng nhiều nhất: {top_payment}")

# Thời điểm giao dịch nhiều nhất
top_time = df["TimeOfDay"].value_counts().idxmax()
print(f"Thời gian giao dịch nhiều nhất: {top_time}")