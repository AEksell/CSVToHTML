import tkinter as tk 
from tkinter import scrolledtext
from tkinter import filedialog as fd
from tkinter import ttk
from tkinter import PhotoImage
import customtkinter
import pandas as pd
import pyperclip

#APP UI
customtkinter.set_appearance_mode("light") #Color scheme

app = customtkinter.CTk() #Name of program 
app.geometry("720x480") #Resolution
app.title("CSV to HTML") 

title = customtkinter.CTkLabel(app, text="CSV TO HTML")  #Text inside the program that says 'CSV TO HTML'
title.pack() #.pack organizes the elements position, it is required to finish editing an element, always remember to pack your element.

#MAIN FUNCTION
def select_csv():

    #SELECTS THE CSV FILE                                        Only allows CSV files, might change to allow EXCL too if i can figure it out
    csv = fd.askopenfilename(title = "Select file",filetypes = (("CSV Files","*.csv"),))
    datafile = pd.read_csv(csv)
    CSVData = datafile.to_html(index=False) #Translates the CSV file into HTML *CODE*, (INDEX FALSE MAKES THE INPUT WORK FOR SOME REASON I DONT KNOW)
    
    textWidget = scrolledtext.ScrolledText(app, width=300, height=400) #Widget is a box where text can be put and can have its own scrollbar 
    textWidget.insert(tk.INSERT, CSVData)
    textWidget.configure(state='disabled')
    textWidget.pack(padx=50, pady=60)

    openButton.destroy()

    #CLIPBOARD COPY
    def copyToClipboard():
        currentText = textWidget.get("1.0", tk.END)
        pyperclip.copy(currentText)  # Replace with your actual text or data

    copy_button = ttk.Button(
        app, 
        text="Copy to Clipboard", 
        command=copyToClipboard) #pyperclip allows the program to put input into the users clipboard (copy and paste)
    copy_button.place(x=100, y=35) #You might notice how there is no "pack", thats because "pack" and "place" are mutually exclusive since they both do the same task.

    #NEW CSV INPUT
    def newCsv():
        textWidget.configure(state='normal')
        nextCSV = fd.askopenfilename(title = "Select file",filetypes = (("CSV Files","*.csv"),))

        nextData = pd.read_csv(nextCSV)
        newCSVData = nextData.to_html(index=False)
        
        textWidget.delete("1.0", tk.END)
        textWidget.insert(tk.INSERT, newCSVData)
        textWidget.configure(state='disabled')

    newButton = ttk.Button(
        app,
        text='Select New CSV File',
        command=newCsv)
    newButton.place(x=250, y=35)

#BUTTONS
openButton = ttk.Button( #Need to make this AFTER the function to have it be listed in 'command'
    app, #where the button will go (plainly on the program)
    text='Open a File',
    command=select_csv) #Selects function to run
openButton.pack(expand=True)


app.mainloop() #Properly opens the app (Program)