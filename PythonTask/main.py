import tkinter as tk 
from tkinter import scrolledtext
from tkinter import filedialog as fd
from tkinter import ttk
import customtkinter
import pandas as pd

#APP UI
customtkinter.set_appearance_mode("light") #Color scheme

app = customtkinter.CTk() #Name of program 
app.geometry("720x480") #Resolution
app.title("CSV to HTML") 

title = customtkinter.CTkLabel(app, text="CSV TO HTML")  #Text inside the program that says 'CSV TO HTML'
title.pack() #.pack is required to finish editing an element, always remember to pack your element as to not leave it open.


#MAIN FUNCTION
def select_csv():

    #SELECTS THE CSV FILE                                        Only allows CSV files, might change to allow EXCL too if i can figure it out
    csv = fd.askopenfilename(title = "Select file",filetypes = (("CSV Files","*.csv"),))

    datafile = pd.read_csv(csv)
    CSVData = datafile.to_html(index=False) #Translates the CSV file into HTML *CODE*, (INDEX FALSE MAKES THE INPUT WORK FOR SOME REASON I DONT KNOW)
    
    text_widget = scrolledtext.ScrolledText(app, width=300, height=400) #Widget is a box where text can be put and can have its own scrollbar 
    text_widget.insert(tk.INSERT, CSVData)
    text_widget.configure(state='disabled')
    text_widget.pack(padx=10, pady=40)

    open_button.destroy()


#BUTTONS
open_button = ttk.Button( #Need to make this AFTER the function to have it be listed in 'command'
    app, #where the button will go (plainly on the program)
    text='Open a File',
    command=select_csv) #Selects function to run
open_button.pack(expand=True)


app.mainloop() #Properly opens the app (Program)