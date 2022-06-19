from tkinter import *
import ctypes as ct
 
ct.windll.shcore.SetProcessDpiAwareness(1)#TO OPTIMIZE UI
root = Tk()
root.title(" Lab Management System")
root.geometry("750x480")
root.configure(bg = "#363636")
root.resizable(width=False,height=False)
root.iconbitmap("mut.ico") # MUTHOOT LOGO

shut_string = "Send Shutdown call to all devices"
fetch_string = "Fetch the details from a device"

options = [
    "10.90.16.0",
    "10.90.16.1",
    "10.90.16.2",
    "10.90.16.3",
    "10.90.16.4",
    "10.90.16.5",
    "10.90.16.6",
]


# datatype of menu text
clicked = StringVar()
data = StringVar()
  
# initial menu text
clicked.set( "Select" )

dataset = {
    "ip" : str(clicked),
    "Name" : "jdkjkhs"
}
  



#FOR DARK TITLE BAR ONLY SUPPORTED IN Windows 11
def dark_title_bar(window):
    """
    MORE INFO:
    https://docs.microsoft.com/en-us/windows/win32/api/dwmapi/ne-dwmapi-dwmwindowattribute
    """
    window.update()
    DWMWA_USE_IMMERSIVE_DARK_MODE = 20
    set_window_attribute = ct.windll.dwmapi.DwmSetWindowAttribute
    get_parent = ct.windll.user32.GetParent
    hwnd = get_parent(window.winfo_id())
    rendering_policy = DWMWA_USE_IMMERSIVE_DARK_MODE
    value = 2
    value = ct.c_int(value)
    set_window_attribute(hwnd, rendering_policy, ct.byref(value),ct.sizeof(value))

def button_hover0(e):
    status_label.config(text=shut_string)
def button_hover1(e):
    status_label.config(text=fetch_string)
def button_leave(e):
    status_label.config(text="")
def handle_fetch():
        data.set(dataset)

dark_title_bar(root)

#SECTION 1
Label(
    root, 
    text="Select device IP",
    bg="#363636",
    fg="#FFFFFF",
    font='arial 12').place(x=30,y=30) #ipLabel

op = OptionMenu( root , clicked , *options,  )
op.config(font="arial 10 italic",bg='#333333',fg="#FFFFFF",width=30) #ipBox
op.place(x = 30, y = 65,height=38)


#BUTTONS

#shutButton
img0 = PhotoImage(file = f"img0.png") 
b0 = Button(
    image = img0,
    borderwidth = 0,
    bg="#363636",
    cursor="hand2",
    highlightthickness = 0,
    relief = "flat")

b0.place(
    x = 590, y = 60,
    width = 124,
    height = 48)

b0.bind("<Enter>", button_hover0)
b0.bind("<Leave>", button_leave)

#fetchButton
img1 = PhotoImage(file = f"img1.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    bg="#363636",
    cursor="hand2",
    command= handle_fetch,
    highlightthickness = 0,
    relief = "flat")

b1.place(
    x = 444, y = 60,
    width = 124,
    height = 48) 

b1.bind("<Enter>", button_hover1)
b1.bind("<Leave>", button_leave)


#INFO SECTION


Label(
    root, 
    text="Details",
    bg="#363636",
    fg="#FFFFFF",
    font='arial 12').place(x=30,y=120) #info

info_box = Entry(root, state=DISABLED,textvariable=data, width = 85).place(x = 30, y = 160,height=270)
 #infoBox

#STATUS BAR
status_label = Label(root,text="", bg="#363636",fg="#FFFFFF",anchor=W)
status_label.pack(side=BOTTOM, ipady=6, ipadx=6,)




root.mainloop()