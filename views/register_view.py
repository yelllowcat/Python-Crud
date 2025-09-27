
import tkinter


class RegisterView(tkinter.Toplevel):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.title("Register")
        self.geometry("400x300")
        self.resizable(width=False, height=False)

        self.username_label = tkinter.Label(self, text="Username:")
        self.username_entry = tkinter.Entry(self)
        self.username_label.pack(pady=10)
        self.username_entry.pack(pady=10)

        self.password_label = tkinter.Label(self, text="Password:")
        self.password_entry = tkinter.Entry(self, show="*")
        self.password_label.pack(pady=10)
        self.password_entry.pack(pady=10)

        self.confirm_password_label = tkinter.Label(self, text="Confirm Password:")
        self.confirm_password_entry = tkinter.Entry(self, show="*")
        self.confirm_password_label.pack(pady=10)
        self.confirm_password_entry.pack(pady=10)

        self.register_button = tkinter.Button(self, text="Register", command=self._default_register)
        self.register_button.pack(pady=20)
        self.protocol("WM_DELETE_WINDOW", self._on_close)