from tkinter import *
import tkinter as tk
from sidebar import *  # Import the create_sidebar function
import subprocess
from commmon_components import logo_name

def viewButton():
    root.destroy()
    subprocess.run(["python", "Card.py"])
# def open_donation_page():
#     print("Opening Lecture Page...")
#     subprocess.run(["python", "lecture_page.py"])
#
# def open_Volunteer_page():
#     print("Opening Volunteer Page...")
#     subprocess.run(["python", "Volunteer_page.py"])
#
# def open_rescue_section():
#     print("Opening Teacher Section Page...")
#     subprocess.run(["python", "Rescue.py"])
#
# def open_adoption():
#     print("Opening Rescue Page...")
#     subprocess.run(["python", "teacher_section.py"])

def open_post_adoption_page():
     root.destroy()
     subprocess.run(["python", "PostAdoption.py"])

def  open_viewAdoption():
    root.destroy()
    import viewAdoption

root = Tk()
logo_name(root)
root.geometry("800x600+100+100")

# Use the create_sidebar function to create the sidebar
topbar,sidebar, buttons = create_sidebar(root,open_Volunteer_page, open_donation_page, open_rescue_section, open_adoption)


button_frame = Frame(root, bg="white")
button_frame.pack(side=TOP, fill=X)
add_campaign_button = Button(button_frame, text="Adopt a pet", fg="white", bg="#eb4163", bd=0, padx=20, pady=10,command=open_post_adoption_page)
add_campaign_button.pack(side=TOP, fill=X, padx=20, pady=(50, 0))

view_pet = Button(button_frame, text="View Pets for Adoption", fg="white", bg="#eb4163", bd=0, padx=20, pady=10,command=open_viewAdoption)
view_pet.pack(side=TOP, fill=X, padx=20, pady=(50, 0))
# Adjust pady to add space
# view_campaign_button = Button(button_frame, text="post pet for adoption", fg="white", bg="#eb4163", bd=0, padx=20, pady=10,command=viewButton)
# view_campaign_button.pack(side=TOP, fill=X, padx=20, pady=(10, 0))  # Adjust pady to add space
root.mainloop()
