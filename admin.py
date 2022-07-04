from dataclasses import field
from tkinter import *
from pandastable import Table
from pymongo import MongoClient
from pandas import DataFrame
from tkinter.font import Font 
from tkinter import messagebox
import tkinter.ttk as ttk
import openpyxl
import ctypes 

root = Tk()
ctypes.windll.shcore.SetProcessDpiAwareness(1)
root.eval('tk::PlaceWindow . center')
root.title("LMS_admin_v1.0")
root.geometry("900x480")
root.config(bg="#FFFFFF")
root.resizable(False,False)
font = Font(family = "Helvetica", size = 13)
root.option_add("*TCombobox*Listbox*Font", font)
f = Frame(root)
f.place(x=20,y=40)

#ttkStyles
style = ttk.Style()
style.configure('TEntry',padding='5 5 0 5', fieldbackground='black')
style.configure('TCombobox', padding='5 5 0 5')
style.configure(
    'W.TButton',
    padding='2 2 0 4',
    font = ('calibri', 12))


def handle_filter():
    field = ftr_box.get()
    value = value_box.get()
    new_cur = collection.find({field : value})
    list_cur = list(new_cur)
    if(list_cur):
        render_table(list_cur)
    else:
        messagebox.showinfo('Mismatch','Combination not Found')

def handle_reset():
    cursor = collection.find()
    list_cursor = list(cursor)
    render_table(list_cursor)

def render_table(cur):
    df = DataFrame(cur)
    df.pop('_id')
    table = Table(f,
        dataframe = df,
        showtoolbar=False, 
        showstatusbar=True,
        width=780,
        editable=False,
        )
    table.show()


#connect to mongodb
client = MongoClient("mongodb://127.0.0.1:27017/")
db = client.LMS
collection = db.info
handle_reset()

#labels and entries

dropdown = ["Branch","Date","Type","Name"]
eq = Label(root)
eq.config(text="=",font="Arial 12")
eq.place(x=230,y=420)

ftr_box = ttk.Combobox(root, values=dropdown,state='readonly',style='W.TCombobox',font="Helvetica 13")
ftr_box.place(x=20,y=420)

value_box = ttk.Entry(root, width=18, font='Arial 12')
value_box.place(x=250,y=420)

#buttons
ftr_btn = ttk.Button(
    root,
    style= 'W.TButton',
    text="Filter",
    command=handle_filter).place(x=430,y=420)

rst_btn = ttk.Button(
    root,
    style= 'W.TButton',
    text="Reset",
    command=handle_reset).place(x=530,y=420)


# df.to_excel (r'C:\Users\Amal\Desktop\export_dataframe.xlsx', index = False, header=True)
root.mainloop()