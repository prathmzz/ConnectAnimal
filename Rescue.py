from tkinter import *
import webview
from sidebar import create_sidebar  # Import the create_sidebar function
import geocoder
import subprocess
from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
from sidebar import create_sidebar
import subprocess
def open_lecture_page():
    print("Opening Lecture Page...") 
    root.destroy()

    subprocess.run(["python", "lecture_page.py"])
def open_Volunteer_page():
    print("Opening Volunteer Page...")
    root.destroy()

    subprocess.run(["python", "Volunteer_page.py"])
def open_teacher_section():
    print("Opening Teacher Section Page...")
    root.destroy()

    subprocess.run(["python", "teacher_section.py"])
def open_Rescue():
    print("Opening Rescue Page...")
    root.destroy()

    subprocess.run(["python", "Rescue.py"])
def open_lecture_page():
    print("Opening Lecture Page...") 
    root.destroy()

    subprocess.run(["python", "lecture_page.py"])
def open_Volunteer_page():
    print("Opening Volunteer Page...")
    root.destroy()

    subprocess.run(["python", "Volunteer_page.py"])
def open_teacher_section():
    print("Opening Teacher Section Page...")
    root.destroy()

    subprocess.run(["python", "teacher_section.py"])
def open_Rescue():
    print("Opening Rescue Page...")
    root.destroy()

    subprocess.run(["python", "Rescue.py"])

def open_google_maps():
    # Get user's location
    location = geocoder.ip('me')
    lat, lng = location.latlng

    # Construct the Google Maps URL with updated coordinates
    maps_url = f"https://www.google.com/maps/search/Veterinary+Centers/@{lat},{lng},15z"

    # Open the Google Maps URL in webview
    webview.create_window('Google Maps API', maps_url)
    webview.start()


def fetch_user_location():
    location = geocoder.ip('me')
    user_city = location.city
    location_label.config(text=f"Your location: {user_city}")


root = Tk()
root.title("Animal Connect")
root.geometry("800x600+100+100")

# Use the create_sidebar function to create the sidebar

topbar, sidebar, buttons = create_sidebar(root, open_lecture_page, open_Volunteer_page, open_teacher_section, open_Rescue)
# Create a frame for the buttons in the white portion
button_frame = Frame(root, bg="white")
button_frame.pack(side=TOP, fill=X)

# Add a button to fetch user location
Button(button_frame, text="Find Centers", command=fetch_user_location).pack(side=TOP, pady=(
0, 5))  # Adjusted packing options to remove space

# Label to display user's location
location_label = Label(button_frame, text="")
location_label.pack(side=TOP, pady=5)

# Add a space between the buttons
Label(button_frame, text="").pack(side=TOP, pady=10)

# Add the "Open Google Maps" button below
Button(button_frame, text="Open Google Maps", command=open_google_maps).pack(side=TOP, pady=(
0, 5))  # Adjusted packing options to remove space

# Configure button commands
# for button in buttons:
#     button.config(command=open_google_maps)

root.mainloop()