import customtkinter as ctk
from datetime import datetime


class DashboardPage(ctk.CTkFrame):

    def __init__(self, master, user, state):
        super().__init__(master)

        self.master = master
        self.user = user
        self.state = state

        self.create_ui()

    # ==========================
    def create_ui(self):

        self.sidebar = ctk.CTkFrame(self, width=220, corner_radius=0)
        self.sidebar.pack(side="left", fill="y")

        self.container = ctk.CTkFrame(self)
        self.container.pack(side="left", fill="both", expand=True)

        self.create_sidebar()
        self.show_dashboard()

    # ==========================
    def create_sidebar(self):

        ctk.CTkLabel(
            self.sidebar,
            text="Finance AI",
            font=("Segoe UI", 24, "bold")
        ).pack(pady=20)

        ctk.CTkButton(
            self.sidebar,
            text="Dashboard",
            command=self.show_dashboard
        ).pack(fill="x", padx=10, pady=5)

        ctk.CTkButton(
            self.sidebar,
            text="Transaction",
            command=self.show_transaction
        ).pack(fill="x", padx=10, pady=5)

    # ==========================
    def clear(self):
        for w in self.container.winfo_children():
            w.destroy()

    # ==========================
    def show_dashboard(self):

        self.clear()

        page = ctk.CTkFrame(self.container)
        page.pack(fill="both", expand=True)

        ctk.CTkLabel(
            page,
            text=f"Xin chào {self.user[1]}",
            font=("Segoe UI", 28, "bold")
        ).pack(anchor="w", padx=20, pady=20)

        ctk.CTkLabel(
            page,
            text=datetime.now().strftime("%d/%m/%Y"),
            font=("Segoe UI", 16)
        ).pack(anchor="w", padx=20)

    # ==========================
    def show_transaction(self):

        self.clear()

        ctk.CTkLabel(
            self.container,
            text="Transaction Page",
            font=("Segoe UI", 30)
        ).pack(expand=True)