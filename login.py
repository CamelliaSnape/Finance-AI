import customtkinter as ctk
from tkinter import messagebox

from database import Database


class LoginPage(ctk.CTkFrame):

    def __init__(self, master, login_success, show_register):
        super().__init__(master)

        self.db = Database()

        self.login_success = login_success
        self.show_register = show_register

        self.build_ui()

    # ==========================
    # Giao diện
    # ==========================

    def build_ui(self):

        container = ctk.CTkFrame(self, width=420)
        container.pack(expand=True)

        ctk.CTkLabel(
            container,
            text="Finance AI",
            font=("Segoe UI", 32, "bold")
        ).pack(pady=(40, 10))

        ctk.CTkLabel(
            container,
            text="Đăng nhập",
            font=("Segoe UI", 20)
        ).pack(pady=(0, 25))

        ctk.CTkLabel(
            container,
            text="Tên đăng nhập"
        ).pack(anchor="w", padx=35)

        self.username = ctk.CTkEntry(
            container,
            width=340,
            height=40
        )
        self.username.pack(pady=(5, 15))

        ctk.CTkLabel(
            container,
            text="Mật khẩu"
        ).pack(anchor="w", padx=35)

        self.password = ctk.CTkEntry(
            container,
            show="*",
            width=340,
            height=40
        )
        self.password.pack(pady=(5, 25))

        # Enter để đăng nhập
        self.username.bind("<Return>", lambda e: self.login())
        self.password.bind("<Return>", lambda e: self.login())

        ctk.CTkButton(
            container,
            text="Đăng nhập",
            width=340,
            height=45,
            command=self.login
        ).pack()

        ctk.CTkButton(
            container,
            text="Đăng ký tài khoản",
            fg_color="transparent",
            text_color="#2F80ED",
            hover=False,
            command=self.show_register
        ).pack(pady=20)

    # ==========================
    # Đăng nhập
    # ==========================

    def login(self):

        username = self.username.get().strip()
        password = self.password.get().strip()

        if not username or not password:
            messagebox.showwarning(
                "Thông báo",
                "Vui lòng nhập đầy đủ tên đăng nhập và mật khẩu."
            )
            return

        try:
            user = self.db.login_user(username, password)

            if user:

                messagebox.showinfo(
                    "Đăng nhập thành công",
                    f"Xin chào {user[1]}!"
                )

                # Chuyển sang giao diện chính
                self.login_success(user)

            else:

                messagebox.showerror(
                    "Đăng nhập thất bại",
                    "Sai tên đăng nhập hoặc mật khẩu."
                )

        except Exception as e:

            messagebox.showerror(
                "Lỗi",
                str(e)
            )