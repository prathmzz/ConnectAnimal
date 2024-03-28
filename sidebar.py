from tkinter import *
from PIL import Image, ImageTk
import subprocess
def open_lecture_page():
    print("Opening Lecture Page...")
    subprocess.run(["python", "lecture_page.py"])
def open_Volunteer_page():
    print("Opening Volunteer Page...")
    subprocess.run(["python", "Volunteer_page.py"])
def open_teacher_section():
    print("Opening Teacher Section Page...")
    subprocess.run(["python", "teacher_section.py"])
def open_Rescue():
    print("Opening Rescue Page...")
    subprocess.run(["python", "Rescue.py"])


def create_sidebar(root,open_Volunteer_page,open_lecture_page,open_Rescue,open_teacher_section):
    # Create the top bar (navbar)
    topbar = Frame(root, bg="#ed5876", width=600, height=50)
    topbar.pack(side=TOP, fill=X)

    title = Button(topbar, text="Animal Connect", font=("Arial", 15, "bold"), bd=0, bg="#ed5876", fg="#ffffff", activebackground='#eb4163')
    title.pack(side=LEFT, padx=20, pady=10)

    user_icon_image = Image.open("Images/settings_icon.png").resize((16, 16))
    user_icon_photo = ImageTk.PhotoImage(user_icon_image)
    user_icon = Label(topbar, image=user_icon_photo, bg="#ed5876")
    user_icon.image = user_icon_photo
    user_icon.pack(side=RIGHT, padx=10, pady=10)

    user_name = Label(topbar, text="Animal Connect", font=("Arial", 16), bg="#ed5876", fg="#ffffff")
    user_name.pack(side=RIGHT, pady=10)

    # Create the sidebar frame
    sidebar = Frame(root, width=200, height=600, bg="#eb4163")
    sidebar.pack(side=LEFT, fill=Y)

    menu_items = [
        ("Volunteer", "home_icon.png", open_Volunteer_page),
        ("Donation", "lecture_icon.png", open_lecture_page),
        ("Rescue", "user_icon.png", open_teacher_section),
        ("Adoption", "teacher_icon.png", open_Rescue),
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

    return topbar, sidebar, buttons
