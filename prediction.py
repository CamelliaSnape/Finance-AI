import customtkinter as ctk

from utils import *
from tkinter import messagebox
import joblib
import os
import numpy as np


class PredictionPage(ctk.CTkFrame):

    def __init__(self, master):

        super().__init__(master)

        self.model = None
        self.category_encoder = None
        self.type_encoder = None

        self.load_models()

        self.create_ui()

    # ==========================================
    # LOAD MODEL
    # ==========================================

    def load_models(self):

        try:

            if os.path.exists("spending_model.pkl"):
                self.model = joblib.load("spending_model.pkl")

            elif os.path.exists("model/spending_model.pkl"):
                self.model = joblib.load("model/spending_model.pkl")

            if os.path.exists("category_encoder.pkl"):
                self.category_encoder = joblib.load("category_encoder.pkl")

            elif os.path.exists("model/category_encoder.pkl"):
                self.category_encoder = joblib.load("model/category_encoder.pkl")

            if os.path.exists("type_encoder.pkl"):
                self.type_encoder = joblib.load("type_encoder.pkl")

            elif os.path.exists("model/type_encoder.pkl"):
                self.type_encoder = joblib.load("model/type_encoder.pkl")

        except Exception as e:

            messagebox.showerror("Lỗi", str(e))

    # ==========================================
    # UI
    # ==========================================

    def create_ui(self):

        title = ctk.CTkLabel(
            self,
            text="Dự đoán AI",
            font=("Segoe UI",30,"bold")
        )

        title.pack(pady=20)

        form = ctk.CTkFrame(self)

        form.pack(padx=20,pady=10)

        ctk.CTkLabel(
            form,
            text="Danh mục"
        ).grid(row=0,column=0,padx=10,pady=10)

        self.category = ctk.CTkComboBox(
            form,
            values=[
                "Food",
                "Shopping",
                "Transport",
                "Bills",
                "Salary",
                "Investment",
                "Entertainment",
                "Other"
            ]
        )

        self.category.grid(row=0,column=1,padx=10)

        ctk.CTkLabel(
            form,
            text="Loại"
        ).grid(row=1,column=0,padx=10,pady=10)

        self.type = ctk.CTkComboBox(
            form,
            values=[
                "Income",
                "Expense"
            ]
        )

        self.type.grid(row=1,column=1)

        ctk.CTkLabel(
            form,
            text="Số tiền"
        ).grid(row=2,column=0,padx=10,pady=10)

        self.amount = ctk.CTkEntry(form)

        self.amount.grid(row=2,column=1)

        ctk.CTkButton(
            self,
            text="Dự đoán",
            width=200,
            command=self.predict
        ).pack(pady=25)

        self.result = ctk.CTkTextbox(
            self,
            height=220,
            font=("Segoe UI",16)
        )

        self.result.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=20
        )

    # ==========================================
    # PREDICT
    # ==========================================

    def predict(self):

        self.result.delete("1.0","end")

        if self.model is None:

            self.result.insert(
                "end",
                "Không tìm thấy mô hình AI."
            )

            return

        try:

            category = self.category_encoder.transform(
                [self.category.get()]
            )[0]

            trans_type = self.type_encoder.transform(
                [self.type.get()]
            )[0]

            amount = float(
                self.amount.get()
            )

            X = np.array([
                [
                    category,
                    trans_type,
                    amount
                ]
            ])

            prediction = self.model.predict(X)[0]

            self.result.insert(
                "end",
                f"""KẾT QUẢ DỰ ĐOÁN

Danh mục:
{self.category.get()}

Loại:
{self.type.get()}

Số tiền:
{amount:,.0f} đ

-----------------------------------

Kết quả AI

{prediction}
"""
            )

        except Exception as e:

            messagebox.showerror(
                "Lỗi",
                str(e)
            )