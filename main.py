import customtkinter as ctk

from login import LoginPage
from register import RegisterPage
from gui import GUI

# ==========================
# Theme
# ==========================

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")


class App(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("Finance AI")
        self.geometry("1500x900")

        self.current_frame = None
        self.current_user = None

        self.protocol("WM_DELETE_WINDOW", self.on_close)

        self.show_login()

    # ==========================
    # Đóng chương trình
    # ==========================

    def on_close(self):
        self.destroy()

    # ==========================
    # Xóa Frame hiện tại
    # ==========================

    def clear(self):

        if self.current_frame is not None:
            self.current_frame.destroy()
            self.current_frame = None

    # ==========================
    # Login
    # ==========================

    def show_login(self):

        self.geometry("500x650")

        self.clear()

        self.current_frame = LoginPage(
            self,
            self.login_success,
            self.show_register
        )

        self.current_frame.pack(fill="both", expand=True)

    # ==========================
    # Register
    # ==========================

    def show_register(self):

        self.geometry("500x650")

        self.clear()

        self.current_frame = RegisterPage(
            self,
            self.show_login
        )

        self.current_frame.pack(fill="both", expand=True)

    # ==========================
    # Dashboard
    # ==========================

    def login_success(self, user):

        self.current_user = user

        self.geometry("1500x900")

        self.clear()

        self.current_frame = GUI(
            self,
            user,
            self.show_login
        )

        self.current_frame.pack(fill="both", expand=True)


if __name__ == "__main__":
    app = App()
    app.mainloop()