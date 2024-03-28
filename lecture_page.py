from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
from sidebar import create_sidebar
import subprocess
from commmon_components import logo_name

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

root = Tk()
logo_name(root)
root.geometry("800x600+100+100")

# Call create_sidebar with the required arguments
topbar, sidebar, buttons = create_sidebar(root, open_lecture_page, open_Volunteer_page, open_teacher_section, open_Rescue)

# Add specific content for the lecture page
# label = Label(root, text="Lecture Page Content")
# button_frame = Frame(root, bg="white")
# button_frame.pack(side=TOP, fill=X)
# # Add the two additional buttons in the middle
# add_campaign_button = Button(button_frame, text="Post for donation", fg="white", bg="#eb4163", bd=0, padx=20, pady=10)
# add_campaign_button.pack(side=TOP, fill=X, padx=20, pady=(50, 0))  # Adjust pady to add space
# view_campaign_button = Button(button_frame, text="View Donation", fg="white", bg="#eb4163", bd=0, padx=20, pady=10)
# view_campaign_button.pack(side=TOP, fill=X, padx=20, pady=(10, 0))  # Adjust pady to add space
# # label.pack()
label = tk.Label(root, text="Donation Page")

# Pack the label widget to display it in the window
label.pack()

root.mainloop()




