from tkinter import messagebox
from tkinter import END
import pyperclip

from password_generator import generate_random_password


class PasswordManager:
    def __init__(self, website_input, username_input, password_input):
        self.website_input = website_input
        self.username_input = username_input
        self.password_input = password_input
        self.website = ""
        self.username = ""
        self.password = ""

    def update_entries(self):
        self.website = self.website_input.get()
        self.username = self.username_input.get()
        self.password = self.password_input.get()

    def generate_password(self):
        self.password = generate_random_password()
        self.password_input.delete(0, "end")
        self.password_input.insert(0, self.password)
        pyperclip.copy(self.password)

    def validate(self):
        self.update_entries()
        if not self.website or not self.username or not self.password:
            messagebox.showerror(title="Oops", message="Please don't leave any fields empty!")
            return False
        return True

    def confirm(self):
        self.update_entries()
        is_ok = messagebox.askokcancel(
            title=self.website,
            message=f"These are the details: \n\nEmail: {self.username}\n" \
                    f"Password: {self.password} \n\nIs it ok to save?"
        )
        if not is_ok:
            return False
        return True

    def clear_entries(self):
        self.website_input.delete(0, END)
        self.password_input.delete(0, END)

    def save_to_file(self):
        print('called')
        self.update_entries()
        with open("data.txt", mode="a") as file:
            file.write(f"{self.website},{self.username},{self.password}\n")

