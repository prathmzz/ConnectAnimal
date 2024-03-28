from tkinter import *
from PIL import Image, ImageTk

def open_lecture_page():
    print("Opening Lecture Page...")
    # Call the lecture_page function from the main script
    lecture_page()

def open_Volunteer_page():
    print("Opening Volunteer Page...")
    # Call the Volunteer_page function from the main script
    Volunteer_page()

def open_teacher_section():
    print("Opening Teacher Section Page...")
    # Call the teacher_section function from the main script
    teacher_section()

def open_Rescue():
    print("Opening Rescue Page...")
    # Call the Rescue function from the main script
    Rescue()

def create_sidebar(root):
    # Create the sidebar frame
    sidebar = Frame(root, width=200, height=600, bg="#eb4163")
    sidebar.pack(side=LEFT, fill=Y)

    menu_items = [
        ("Volunteer", "home_icon.png", open_Volunteer_page),
        ("Donation", "lecture_icon.png", open_lecture_page),
        ("Adoption", "user_icon.png", open_teacher_section),
        ("Rescue", "teacher_icon.png", open_Rescue),
    ]

    buttons = []

    for item in menu_items:
        image = Image.open("Images/" + item[1])
        photo_image = ImageTk.PhotoImage(image)
        button = Button(sidebar, text=item[0], image=photo_image, compound=LEFT, fg="white", bg="#eb4163", bd=0, padx=20,
                        pady=10, anchor="w")
        button.image = photo_image
        button.pack(anchor="w", fill=X)
        button.config(command=item[2])  # Set the command for each button
        buttons.append(button)

    return sidebar, buttons
