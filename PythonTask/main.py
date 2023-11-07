import tkinter
import customtkinter
from tkinter import filedialog as fd
from tkinter import ttk

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("green")

app = customtkinter.CTk()
app.geometry("720x480")
app.title("CSV to HTML")

title = customtkinter.CTkLabel(app, text="CSV TO HTML")
title.pack()

def select_csv():
    file_name = fd.askopenfilename(title = "Select file",filetypes = (("CSV Files","*.csv"),))

    open_button.destroy()

open_button = ttk.Button(
    app,
    text='Open a File',
    command=select_csv
)

open_button.pack(expand=True)

app.mainloop()