import customtkinter as ctk

from utils import *
from tkinter import filedialog, messagebox
import pandas as pd
from database import Database


class ReportPage(ctk.CTkFrame):

    def __init__(self, master, user_id):

        super().__init__(master)

        self.db = Database()
        self.user_id = user_id

        self.create_ui()

    # ==========================================

    def create_ui(self):

        title = ctk.CTkLabel(
            self,
            text="Xuất báo cáo",
            font=("Segoe UI",30,"bold")
        )

        title.pack(pady=20)

        button_frame = ctk.CTkFrame(self)

        button_frame.pack(pady=20)

        ctk.CTkButton(
            button_frame,
            text="Xuất CSV",
            width=180,
            command=self.export_csv
        ).grid(row=0,column=0,padx=10)

        ctk.CTkButton(
            button_frame,
            text="Xuất Excel",
            width=180,
            command=self.export_excel
        ).grid(row=0,column=1,padx=10)

        ctk.CTkTextbox(
            self,
            height=250
        ).pack(
            fill="both",
            expand=True,
            padx=20,
            pady=20
        )

    # ==========================================

    def get_dataframe(self):

        data = self.db.get_transactions(self.user_id)

        columns = [

            "ID",

            "User ID",

            "Date",

            "Category",

            "Type",

            "Amount",

            "Description"

        ]

        return pd.DataFrame(
            data,
            columns=columns
        )

    # ==========================================

    def export_csv(self):

        df = self.get_dataframe()

        path = filedialog.asksaveasfilename(

            defaultextension=".csv",

            filetypes=[

                ("CSV File","*.csv")

            ]

        )

        if path:

            df.to_csv(

                path,

                index=False,

                encoding="utf-8-sig"

            )

            messagebox.showinfo(

                "Thông báo",

                "Xuất CSV thành công."

            )

    # ==========================================

    def export_excel(self):

        df = self.get_dataframe()

        path = filedialog.asksaveasfilename(

            defaultextension=".xlsx",

            filetypes=[

                ("Excel File","*.xlsx")

            ]

        )

        if path:

            df.to_excel(

                path,

                index=False

            )

            messagebox.showinfo(

                "Thông báo",

                "Xuất Excel thành công."

            )