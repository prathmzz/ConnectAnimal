import tkinter as tk
import sqlite3
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
from sidebar import create_sidebar  # Import the create_sidebar function
def open_lecture_page():
    print("Opening Lecture Page...")

def open_Volunteer_page():
    print("Opening Volunteer Page...")

def open_teacher_section():
    print("Opening Teacher Section Page...")

def open_Rescue():
    print("Opening Rescue Page...")
def add_card(name, address, phone, photo=None):
    # Create a new card frame
    card_frame = tk.Frame(cards_frame, bg="white", bd=2, relief=tk.RIDGE)
    card_frame.pack(padx=5, pady=5, side=tk.LEFT)  # Pack the card frame side by side

    if photo:
        # Display image in the card
        photo_label = tk.Label(card_frame, image=photo, bg="white")
        photo_label.image = photo
        photo_label.pack(anchor=tk.N)

    # Display name, address, and phone number below the image
    tk.Label(card_frame, text="Name: " + name, bg="white").pack(anchor=tk.W)
    tk.Label(card_frame, text="Address: " + address, bg="white").pack(anchor=tk.W)
    tk.Label(card_frame, text="Phone: " + phone, bg="white").pack(anchor=tk.W)

def switch_to_card_page():
    input_frame.pack_forget()
    main_menu_frame.pack_forget()
    cards_frame.pack(fill=tk.BOTH, expand=True)
    display_cards()

def switch_to_main_menu():
    cards_frame.pack_forget()
    main_menu_frame.pack(fill=tk.BOTH, expand=True)
    input_frame.pack(fill=tk.BOTH, expand=True)

def switch_to_image_page():
    main_menu_frame.pack_forget()
    image_page_frame.pack(fill=tk.BOTH, expand=True)
    display_uploaded_image()

def open_volunteer_page():
    print("")

def create_database():
    conn = sqlite3.connect("user_data.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS Users (
                Name TEXT,
                Address TEXT,
                Phone TEXT,
                Photo BLOB
                )''')
    conn.commit()
    conn.close()

def insert_user_data(name, address, phone, photo=None):
    conn = sqlite3.connect("user_data.db")
    c = conn.cursor()
    c.execute("INSERT INTO Users VALUES (?, ?, ?, ?)", (name, address, phone, photo))
    conn.commit()
    conn.close()

def get_user_data():
    conn = sqlite3.connect("user_data.db")
    c = conn.cursor()
    c.execute("SELECT * FROM Users")
    rows = c.fetchall()
    conn.close()
    return rows

def display_cards():
    # Clear existing cards
    for widget in cards_frame.winfo_children():
        widget.destroy()

    # Display cards for all user data from the database
    for row in get_user_data():
        name, address, phone, photo = row
        if photo:
            photo = Image.open(photo)
            photo.thumbnail((120, 120))  # Resize the image to fit within the card
            photo = ImageTk.PhotoImage(photo)
        add_card(name, address, phone, photo)

def display_uploaded_image():
    image_data = get_user_data()[-1][-1]  # Get the last uploaded image
    if image_data:
        photo = Image.open(image_data)
        photo.thumbnail((400, 400))
        photo = ImageTk.PhotoImage(photo)
        uploaded_image_label.configure(image=photo)
        uploaded_image_label.image = photo

def upload_image():
    filename = filedialog.askopenfilename(title="Select Image", filetypes=(("Image files", "*.png;*.jpg;*.jpeg"), ("All files", "*.*")))
    if filename:
        insert_user_data('', '', '', filename)
        switch_to_image_page()

root = Tk()
root.title("Animal Connect")
root.geometry("800x600+100+100")
topbar,sidebar, buttons = create_sidebar(root,open_Volunteer_page,open_lecture_page,open_Rescue,open_teacher_section)

# Create database and table if they don't exist
create_database()

# Create a frame for the buttons in the white portion
main_menu_frame = tk.Frame(root)
main_menu_frame.pack(fill=tk.BOTH, expand=True)
button_frame = Frame(root, bg="white")
button_frame.pack(side=TOP, fill=X)
tk.Label(main_menu_frame, text="Welcome to Animal Connect", font=("Helvetica", 24)).pack(pady=20)
tk.Button(main_menu_frame, text="Go to Card Page", command=switch_to_card_page).pack()

# Create input fields
input_frame = tk.Frame(root)
input_frame.pack(fill=tk.BOTH, expand=True, padx=200, pady=100)

tk.Label(input_frame, text="Name:").grid(row=0, column=0, sticky=tk.W)
name_entry = tk.Entry(input_frame, width=50)
name_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(input_frame, text="Address:").grid(row=1, column=0, sticky=tk.W)
address_entry = tk.Entry(input_frame, width=50)
address_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Label(input_frame, text="Phone:").grid(row=2, column=0, sticky=tk.W)
phone_entry = tk.Entry(input_frame, width=50)
phone_entry.grid(row=2, column=1, padx=5, pady=5)

def post_button_command():
    insert_user_data(name_entry.get(), address_entry.get(), phone_entry.get())
    switch_to_card_page()

post_button = tk.Button(input_frame, text="Post", command=post_button_command)
post_button.grid(row=3, columnspan=2, pady=10)

# Create a button to upload image
upload_image_button = tk.Button(input_frame, text="Upload Image", command=upload_image)
upload_image_button.grid(row=4, columnspan=2, pady=10)

# Frame to hold cards
cards_frame = tk.Frame(root)

# Frame to display uploaded image
image_page_frame = tk.Frame(root)

# Label to display uploaded image
uploaded_image_label = tk.Label(image_page_frame)
uploaded_image_label.pack(pady=20)

Label(button_frame, text="").pack(side=TOP, pady=10)

# Configure button commands
for button in buttons:
    button.config(command=open_volunteer_page)

root.mainloop()
