
from tkinter import *
import tkinter.ttk as ttk
from tkinter import messagebox
from tkinter.font import Font  
from pymongo import MongoClient



root = Tk()
root.resizable(width=False,height=False)
root.geometry("500x480")
root.title("LMS_Client_v1.0")
root.config(bg='#FFFFFF')
root.eval('tk::PlaceWindow . center')
root.attributes('-topmost', 1)
font = Font(family = "Helvetica", size = 13)
root.option_add("*TCombobox*Listbox*Font", font)
root.style = ttk.Style()
root.style.theme_use("clam")
#ct.windll.shcore.SetProcessDpiAwareness(1)

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
style.configure('TEntry',padding='5 5 0 5')
style.configure(
    'W.TButton',
    padding='5 5 0 5',
    font = ('calibri', 10))
style.configure('TCombobox', padding='4 4 0 4', background="#FFFFFF")
    

#Label_init

name = Label(root)
roll = Label(root)
branch = Label(root)
purpose = Label(root)
exit_time = Label(root)

#Label_config

name.config(font="Courier-New 12",text="Name",bg='#FFFFFF')
roll.config(font="Courier-New 12",text="Roll no:",bg='#FFFFFF')
branch.config(font="Courier-New 12",text="Branch:",bg='#FFFFFF')
purpose.config(font="Courier-New 12",text="Type:",bg='#FFFFFF')
exit_time.config(font="Courier-New 12",text="Exit:",bg='#FFFFFF')

#Label_place

name.place(x=50,y=60)
roll.place(x=50,y=120)
branch.place(x=50,y=180)
purpose.place(x=50,y=240)
exit_time.place(x=50,y=300)

#Entries
name_box = ttk.Entry(root, width=23, font='Courier-New 13')
roll_box = ttk.Entry(root, width=4, font='Courier-New 13')
branch_box = ttk.Combobox(root, values=branch_list,state='readonly',style='W.TCombobox',font="Mono 12")
purpose_box = ttk.Combobox(root, values=type_list,state='readonly',style='W.TCombobox',font="Mono 12")
exit_box = ttk.Entry(root, width=10, font='Courier-New 13')

#Entries_place
name_box.place(x=140,y=55)
roll_box.place(x=140,y=115)
branch_box.place(x=140,y=175)
purpose_box.place(x=140,y=235)
exit_box.place(x=140,y=295)

#Buttons
submit_button = ttk.Button(
    root,
    style= 'W.TButton',
    text="Submit",
    command=handle_submit).place(x=50,y=390)

clear_button = ttk.Button(
    root,
    style= 'W.TButton',
    text="Clear",
    command=handle_clear).place(x=330,y=390)

root.mainloop()
