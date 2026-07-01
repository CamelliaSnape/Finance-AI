import customtkinter as ctk
from tkinter import ttk

import customtkinter as ctk
from tkinter import ttk

import customtkinter as ctk

from utils import *
from utils.data_loader import FinanceData
from utils.charts import FinanceChart


class StatisticsPage(ctk.CTkFrame):

    def __init__(self, master, user_id):

        super().__init__(master)

        self.data = FinanceData(user_id)

        self.create_ui()

    # ======================================

    def create_ui(self):

        title = ctk.CTkLabel(
            self,
            text="Thống kê chi tiêu",
            font=("Segoe UI", 30, "bold")
        )

        title.pack(anchor="w", padx=20, pady=20)

        body = ctk.CTkFrame(self)

        body.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=10
        )

        body.grid_columnconfigure((0,1), weight=1)
        body.grid_rowconfigure((0,1), weight=1)

        # Income

        income_frame = ctk.CTkFrame(body)

        income_frame.grid(
            row=0,
            column=0,
            sticky="nsew",
            padx=10,
            pady=10
        )

        FinanceChart.line(

            income_frame,

            self.data.income_by_month(),

            "Thu nhập theo tháng"

        )

        # Expense

        expense_frame = ctk.CTkFrame(body)

        expense_frame.grid(
            row=0,
            column=1,
            sticky="nsew",
            padx=10,
            pady=10
        )

        FinanceChart.line(

            expense_frame,

            self.data.expense_by_month(),

            "Chi tiêu theo tháng"

        )

        # Pie

        pie_frame = ctk.CTkFrame(body)

        pie_frame.grid(
            row=1,
            column=0,
            sticky="nsew",
            padx=10,
            pady=10
        )

        FinanceChart.pie(

            pie_frame,

            self.data.expense_by_category(),

            "Chi tiêu theo danh mục"

        )

        # Top Expense

        table_frame = ctk.CTkFrame(body)

        table_frame.grid(
            row=1,
            column=1,
            sticky="nsew",
            padx=10,
            pady=10
        )

        ctk.CTkLabel(

            table_frame,

            text="Top 10 khoản chi",

            font=("Segoe UI",18,"bold")

        ).pack(pady=10)

        columns = (

            "Date",

            "Category",

            "Amount"

        )

        tree = ttk.Treeview(

            table_frame,

            columns=columns,

            show="headings",

            height=10

        )

        for col in columns:

            tree.heading(col, text=col)

            tree.column(

                col,

                anchor="center",

                width=120

            )

        top = self.data.top_expense()

        if top is not None:

            for _, row in top.iterrows():

                tree.insert(

                    "",

                    "end",

                    values=(

                        row["Date"].strftime("%d/%m/%Y"),

                        row["Category"],

                        f'{row["Amount"]:,.0f} đ'

                    )

                )

        tree.pack(

            fill="both",

            expand=True,

            padx=10,

            pady=10

        )