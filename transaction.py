import customtkinter as ctk
from tkinter import ttk


class TransactionPage(ctk.CTkFrame):

    def __init__(self, master, state):
        super().__init__(master)

        self.state = state

        self.create_title()
        self.create_form()
        self.create_table()

        self.refresh_table()

    # ==========================
    # TITLE
    # ==========================

    def create_title(self):

        ctk.CTkLabel(
            self,
            text="Quản lý giao dịch",
            font=("Segoe UI", 28, "bold")
        ).pack(anchor="w", padx=20, pady=(20, 10))

    # ==========================
    # FORM
    # ==========================

    def create_form(self):

        form = ctk.CTkFrame(self)
        form.pack(fill="x", padx=20)

        form.grid_columnconfigure((0, 1, 2, 3), weight=1)

        # Date
        ctk.CTkLabel(form, text="Ngày").grid(row=0, column=0, padx=10, pady=8)
        self.date_entry = ctk.CTkEntry(form)
        self.date_entry.grid(row=1, column=0, padx=10, pady=5, sticky="ew")

        # Category
        ctk.CTkLabel(form, text="Danh mục").grid(row=0, column=1)
        self.category = ctk.CTkComboBox(
            form,
            values=["Food", "Shopping", "Transport", "Salary", "Entertainment", "Bills", "Investment", "Other"]
        )
        self.category.set("Food")   # 🔥 FIX
        self.category.grid(row=1, column=1, padx=10, pady=5, sticky="ew")

        # Type
        ctk.CTkLabel(form, text="Loại").grid(row=0, column=2)
        self.type = ctk.CTkComboBox(
            form,
            values=["Income", "Expense"]
        )
        self.type.set("Expense")   # 🔥 FIX
        self.type.grid(row=1, column=2, padx=10, pady=5, sticky="ew")

        # Amount
        ctk.CTkLabel(form, text="Số tiền").grid(row=0, column=3)
        self.amount = ctk.CTkEntry(form)
        self.amount.grid(row=1, column=3, padx=10, pady=5, sticky="ew")

        # Description
        ctk.CTkLabel(form, text="Mô tả").grid(row=2, column=0, pady=(20, 5))
        self.description = ctk.CTkEntry(form)
        self.description.grid(row=3, column=0, columnspan=4, padx=10, sticky="ew")

        # ==========================
        # BUTTONS
        # ==========================

        button_frame = ctk.CTkFrame(form, fg_color="transparent")
        button_frame.grid(row=4, column=0, columnspan=4, pady=20)

        ctk.CTkButton(button_frame, text="Thêm", command=self.add_transaction).pack(side="left", padx=5)
        ctk.CTkButton(button_frame, text="Cập nhật", command=self.update_transaction).pack(side="left", padx=5)
        ctk.CTkButton(button_frame, text="Xóa", command=self.delete_transaction).pack(side="left", padx=5)
        ctk.CTkButton(button_frame, text="Làm mới", command=self.clear_form).pack(side="left", padx=5)

    # ==========================
    # TABLE
    # ==========================

    def create_table(self):

        table_frame = ctk.CTkFrame(self)
        table_frame.pack(fill="both", expand=True, padx=20, pady=20)

        columns = ("ID", "Date", "Category", "Type", "Amount", "Description")

        self.table = ttk.Treeview(table_frame, columns=columns, show="headings")

        for col in columns:
            self.table.heading(col, text=col)
            self.table.column(col, anchor="center", width=120)

        scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=self.table.yview)
        self.table.configure(yscrollcommand=scrollbar.set)

        self.table.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

    # ==========================
    # LOGIC
    # ==========================

    def add_transaction(self):

        date = self.date_entry.get()
        category = self.category.get()
        ttype = self.type.get()
        amount = self.amount.get()
        desc = self.description.get()

        if not date or not amount:
            print("Thiếu dữ liệu")
            return

        self.state.transactions.append((date, category, ttype, amount, desc))

        self.refresh_table()
        self.clear_form()

    def refresh_table(self):

        self.table.delete(*self.table.get_children())

        for i, row in enumerate(self.state.transactions, start=1):
            self.table.insert("", "end", values=(i, *row))

    def clear_form(self):

        self.date_entry.delete(0, "end")
        self.amount.delete(0, "end")
        self.description.delete(0, "end")

        self.category.set("Food")
        self.type.set("Expense")

    def delete_transaction(self):

        selected = self.table.selection()
        if not selected:
            return

        indexes = sorted(
            [int(self.table.item(i)["values"][0]) - 1 for i in selected],
            reverse=True
        )

        for idx in indexes:
            if 0 <= idx < len(self.state.transactions):
                self.state.transactions.pop(idx)

        self.refresh_table()

    def update_transaction(self):

        selected = self.table.selection()
        if not selected:
            return

        item = selected[0]
        idx = int(self.table.item(item)["values"][0]) - 1

        if 0 <= idx < len(self.state.transactions):

            self.state.transactions[idx] = (
                self.date_entry.get(),
                self.category.get(),
                self.type.get(),
                self.amount.get(),
                self.description.get()
            )

        self.refresh_table()