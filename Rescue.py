from tkinter import *
from tkinter import messagebox  # Import messagebox for popup
import webview
import geocoder
from PIL import Image, ImageTk
<<<<<<< Updated upstream
from sidebar import create_sidebar
=======
from sidebar import *
>>>>>>> Stashed changes
from commmon_components import logo_name

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
<<<<<<< Updated upstream
    # Get user's station
    location = geocoder.ip('me')
    station = location.raw.get('station', 'Unknown')  # Get the station information or set to 'Unknown' if not available
    
    # Update location label
    location_label.config(text=f"Your location: {station}")
=======
    # Popup asking for user's location
    result = messagebox.askyesno("Location", "Allow this app to access your location?")
    if result:
        location = geocoder.ip('me')
        user_city = location.city
        location_label.config(text=f"Your location: {user_city}")
    else:
        location_label.config(text="Your location: Unknown")
>>>>>>> Stashed changes

root = Tk()
logo_name(root, "Rescue")
root.geometry("800x600+100+100")

# Use the create_sidebar function to create the sidebar
topbar, sidebar, buttons = create_sidebar(root, open_google_maps, fetch_user_location, fetch_user_location, fetch_user_location)

# Create a frame for the buttons in the white portion
button_frame = Frame(root, bg="white")
button_frame.pack(side=TOP, fill=X)

location_label = Label(button_frame, text="")
location_label.pack(side=TOP, pady=5)

add_campaign_button = Button(button_frame, text="Find Centers", fg="white", bg="#eb4163", bd=0,font=("Jungle Fever", 12,"bold"), padx=20, pady=10,command=fetch_user_location)
add_campaign_button.pack(side=TOP, fill=X, padx=20, pady=(50, 0))

view_pet = Button(button_frame, text="Open Google Maps", fg="white", bg="#eb4163", bd=0, padx=20,font=("Jungle Fever", 12,"bold"), pady=10,command=open_google_maps)
view_pet.pack(side=TOP, fill=X, padx=20, pady=(50, 0))

# Load and resize the image
image = Image.open("images/bg-2.png")
image = image.resize((700, 250), Image.LANCZOS)  # Resize the image to fill remaining space
photo = ImageTk.PhotoImage(image)

# Create a label to display the image
image_label = Label(root, image=photo)
image_label.image = photo  # Keep a reference to avoid garbage collection
image_label.pack(fill=BOTH, expand=True, pady=(80, 0))

root.mainloop()
