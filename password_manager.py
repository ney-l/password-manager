import json
from tkinter import messagebox
from tkinter import END
import pyperclip

from password_generator import PasswordGenerator


class PasswordManager(PasswordGenerator):
    def __init__(self, website_input, username_input, password_input):
        super().__init__()

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
        self.password = self.generate_random_password()
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
            message=f"These are the details: \n\nEmail:\n {self.username}\n\n" \
                    f"Password:\n {self.password} \n\nIs it ok to save?"
        )
        return is_ok

    def clear_entries(self):
        self.website_input.delete(0, END)
        self.password_input.delete(0, END)

    def save_to_file(self):
        self.update_entries()
        new_data = {
            self.website: {
                "username": self.username,
                "password": self.password
            }
        }

        data = self.load_saved_passwords()
        data.update(new_data)
        # Save updated data
        with open("data.json", mode="w") as file:
            json.dump(data, file, indent=4)

    def load_saved_passwords(self):
        try:
            with open("data.json", mode="r") as file:
                data = json.load(file)
        except FileNotFoundError:
            with open("data.json", mode="w") as file:
                data = {}
                json.dump(data, file, indent=4)
        finally:
            return data

    def find_password(self):
        self.update_entries()
        data = self.load_saved_passwords()
        try:
            credentials = data[self.website]
            username = credentials["username"]
            password = credentials["password"]
            messagebox.showinfo(
                title=self.website,
                message=f"Website:\n {self.website}\n\n"
                        f"Username:\n {username}\n\n"
                        f"Password:\n {password}"
            )
        except KeyError:
            messagebox.showerror(message="No details for the website exists")