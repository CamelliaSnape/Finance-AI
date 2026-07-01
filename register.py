import customtkinter as ctk
from tkinter import messagebox
from database import Database


class RegisterPage(ctk.CTkFrame):

    def __init__(self, master, show_login):

        super().__init__(master)

        self.db = Database()
        self.show_login = show_login

        self.build_ui()

    def build_ui(self):

        container = ctk.CTkFrame(self, width=450)
        container.pack(expand=True)

        ctk.CTkLabel(
            container,
            text="Đăng ký tài khoản",
            font=("Segoe UI", 30, "bold")
        ).pack(pady=(30, 25))

        # Họ tên
        ctk.CTkLabel(container, text="Họ và tên").pack(anchor="w", padx=40)

        self.fullname = ctk.CTkEntry(container, width=350, height=40)
        self.fullname.pack(pady=(5, 15))

        # Username
        ctk.CTkLabel(container, text="Tên đăng nhập").pack(anchor="w", padx=40)

        self.username = ctk.CTkEntry(container, width=350, height=40)
        self.username.pack(pady=(5, 15))

        # Email
        ctk.CTkLabel(container, text="Email").pack(anchor="w", padx=40)

        self.email = ctk.CTkEntry(container, width=350, height=40)
        self.email.pack(pady=(5, 15))

        # Password
        ctk.CTkLabel(container, text="Mật khẩu").pack(anchor="w", padx=40)

        self.password = ctk.CTkEntry(
            container,
            show="*",
            width=350,
            height=40
        )
        self.password.pack(pady=(5, 15))

        # Confirm
        ctk.CTkLabel(
            container,
            text="Nhập lại mật khẩu"
        ).pack(anchor="w", padx=40)

        self.confirm = ctk.CTkEntry(
            container,
            show="*",
            width=350,
            height=40
        )
        self.confirm.pack(pady=(5, 25))

        self.confirm.bind("<Return>", lambda e: self.register())

        ctk.CTkButton(
            container,
            text="Đăng ký",
            width=350,
            height=45,
            command=self.register
        ).pack()

        ctk.CTkButton(
            container,
            text="Đã có tài khoản? Đăng nhập",
            fg_color="transparent",
            text_color="#2F80ED",
            hover=False,
            command=self.show_login
        ).pack(pady=20)

    def register(self):

        fullname = self.fullname.get().strip()
        username = self.username.get().strip()
        email = self.email.get().strip()
        password = self.password.get()
        confirm = self.confirm.get()

        if not fullname or not username or not email or not password or not confirm:

            messagebox.showwarning(
                "Thông báo",
                "Vui lòng nhập đầy đủ thông tin."
            )
            return

        if "@" not in email or "." not in email:

            messagebox.showwarning(
                "Thông báo",
                "Email không hợp lệ."
            )
            return

        if password != confirm:

            messagebox.showerror(
                "Thông báo",
                "Mật khẩu không khớp."
            )
            return

        try:

            self.db.register_user(
                fullname,
                username,
                email,
                password
            )

            messagebox.showinfo(
                "Thành công",
                "Đăng ký tài khoản thành công!"
            )

            self.fullname.delete(0, "end")
            self.username.delete(0, "end")
            self.email.delete(0, "end")
            self.password.delete(0, "end")
            self.confirm.delete(0, "end")

            self.show_login()

        except Error as e:
            raise Exception(str(e))