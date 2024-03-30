from tkinter import *
from PIL import Image, ImageTk, ImageOps
import subprocess
from tkinter import ttk


def open_donation_page(root):
    print("Opening Lecture Page...")
    root.destroy()
    import lecture_page


def open_Volunteer_page(root):
    print("Opening Volunteer Page...")
    root.destroy()
    import Volunteer_page


def open_rescue_section(root):
    print("Opening Teacher Section Page...")
    root.destroy()
    import Rescue


def open_adoption(root):
    print("Opening Rescue Page...")
    root.destroy()
    import teacher_section


def create_sidebar(root, open_Volunteer_page, open_donation_page, open_rescue_section, open_adoption):
    # Create the top bar (navbar)
    topbar = Frame(root, bg="#ed5876", width=600, height=50)
    topbar.pack(side=TOP, fill=X)

    title = Button(topbar, text="Animal Connect", font=("Arial", 15, "bold"), bd=0, bg="#ed5876", fg="#ffffff",
                   activebackground='#eb4163')
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
        ("Volunteer", "volunteer.png", lambda: open_Volunteer_page(root)),
        ("Donation", "donation.png", lambda: open_donation_page(root)),
        ("Rescue", "animal-rescue.png", lambda: open_rescue_section(root)),
        ("Adoption", "adoption.png", lambda: open_adoption(root)),
    ]

    buttons = []

    for item in menu_items:
        # Resize the image to 50x50 using LANCZOS resampling filter
        image = Image.open("Images/" + item[1]).resize((50, 50), Image.LANCZOS)
        photo_image = ImageTk.PhotoImage(image)
        button = Button(sidebar, text=item[0], font=("Arial", 12, "bold"), image=photo_image, compound=LEFT, fg="white",
                        bg="#eb4163", bd=0, padx=20,
                        pady=15, anchor="w")
        button.image = photo_image
        button.pack(anchor="w", fill=X)
        button.config(command=item[2])  # Set the command for each button
        buttons.append(button)

        # Add a horizontal separator after each button
        separator = ttk.Separator(sidebar, orient='horizontal')
        separator.pack(fill='x', padx=10, pady=5)

    return topbar, sidebar, buttons
