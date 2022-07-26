from dataclasses import field
from tkinter import *
from tkinter.filedialog import asksaveasfilename
from pandastable import Table
from pymongo import MongoClient
from pandas import DataFrame
from tkinter.font import Font 
from tkinter import messagebox
import tkinter.ttk as ttk
import ctypes 
import os

root = Tk()
ctypes.windll.shcore.SetProcessDpiAwareness(1)
root.eval('tk::PlaceWindow . center')
root.title("LMS_admin_v1.0")
root.geometry("1200x750")
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

def handle_print():
    file = asksaveasfilename(filetypes=[('excel', "*.xlsx")])
    if(file):
        df.to_excel(file+".xlsx",index = False, header=True)

def handle_shutdown_call():
    os.system("./client -r shutdown -t 60 -i eth0")

def handle_notify():
    msg = notify_box.get()
    os.system("./client -r notify -m "+msg+" -b -i eth0")


def render_table(cur):
    global df
    df = DataFrame(cur)
    df.pop('_id')
    table = Table(f,
        dataframe = df,
        showtoolbar=False, 
        showstatusbar=True,
        width=1100,
        height=500,
        editable=False,
        )
    table.show()
    for i in range(2):
        table.zoomIn()
    table.expandColumns(factor=50)

#connect to mongodb
ip = "mongodb://127.0.0.1:27017/"
client = MongoClient(ip)
db = client.LMS
collection = db.info
handle_reset()

#labels and entries

dropdown = ["Branch","Date","Type","Name","Table_No","IP"]
eq = Label(root)
eq.config(text="=",font="Arial 12")
eq.place(x=230,y=640)

ftr_box = ttk.Combobox(root, values=dropdown,state='readonly',style='W.TCombobox',font="Helvetica 13")
ftr_box.place(x=20,y=640)

value_box = ttk.Entry(root, width=18, font='Arial 12')
value_box.place(x=250,y=640)

notify_box = ttk.Entry(root, width=43, font='Arial 12')
notify_box.place(x=20,y=690)
#buttons
ftr_btn = ttk.Button(
    root,
    style= 'W.TButton',
    text="Filter",
    command=handle_filter).place(x=430,y=640)

rst_btn = ttk.Button(
    root,
    style= 'W.TButton',
    text="Reset",
    command=handle_reset).place(x=530,y=640)

print_btn = ttk.Button(
    root,
    style= 'W.TButton',
    text="Print",
    command=handle_print).place(x=530,y=690)

shut_btn = ttk.Button(
    root,
    style= 'W.TButton',
    text="Shutdown",
    command=handle_shutdown_call).place(x=1080,y=640)

notify_btn = ttk.Button(
    root,
    style= 'W.TButton',
    text="Notify",
    command=handle_notify).place(x=430,y=690)

# df.to_excel (r'C:\Users\Amal\Desktop\export_dataframe.xlsx', index = False, header=True)
root.mainloop()
