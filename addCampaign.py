from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
from sidebar import create_sidebar

import subprocess
import tkinter as tk

def open_lecture_page():
    root.destroy()
    subprocess.run(["python", "lecture_page.py"])

def open_Volunteer_page():   
    root.destroy()
    subprocess.run(["python", "Volunteer_page.py"])

def open_teacher_section():   
    root.destroy()
    subprocess.run(["python", "teacher_section.py"])

def open_Rescue():
    root.destroy()

def open_view_campaign():
    root.destroy()
    subprocess.run(["python", "viewCampaign.py"])

root = Tk()
root.title("Animal Connect")
root.geometry("800x600+100+100")

topbar, sidebar, buttons = create_sidebar(root, open_lecture_page, open_Volunteer_page, open_teacher_section, open_Rescue)
frame = Frame(root, bg='white')
frame.place(x=162, y=0)  # Adjusted position to be next to the sidebar
root.title("Volunteer Page")
root.geometry("800x600+100+100")

# Create a frame for the button and label
button_frame = Frame(root, bg="white")
button_frame.pack(side=TOP, fill=X)

# Create the main frame
main_frame = Frame(root, bg="white")
main_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

# Add the label
heading = Label(main_frame, text='CAMPAIGN REGISTER', font=('Microsoft Yahei UI Light', 18, 'bold underline'), bg='white', fg='firebrick1')
heading.grid(row=0, column=0, padx=55, pady=10, columnspan=2)

# Add the entry fields
fields = [
    ('Name of Campaign', 1),
    ('Location', 3),
    ('Contact number', 5),
    ('Description of your Campaign', 7)
]

for text, row in fields:
    label = Label(main_frame, text=text, font=('Microsost Yahei UI Light', 10, 'bold'), bg='white', fg='firebrick1')
    label.grid(row=row, column=0, sticky='w', padx=40, pady=(12, 0))

    entry = Entry(main_frame, width=30, font=('Microsost Yahei UI Light', 10, 'bold'), bg='firebrick1', fg='white')
    entry.grid(row=row + 1, column=0, sticky='w', padx=40)
    
# Add the terms and conditions checkbox
check = IntVar()
termandconditions = Checkbutton(main_frame, text='I agree to the terms & conditions', font=('Microsost Yahei UI Light', 8, 'bold'), fg='firebrick1', bg='white', activebackground='white', activeforeground='firebrick1', cursor='hand2', variable=check)
termandconditions.grid(row=9, column=0, padx=2, pady=13, columnspan=2)

# Add the "Add Campaign" button
addCampaign = Button(main_frame, text='Add Campaign', font=('Open Sans', 16, 'bold'), bd=0, bg='firebrick1', fg='white', activebackground='firebrick1', activeforeground='white', width=17, command=open_view_campaign)
addCampaign.grid(row=10, column=0, pady=10, columnspan=2)

root.mainloop()
