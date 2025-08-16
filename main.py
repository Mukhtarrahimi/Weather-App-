from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox
from geopy.geocoders import Nominatim
from datetime import datetime
from timezonefinder import TimezoneFinder
import requests
import pytz


root = Tk()
root.title("Weather App")
root.resizable(False, False)
root.geometry("900x500+300+200")

# search box
search_img = PhotoImage(file="images/Copy of search.png")
my_image = Label(root, image=search_img)
my_image.place(x=20, y=20)

textfield = tk.Entry(root, justify='center', width=22, font=('poppins', 20, 'bold'), bg="#404040", border=0, fg="white")
textfield.place(x=50, y=40)
textfield.focus()

search_icon = PhotoImage(file="images/Copy of search_icon (1).png")
my_image_icon = Button(image=search_icon, borderwidth=0, cursor="hand2", bg="#404040", activebackground="#404040")
my_image_icon.place(x=400, y=34)

# logo
logo_image = PhotoImage(file="images/Copy of logo.png")
my_image_logo = Label(image=logo_image)
my_image_logo.place(x=150, y=100)

# bottom box
frame_image = PhotoImage(file="images/Copy of box (1).png")
my_image_frame = Label(image=frame_image)
my_image_frame.pack(padx=5, pady=5, side=BOTTOM)

# label
label1 = Label(root, text="WIND", font=('Helvetica', 20, 'bold'), bg="#1ab5ef", fg="white")
label1.place(x=100, y=400)

label2 = Label(root, text="HUMIDITY", font=('Helvetica', 20, 'bold'), bg="#1ab5ef", fg="white")
label2.place(x=240, y=400)

label3 = Label(root, text="DESCRIPTION", font=('Helvetica', 20, 'bold'), bg="#1ab5ef", fg="white")
label3.place(x=420, y=400)

label4 = Label(root, text="PRESSURE", font=('Helvetica', 20, 'bold'), bg="#1ab5ef", fg="white")
label4.place(x=650, y=400)

root.mainloop()