import tkinter as tk
import sqlite3
from tkinter import *
from sidebar import create_sidebar  # Import the create_sidebar function
import subprocess
import tkinter as tk
from commmon_components import logo_name

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

def add_card(name, address, phone):
    # Calculate the number of existing cards to determine the row and column for the new card
    num_cards = len(cards_frame.grid_slaves())
    # Create a new card frame
    card_frame = tk.Frame(cards_frame, bg="white", bd=2, relief=tk.RIDGE)
    card_frame.grid(row=num_cards // 3, column=num_cards % 3, padx=5, pady=5)  # Side by side, 3 cards per row
    # Display name, address, and phone number below the image
    tk.Label(card_frame, text="Name: " + name, bg="white").pack(anchor=tk.W)
    tk.Label(card_frame, text="Address: " + address, bg="white").pack(anchor=tk.W)
    tk.Label(card_frame, text="Phone: " + phone, bg="white").pack(anchor=tk.W)

root = tk.Tk()
logo_name(root)
root.geometry("800x600+100+100")
topbar, sidebar, buttons = create_sidebar(root, open_lecture_page, open_Volunteer_page, open_teacher_section, open_Rescue)

def switch_to_main_menu():
    cards_frame.pack_forget()  # Hide the cards frame if it's currently displayed
    input_frame.pack(fill=tk.BOTH, expand=True)  # Display the input frame
    main_menu_frame.pack(fill=tk.BOTH, expand=True)  # Display the main menu frame 
    
def switch_to_card_page():
    input_frame.pack_forget()
    main_menu_frame.pack_forget()
    cards_frame.pack(fill=tk.BOTH, expand=True)
    display_cards()
    switch_to_main_frame = tk.Frame(cards_frame)
    switch_to_main_frame.pack(pady=10)
    switch_to_main_button = tk.Button(switch_to_main_frame, text="Switch to Main", command=switch_to_main_menu)
    switch_to_main_button.pack()



def create_database():
    conn = sqlite3.connect("user_data.db")
    c = conn.cursor()
    
    # Drop the existing Users table if it exists
    c.execute('''DROP TABLE IF EXISTS Users''')
    
    # Create the Users table with the updated schema
    c.execute('''CREATE TABLE Users (
                Name TEXT,
                Address TEXT,
                Phone TEXT
                )''')
    
    conn.commit()
    conn.close()

def insert_user_data(name, address, phone):
    conn = sqlite3.connect("user_data.db")
    c = conn.cursor()
    c.execute("INSERT INTO Users VALUES (?, ?, ?)", (name, address, phone))
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
        if all(row):  # Check if all values in the row are not empty or None
            name, address, phone = row
            add_card(name, address, phone)
        else:
            print("Invalid data format in database row:", row)




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
    # Get the values entered in the input fields
    name = name_entry.get()
    address = address_entry.get()
    phone = str(phone_entry.get())  # Ensure phone is a string

    # Insert the user data into the database
    insert_user_data(name, address, phone)

    # Create a new card with the entered details
    add_card(name, address, phone)

    # Switch to the card page to display the newly added card
    switch_to_card_page()


post_button = tk.Button(input_frame, text="Post", command=post_button_command)
post_button.grid(row=3, columnspan=2, pady=10)


# Frame to hold cards
cards_frame = tk.Frame(root)



root.mainloop()