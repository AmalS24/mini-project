from tkinter import *


def btn_clicked():
    print("Button Clicked")


window = Tk()

window.geometry("778x515")
window.configure(bg = "#363636")
canvas = Canvas(
    window,
    bg = "#363636",
    height = 515,
    width = 778,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

entry0_img = PhotoImage(file = f"img_textBox0.png")
entry0_bg = canvas.create_image(
    390.5, 319.5,
    image = entry0_img)

entry0 = Entry(
    bd = 0,
    bg = "#ffffff",
    highlightthickness = 0)

entry0.place(
    x = 62.0, y = 175,
    width = 657.0,
    height = 287)

entry1_img = PhotoImage(file = f"img_textBox1.png")
entry1_bg = canvas.create_image(
    230.0, 102.0,
    image = entry1_img)

entry1 = Entry(
    bd = 0,
    bg = "#ffffff",
    highlightthickness = 0)

entry1.place(
    x = 61.0, y = 78,
    width = 338.0,
    height = 46)

img0 = PhotoImage(file = f"img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b0.place(
    x = 600, y = 78,
    width = 124,
    height = 48)

img1 = PhotoImage(file = f"img1.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b1.place(
    x = 444, y = 77,
    width = 124,
    height = 48)

canvas.create_text(
    223.5, 62.5,
    text = "Enter device IP",
    fill = "#ffffff",
    font = ("Inter-Medium", int(18.0)))

canvas.create_text(
    129.5, 157.0,
    text = "Info",
    fill = "#ffffff",
    font = ("Inter-SemiBold", int(18.0)))

window.resizable(False, False)
window.mainloop()
