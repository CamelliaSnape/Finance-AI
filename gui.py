import customtkinter as ctk

from dashboard import DashboardPage
from transaction import TransactionPage
from analysis import AnalysisPage
from advisor import AdvisorPage
from prediction import PredictionPage
from report import ReportPage

from state import AppState
from utils import Session


class GUI(ctk.CTkFrame):

    def __init__(self, master, user, logout_callback):
        super().__init__(master)

        self.user = user
        self.logout_callback = logout_callback

        # App State
        self.app_state = AppState()
        self.app_state.set_user(user)

        # Layout
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        self.create_sidebar()
        self.create_container()
        self.create_pages()

        self.show_dashboard()

    # ==========================================
    # CONTAINER
    # ==========================================

    def create_container(self):

        self.container = ctk.CTkFrame(self)

        self.container.grid(
            row=0,
            column=1,
            sticky="nsew",
            padx=15,
            pady=15
        )

    # ==========================================
    # PAGE
    # ==========================================

    def create_pages(self):

        self.pages = {}

        self.pages["dashboard"] = DashboardPage(
            self.container,
            self.user,
            self.app_state
        )

        self.pages["transaction"] = TransactionPage(
            self.container,
            self.app_state
        )

        self.pages["analysis"] = self.safe_create(AnalysisPage)

        self.pages["advisor"] = self.safe_create(AdvisorPage)

        self.pages["prediction"] = self.safe_create(PredictionPage)

        self.pages["report"] = self.safe_create(
            ReportPage,
            need_user=True
        )

    def safe_create(self, page_class, need_user=False):

        try:

            if need_user:
                return page_class(
                    self.container,
                    self.user,
                    self.app_state
                )

            return page_class(
                self.container,
                self.app_state
            )

        except TypeError:

            if need_user:
                return page_class(
                    self.container,
                    self.user
                )

            return page_class(self.container)

    # ==========================================
    # SIDEBAR
    # ==========================================

    def create_sidebar(self):

        sidebar = ctk.CTkFrame(
            self,
            width=220,
            corner_radius=0
        )

        sidebar.grid(
            row=0,
            column=0,
            sticky="ns"
        )

        ctk.CTkLabel(
            sidebar,
            text="Finance AI",
            font=("Segoe UI", 28, "bold")
        ).pack(pady=30)

        menus = [

            ("Dashboard", self.show_dashboard),

            ("Transaction", self.show_transaction),

            ("Analysis", self.show_analysis),

            ("AI Advisor", self.show_advisor),

            ("Prediction", self.show_prediction),

            ("Report", self.show_report),

            ("Logout", self.logout)

        ]

        for text, command in menus:

            ctk.CTkButton(
                sidebar,
                text=text,
                width=180,
                height=42,
                command=command
            ).pack(pady=6)

    # ==========================================
    # PAGE
    # ==========================================

    def clear_container(self):

        for widget in self.container.winfo_children():
            widget.pack_forget()

    def show_dashboard(self):
        self.clear_container()
        self.pages["dashboard"].pack(fill="both", expand=True)

    def show_transaction(self):
        self.clear_container()
        self.pages["transaction"].pack(fill="both", expand=True)

    def show_analysis(self):
        self.clear_container()
        self.pages["analysis"].pack(fill="both", expand=True)

    def show_advisor(self):
        self.clear_container()
        self.pages["advisor"].pack(fill="both", expand=True)

    def show_prediction(self):
        self.clear_container()
        self.pages["prediction"].pack(fill="both", expand=True)

    def show_report(self):
        self.clear_container()
        self.pages["report"].pack(fill="both", expand=True)

    # ==========================================
    # LOGOUT
    # ==========================================

    def logout(self):

        Session.logout()

        self.logout_callback()