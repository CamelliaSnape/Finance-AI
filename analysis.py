import customtkinter as ctk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import pandas as pd

import customtkinter as ctk

from utils import *

class AnalysisPage(ctk.CTkFrame):

    def __init__(self, master):

        super().__init__(master)

        self.pack(fill="both", expand=True)

        self.load_data()

        self.create_header()

        self.create_charts()

    # ==================================

    def load_data(self):

        try:

            self.df = pd.read_csv(
                "data/Personal_Finance_Dataset.csv"
            )

        except:

            self.df = pd.DataFrame()

    # ==================================

    def create_header(self):

        ctk.CTkLabel(

            self,

            text="Phân tích chi tiêu",

            font=("Segoe UI",30,"bold")

        ).pack(anchor="w", padx=20, pady=20)

    # ==================================

    def create_charts(self):

        body = ctk.CTkFrame(self)

        body.pack(fill="both", expand=True, padx=20, pady=10)

        body.grid_columnconfigure((0,1), weight=1)
        body.grid_rowconfigure((0,1), weight=1)

        self.month_chart(body)

        self.category_chart(body)

        self.type_chart(body)

        self.summary(body)

    # ==================================

    def month_chart(self, parent):

        frame = ctk.CTkFrame(parent)

        frame.grid(row=0,column=0,padx=10,pady=10,sticky="nsew")

        ctk.CTkLabel(

            frame,

            text="Chi tiêu theo tháng",

            font=("Segoe UI",18,"bold")

        ).pack()

        fig = plt.Figure(figsize=(5,3))

        ax = fig.add_subplot(111)

        if not self.df.empty:

            month = self.df.groupby("Month")["Amount"].sum()

            ax.bar(month.index.astype(str), month.values)

        canvas = FigureCanvasTkAgg(fig,frame)

        canvas.draw()

        canvas.get_tk_widget().pack(fill="both",expand=True)

    # ==================================

    def category_chart(self,parent):

        frame = ctk.CTkFrame(parent)

        frame.grid(row=0,column=1,padx=10,pady=10,sticky="nsew")

        ctk.CTkLabel(

            frame,

            text="Chi tiêu theo danh mục",

            font=("Segoe UI",18,"bold")

        ).pack()

        fig=plt.Figure(figsize=(5,3))

        ax=fig.add_subplot(111)

        if not self.df.empty:

            category=self.df.groupby("Category")["Amount"].sum()

            ax.pie(

                category.values,

                labels=category.index,

                autopct="%1.1f%%"

            )

        canvas=FigureCanvasTkAgg(fig,frame)

        canvas.draw()

        canvas.get_tk_widget().pack(fill="both",expand=True)

    # ==================================

    def type_chart(self,parent):

        frame=ctk.CTkFrame(parent)

        frame.grid(row=1,column=0,padx=10,pady=10,sticky="nsew")

        ctk.CTkLabel(

            frame,

            text="Income vs Expense",

            font=("Segoe UI",18,"bold")

        ).pack()

        fig=plt.Figure(figsize=(5,3))

        ax=fig.add_subplot(111)

        if not self.df.empty:

            t=self.df.groupby("Type")["Amount"].sum()

            ax.bar(t.index,t.values)

        canvas=FigureCanvasTkAgg(fig,frame)

        canvas.draw()

        canvas.get_tk_widget().pack(fill="both",expand=True)

    # ==================================

    def summary(self,parent):

        frame=ctk.CTkFrame(parent)

        frame.grid(row=1,column=1,padx=10,pady=10,sticky="nsew")

        ctk.CTkLabel(

            frame,

            text="Nhận xét",

            font=("Segoe UI",18,"bold")

        ).pack(pady=10)

        textbox=ctk.CTkTextbox(frame)

        textbox.pack(fill="both",expand=True,padx=15,pady=10)

        if self.df.empty:

            textbox.insert(
                "0.0",
                "Không có dữ liệu."
            )

        else:

            total=self.df["Amount"].sum()

            max_category=self.df.groupby("Category")["Amount"].sum().idxmax()

            textbox.insert(
                "0.0",
                f"""Tổng giao dịch:

{total:,.0f} đ

Danh mục chi nhiều nhất:

{max_category}

AI Advisor sẽ phân tích
chi tiết tại trang AI Advisor."""
            )

        textbox.configure(state="disabled")