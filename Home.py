from tkinter import *
import tkinter as tk
from sidebar import create_sidebar  # Import the create_sidebar function
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
    root = Tk()

root = Tk()
root.title("Volunteer Page")
root.geometry("800x600+100+100")

# Use the create_sidebar function to create the sidebar
topbar,sidebar, buttons = create_sidebar(root,open_Volunteer_page,open_lecture_page,open_Rescue,open_teacher_section)
welcome_label = Label(root, text="Welcome to Animal Connect", font=("Arial", 20))
welcome_label.pack(pady=20)
root.mainloop()