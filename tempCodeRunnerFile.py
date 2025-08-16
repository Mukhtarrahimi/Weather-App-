from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox
from geopy.geocoders import Nominatim
from datetime import datetime
from timezonefinder import TimezoneFinder
import requests
import pytz

# ---------- تنظیمات ----------
API_KEY = ""  # <-- کلید OpenWeatherMap خودت را اینجا بگذار (مثلاً "abcd1234...")
WEATHER_URL = "http://api.openweathermap.org/data/2.5/weather"


# function
def getWeather():
    city = textfield.get().strip()
    if not city:
        messagebox.showwarning("Warning", "Please enter a city name.")
        return

    if not API_KEY:
        messagebox.showerror(
            "Missing API Key",
            "Please set your OpenWeatherMap API key in API_KEY variable.",
        )
        return

    try:
        # Geocoding
        geolocator = Nominatim(user_agent="geoapiExercises", timeout=10)
        location = geolocator.geocode(city)
        if location is None:
            messagebox.showerror("Not Found", f"City '{city}' was not found.")
            return

        # Timezone
        obj = TimezoneFinder()
        result = obj.timezone_at(lat=location.latitude, lng=location.longitude)
        if not result:
            messagebox.showerror(
                "Timezone Error", "Could not determine timezone for this location."
            )
            return

        home = pytz.timezone(result)
        local_time = datetime.now(home)
        current_time = local_time.strftime("%I:%M %p")
        clock.config(text=current_time)
        name.config(text="CURRENT WEATHER OF " + city.upper())

        # Weather API
        params = {"q": city, "appid": API_KEY}
        resp = requests.get(WEATHER_URL, params=params, timeout=15)
        resp.raise_for_status()
        json_data = resp.json()

        # اگر شهر نامعتبر بود (کدهای خطا از API)
        if str(json_data.get("cod")) != "200":
            msg = json_data.get("message", "Unknown error")
            messagebox.showerror("API Error", f"OpenWeather error: {msg}")
            return

        condition = json_data["weather"][0]["main"]
        description = json_data["weather"][0]["description"]
        temp = int(json_data["main"]["temp"] - 273.15)  # Kelvin -> Celsius
        pressure = json_data["main"]["pressure"]
        humidity = json_data["main"]["humidity"]
        wind = json_data["wind"]["speed"]

        # Update UI labels (بدون تغییر در چینش/استایل)
        t.config(text=str(temp) + "°C")
        c.config(text=condition + " | " + description)

        w.config(text=str(wind) + " km/h")
        h.config(text=str(humidity))
        d.config(text=description)
        p.config(text=str(pressure))

    except requests.exceptions.RequestException as e:
        messagebox.showerror("Network Error", f"Network/HTTP error:\n{e}")
    except Exception as e:
        messagebox.showerror("Error", f"An unexpected error occurred:\n{e}")


root = Tk()
root.title("Weather App")
root.resizable(False, False)
root.geometry("900x500+300+200")

# search box
search_img = PhotoImage(file="images/Copy of search.png")
my_image = Label(root, image=search_img)
my_image.place(x=20, y=20)

textfield = tk.Entry(
    root,
    justify="center",
    width=22,
    font=("poppins", 20, "bold"),
    bg="#404040",
    border=0,
    fg="white",
)
textfield.place(x=50, y=40)
textfield.focus()

search_icon = PhotoImage(file="images/Copy of search_icon (1).png")
my_image_icon = Button(
    image=search_icon,
    borderwidth=0,
    cursor="hand2",
    bg="#404040",
    activebackground="#404040",
    command=getWeather,
)
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
name = Label(root, font=("arial", 70, "bold"))
name.place(x=30, y=100)
clock = Label(root, font=("Helvetica", 20))
clock.place(x=30, y=13)

# label
label1 = Label(
    root, text="WIND", font=("Helvetica", 20, "bold"), bg="#1ab5ef", fg="white"
)
label1.place(x=100, y=400)

label2 = Label(
    root, text="HUMIDITY", font=("Helvetica", 20, "bold"), bg="#1ab5ef", fg="white"
)
label2.place(x=240, y=400)

label3 = Label(
    root, text="DESCRIPTION", font=("Helvetica", 20, "bold"), bg="#1ab5ef", fg="white"
)
label3.place(x=420, y=400)

label4 = Label(
    root, text="PRESSURE", font=("Helvetica", 20, "bold"), bg="#1ab5ef", fg="white"
)
label4.place(x=650, y=400)

t = Label(font=("arial", 70, "bold"), fg="#ee666d")
t.place(x=400, y=150)
c = Label(font=("arial", 15, "bold"), fg="#ee666d")
c.place(x=400, y=250)

w = Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
w.place(x=120, y=430)
h = Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
h.place(x=300, y=430)
d = Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
d.place(x=500, y=430)
p = Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
p.place(x=720, y=430)

root.mainloop()
