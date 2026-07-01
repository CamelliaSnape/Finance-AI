import customtkinter as ctk
import pandas as pd
import joblib
import os
import customtkinter as ctk

from utils import *

class AdvisorPage(ctk.CTkFrame):

    def __init__(self, master):

        super().__init__(master)

        self.pack(fill="both", expand=True)

        self.load_data()

        self.load_model()

        self.build_ui()

    # ==================================

    def load_data(self):

        try:

            self.df = pd.read_csv(
                "data/Personal_Finance_Dataset.csv"
            )

        except:

            self.df = pd.DataFrame()

    # ==================================

    def load_model(self):

        self.model = None

        if os.path.exists("model/spending_model.pkl"):

            self.model = joblib.load(
                "model/spending_model.pkl"
            )

    # ==================================

    def build_ui(self):

        title = ctk.CTkLabel(

            self,

            text="AI Advisor",

            font=("Segoe UI",30,"bold")

        )

        title.pack(anchor="w", padx=20, pady=(20,10))

        self.text = ctk.CTkTextbox(

            self,

            font=("Segoe UI",16)

        )

        self.text.pack(

            fill="both",

            expand=True,

            padx=20,

            pady=20

        )

        self.generate()

    # ==================================

    def generate(self):

        self.text.delete("1.0","end")

        if self.df.empty:

            self.text.insert(

                "end",

                "Không có dữ liệu."

            )

            return

        income = self.df[

            self.df["Type"]=="Income"

        ]["Amount"].sum()

        expense = self.df[

            self.df["Type"]=="Expense"

        ]["Amount"].sum()

        balance = income-expense

        category = self.df.groupby(

            "Category"

        )["Amount"].sum().idxmax()

        amount = self.df.groupby(

            "Category"

        )["Amount"].sum().max()

        advice = f"""

FINANCE AI REPORT

=====================================

Tổng thu nhập:

{income:,.0f} đ

-------------------------------------

Tổng chi tiêu:

{expense:,.0f} đ

-------------------------------------

Số dư hiện tại:

{balance:,.0f} đ

-------------------------------------

Danh mục chi nhiều nhất:

{category}

Giá trị:

{amount:,.0f} đ

=====================================

Đề xuất

• Hạn chế chi tiêu cho danh mục trên.

• Nên dành khoảng 20% thu nhập để tiết kiệm.

• Theo dõi chi tiêu hằng tuần.

• Tránh phát sinh các khoản mua sắm không cần thiết.

• Duy trì số dư dương mỗi tháng.

"""

        self.text.insert(

            "end",

            advice

        )

        self.text.configure(

            state="disabled"

        )