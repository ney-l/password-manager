from tkinter import *


window = Tk()
window.title("My Password Manager")
window.config(padx=10, pady=20)
window.geometry("+1+1")

canvas = Canvas(width=200, height=200, )
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=0, row=0)

window.mainloop()
