from tkinter import *
from password_manager import PasswordManager

FONT_NAME = "Arial"
frequently_used_email = "someone@somewhere.com"

window = Tk()
window.title("My Password Manager")
window.config(padx=50, pady=50)
# window.geometry("+1+1")  # Shows window at the top left of the screen (personal preference)

# Render Logo
canvas = Canvas(width=200, height=200, )
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)


# Render form
def render_label(label, column, row):
    """Takes label and grid position, renders them on the screen
    and returns the Tkinter's Label element"""
    label_element = Label(text=f"{label}:", font=(FONT_NAME, 20))
    label_element.grid(column=column, row=row)
    return label_element


render_label("Website", column=0, row=1)
render_label("Email/Username", column=0, row=2)
render_label("Password", column=0, row=3)


def render_input(width, column, row, columnspan=1):
    """Takes width and grid position, renders them on the screen
    and returns the Tkinter's Entry element"""
    input_element = Entry(width=width)
    input_element.grid(column=column, row=row, columnspan=columnspan)
    return input_element


website_input = render_input(width=26, column=1, row=1)
website_input.focus()

username_input = render_input(width=43, column=1, row=2, columnspan=2)
username_input.insert(END, frequently_used_email)

password_input = render_input(width=26, column=1, row=3)


def render_button(text, column, row, width, columnspan=1):
    button_element = Button(text=text, width=width)
    button_element.grid(column=column, row=row, columnspan=columnspan)
    return button_element


generate_button = render_button(
    text="Generate Password",
    column=2,
    row=3,
    width=12
)

search_button = render_button(
    text="Search",
    column=2,
    row=1,
    width=12
)

add_button = render_button(
    text="Add",
    column=1,
    row=4,
    width=41,
    columnspan=2,
)

password_manager = PasswordManager(
    website_input,
    username_input,
    password_input
)


def save():
    is_valid = password_manager.validate()

    if is_valid:
        is_ok = password_manager.confirm()
        if is_ok:
            password_manager.save_to_file()
            password_manager.clear_entries()


add_button.config(command=save)
generate_button.config(command=password_manager.generate_password)
search_button.config(command=password_manager.find_password)

window.mainloop()
