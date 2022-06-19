
from tkinter import *
import tkinter.ttk as ttk
from tkinter import messagebox
from tkinter.font import Font  
from pymongo import MongoClient
import ctypes as ct


root = Tk()
root.resizable(width=False,height=False)
root.geometry("430x480")
root.title("Client")
root.eval('tk::PlaceWindow . center')
root.attributes('-topmost', 1)
font = Font(family = "Helvetica", size = 13)
root.option_add("*TCombobox*Listbox*Font", font)
ct.windll.shcore.SetProcessDpiAwareness(1)

branch_select = StringVar()
type_select = StringVar()
branch_select.set("--Select--")
type_select.set("--Select--")
branch_list = ['CSE','CSE-AI','CSE-DS']
type_list = ['Regular','Extra','Exam']

def handle_submit():
    box = [name_box,exit_box,roll_box,purpose_box,branch_box]
    for i in box:
        if(i.get() == ''):
            messagebox.showwarning('Error','A Field is Missing')
            return
    else:
         reply = messagebox.askquestion('Confirm','Proceed with Final Submit...?')
         if( reply == 'yes'):
            handle_finalsubmit()
         else:
            return
        

def handle_clear():
    box = [name_box,exit_box,roll_box]
    for i in box:
        i.delete(0,END)
    purpose_box.set('')
    branch_box.set('')

def handle_finalsubmit():
    record = {
        'Name' : name_box.get(),
        'Roll_No' : roll_box.get(),
        'Branch' : branch_box.get(),
        'Type' : purpose_box.get(),
        'Exit_time' : exit_box.get()
    }
    client = MongoClient("mongodb://127.0.0.1:27017/")
    mydb = client['LMS'] #create db LMS
    table = mydb.info #create collection info
    table.insert_one(record)
    root.quit()

#ttkStyles
style = ttk.Style()
style.configure('TEntry',padding='5 5 0 5', fieldbackground='black')
style.configure(
    'W.TButton',
    padding='5 5 0 5',
    font = ('calibri', 13))
style.configure('TCombobox', padding='5 5 0 5')
    

#Label_init
title = Label(root)
name = Label(root)
roll = Label(root)
branch = Label(root)
purpose = Label(root)
exit_time = Label(root)

#Label_config
title.config(font="Arial 15",text="Lab Management System")
name.config(font="Arial 12",text="Name")
roll.config(font="Arial 12",text="Roll no:")
branch.config(font="Arial 12",text="Branch:")
purpose.config(font="Arial 12",text="Type:")
exit_time.config(font="Arial 12",text="Exit:")

#Label_place
title.place(x=100,y=20)
name.place(x=50,y=90)
roll.place(x=50,y=150)
branch.place(x=50,y=210)
purpose.place(x=50,y=270)
exit_time.place(x=50,y=330)

#Entries
name_box = ttk.Entry(root, width=23, font='Arial 13')
roll_box = ttk.Entry(root, width=4, font='Arial 13')
branch_box = ttk.Combobox(root, values=branch_list,state='readonly',style='W.TCombobox',font="Helvetica 13")
purpose_box = ttk.Combobox(root, values=type_list,state='readonly',style='W.TCombobox',font="Helvetica 13")
exit_box = ttk.Entry(root, width=10, font='Arial 13')

#Entries_place
name_box.place(x=120,y=90)
roll_box.place(x=120,y=150)
branch_box.place(x=120,y=210)
purpose_box.place(x=120,y=270)
exit_box.place(x=120,y=330)

#Buttons
submit_button = ttk.Button(
    root,
    style= 'W.TButton',
    text="Submit",
    command=handle_submit).place(x=50,y=400)

clear_button = ttk.Button(
    root,
    style= 'W.TButton',
    text="Clear",
    command=handle_clear).place(x=260,y=400)

root.mainloop()