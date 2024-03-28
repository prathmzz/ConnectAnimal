import tkinter as tk
import sqlite3
from tkinter import *
from PIL import Image, ImageTk
from tkinter import filedialog, messagebox
import PIL
import subprocess
from io import BytesIO
from commmon_components import logo_name
from sidebar import create_sidebar

# Define global variables
image_data = None

# Function to open other pages
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

# Function to select image from file dialog
def select_image():
    global image_data
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
    if file_path:
        with open(file_path, "rb") as file:
            image_data = file.read()

# Function to insert image data into database
def insert_image_to_database(image_data):
    conn = sqlite3.connect("image_data.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS Images (id INTEGER PRIMARY KEY, image BLOB)")
    cursor.execute("INSERT INTO Images (image) VALUES (?)", (image_data,))
    conn.commit()
    conn.close()    

# Function to display image from database
def display_image_from_database(image_data):
    try:
        image = Image.open(BytesIO(image_data))
        # Resize the image to fit inside the card frame
        max_width = 200  # Adjust this value as needed
        max_height = 200  # Adjust this value as needed
        image.thumbnail((max_width, max_height))
        photo = ImageTk.PhotoImage(image)
        label.config(image=photo)
        label.image = photo 
    except PIL.UnidentifiedImageError as e:
        messagebox.showerror("Error", "Failed to display image: {}".format(str(e)))

# Function to switch to main menu
def switch_to_main_menu():
    cards_frame.pack_forget()  # Hide the cards frame if it's currently displayed
    input_frame.pack(fill=tk.BOTH, expand=True)  # Display the input frame
    main_menu_frame.pack(fill=tk.BOTH, expand=True)  # Display the main menu frame 

# Function to switch to card page
def switch_to_card_page():
    input_frame.pack_forget()
    main_menu_frame.pack_forget()
    cards_frame.pack(fill=tk.BOTH, expand=True)
    display_cards()
    switch_to_main_frame = tk.Frame(cards_frame)
    switch_to_main_frame.pack(pady=10)
    switch_to_main_button = tk.Button(switch_to_main_frame, text="Switch to Main", command=switch_to_main_menu)
    switch_to_main_button.pack()

# Function to display cards
def display_cards():
    for widget in cards_frame.winfo_children():
        widget.destroy()
    for row in get_user_data():
        if all(row):
            name, address, phone, image_data = row
            add_card(name, address, phone, image_data)
        else:
            print("Invalid data format in database row:", row)

# Function to add a card
def add_card(name, address, phone, image_data):
    num_cards = len(cards_frame.grid_slaves())
    card_frame = tk.Frame(cards_frame, bg="white", bd=2, relief=tk.RIDGE)
    card_frame.grid(row=num_cards // 3, column=num_cards % 3, padx=5, pady=5)
    display_image_from_database(image_data)
    tk.Label(card_frame, text="Name: " + name, bg="white").pack(anchor=tk.W)
    tk.Label(card_frame, text="Address: " + address, bg="white").pack(anchor=tk.W)
    tk.Label(card_frame, text="Phone: " + phone, bg="white").pack(anchor=tk.W)

# Function to create database
# Function to create database tables
# Function to create database tables
# Function to create database tables
def create_database():
    conn = sqlite3.connect("user_data.db")
    c = conn.cursor()
    
    # Create Users table with id column
    c.execute('''CREATE TABLE IF NOT EXISTS Users (
                id INTEGER PRIMARY KEY,
                Name TEXT,
                Address TEXT,
                Phone TEXT
                )''')
    
    # Create Images table with user_id column
    c.execute('''CREATE TABLE IF NOT EXISTS Images (
                id INTEGER PRIMARY KEY,
                user_id INTEGER,
                image BLOB,
                FOREIGN KEY (user_id) REFERENCES Users(id)
                )''')
    
    conn.commit()
    conn.close()



# Function to insert user data into database
# Function to insert user data into database
def insert_user_data(name, address, phone):
    conn = sqlite3.connect("user_data.db")
    c = conn.cursor()
    c.execute("INSERT INTO Users (Name, Address, Phone) VALUES (?, ?, ?)", (name, address, phone))
    conn.commit()
    conn.close()


# Function to retrieve user data from database
def get_user_data():
    conn = sqlite3.connect("user_data.db")
    c = conn.cursor()
    c.execute("SELECT Name, Address, Phone, image FROM Users INNER JOIN Images ON Users.id = Images.id")
    rows = c.fetchall()
    conn.close()
    return rows


# Create database
create_database()

# Function to handle post button command
def post_button_command():
    name = name_entry.get()
    address = address_entry.get()
    phone = str(phone_entry.get())
    insert_user_data(name, address, phone)
    if image_data:
        insert_image_to_database(image_data)
        add_card(name, address, phone, image_data) 
        switch_to_card_page()
    else:
        messagebox.showerror("Error", "Please select an image.")

# Create root window
root = tk.Tk()
logo_name(root)
root.geometry("800x600+100+100")
topbar, sidebar, buttons = create_sidebar(root, open_lecture_page, open_Volunteer_page, open_teacher_section, open_Rescue)

# Create main menu frame
main_menu_frame = tk.Frame(root)
main_menu_frame.pack(fill=tk.BOTH, expand=True)
button_frame = Frame(root, bg="white")
button_frame.pack(side=TOP, fill=X)
tk.Label(main_menu_frame, text="Welcome to Animal Connect", font=("Helvetica", 24)).pack(pady=20)
tk.Button(main_menu_frame, text="Go to Card Page", command=switch_to_card_page).pack()

# Create input frame
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

# Create post button
post_button = tk.Button(input_frame, text="Post", command=post_button_command)
post_button.grid(row=3, columnspan=2, pady=10)

# Create a button to select an image
select_button = tk.Button(root, text="Select Image", command=select_image)
select_button.pack(pady=10)

# Create a label to display the selected image
label = tk.Label(root)
label.pack()

# Frame to hold cards
cards_frame = tk.Frame(root)

# Start the main event loop
root.mainloop()
