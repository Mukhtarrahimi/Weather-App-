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
root.mainloop()