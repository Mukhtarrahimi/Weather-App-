from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox
from geopy.geocoders import Nominatim
from datetime import datetime
from timezonefinder import TimezoneFinder
import requests
import pytz


# function
def getWeather():
    city= textfield.get()
    
    geolocator = Nominatim(user_agent="geoapiExercises")
    location = geolocator.geocode(city)
    obj = TimezoneFinder()
    result = obj.timezone_at(lat=location.logitude, lng=location.longitude)
    print(result)
    home = pytz.timezone(result)
    local_time = datetime.now(home)
    current_time = local_time.strftime("%I:%M %p")

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
my_image_icon = Button(image=search_icon, borderwidth=0, cursor="hand2", bg="#404040", activebackground="#404040", command=getWeather)
my_image_icon.place(x=400, y=34)

# logo
logo_image = PhotoImage(file="images/Copy of logo.png")
my_image_logo = Label(image=logo_image)
my_image_logo.place(x=150, y=100)

# bottom box
frame_image = PhotoImage(file="images/Copy of box (1).png")
my_image_frame = Label(image=frame_image)
my_image_frame.pack(padx=5, pady=5, side=BOTTOM)

# time
name=Label(root, font=('arial', 70, 'bold'))
name.place(x=30, y=100)
clock = Label(root, font=('Helvetica', 20))
clock.place(x=30, y=13)

# label
label1 = Label(root, text="WIND", font=('Helvetica', 20, 'bold'), bg="#1ab5ef", fg="white")
label1.place(x=100, y=400)

label2 = Label(root, text="HUMIDITY", font=('Helvetica', 20, 'bold'), bg="#1ab5ef", fg="white")
label2.place(x=240, y=400)

label3 = Label(root, text="DESCRIPTION", font=('Helvetica', 20, 'bold'), bg="#1ab5ef", fg="white")
label3.place(x=420, y=400)

label4 = Label(root, text="PRESSURE", font=('Helvetica', 20, 'bold'), bg="#1ab5ef", fg="white")
label4.place(x=650, y=400)

t = Label(font=('arial', 70, 'bold'), fg='#ee666d')
t.place(x=400, y=150)
c = Label(font=('arial', 15, 'bold'), fg='#ee666d')
c.place(x=400, y=250)

w= Label(text='...', font=('arial', 20, 'bold'), bg="#1ab5ef")
w.place(x=120, y=430)
h= Label(text='...', font=('arial', 20, 'bold'), bg="#1ab5ef")
h.place(x=300, y=430)
d= Label(text='...', font=('arial', 20, 'bold'), bg="#1ab5ef")
d.place(x=500, y=430)
p= Label(text='...', font=('arial', 20, 'bold'), bg="#1ab5ef")
p.place(x=720, y=430)


root.mainloop()