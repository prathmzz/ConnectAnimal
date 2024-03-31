

from tkinter import *
import tkinter as tk
from sidebar import *  # Import the create_sidebar function
import subprocess
from commmon_components import logo_name


def open_post_campaign_page():
    root.destroy()
    subprocess.run(["python", "addCampaign.py"])
def viewButton():
    root.destroy()
    subprocess.run(["python", "viewCampaign.py"])

root = Tk()
logo_name(root,"Volunteer")
root.geometry("800x600+100+100")

# Use the create_sidebar function to create the sidebar
topbar, sidebar, buttons = create_sidebar(root, open_Volunteer_page, open_donation_page, open_rescue_section, open_adoption)
button_frame = Frame(root, bg="white")
button_frame.pack(side=TOP, fill=X)
add_campaign_button = Button(button_frame, text="Post Campaign", fg="white",font=("Jungle Fever", 12,"bold"), bg="#eb4163", bd=0, padx=20, pady=10,command=open_post_campaign_page)
add_campaign_button.pack(side=TOP, fill=X, padx=20, pady=(50, 0))  
view_campaign_button = Button(button_frame, text="View Campaign", fg="white",font=("Jungle Fever", 12,"bold"), bg="#eb4163", bd=0, padx=20, pady=10,command=viewButton)
view_campaign_button.pack(side=TOP, fill=X, padx=20, pady=(10, 0))

# Load and resize the image
image = Image.open("images/bg-2.png")
image = image.resize((700, 250), Image.LANCZOS)  # Resize the image to fill remaining space
photo = ImageTk.PhotoImage(image)

# Create a label to display the image
image_label = Label(root, image=photo)
image_label.image = photo  # Keep a reference to avoid garbage collection
image_label.pack(fill=BOTH, expand=True,pady=(150,0))
root.mainloop()