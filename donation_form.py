from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import subprocess
import tkinter as tk
from tkinter import filedialog, messagebox
import sqlite3
from commmon_components import logo_name
from sidebar import *  # Import the create_sidebar function
from commmon_components import *

# def open_Volunteer_page():
#     print("Opening Volunteer Page...")
#     root.destroy()
#     subprocess.run(["python", "Volunteer_page.py"])
#
# def open_donation_page():
#     print("Opening Donation Page...")
#
# def open_rescue_section():
#     print("Opening Rescue Section...")
#
# def open_adoption():
#     print("Opening Adoption Page...")

def select_image():
    global image_data
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
    if file_path:
        with open(file_path, "rb") as file:
            image_data = file.read()
        upload_label.config(text=file_path)

def submit_form():
    name = name_entry.get()
    contact_info = contact_entry.get()
    disease = disease_entry.get()
    funds = funds_entry.get()
    
    if not all([name, contact_info, disease, funds]):
        messagebox.showerror("Error", "Please fill in all fields.")
        return
    
    if not image_data:
        messagebox.showerror("Error", "Please select an image.")
        return
    
    # Process the data as needed, for example, you can save it to a database
    print("Name:", name)
    print("Contact Info:", contact_info)
    print("Disease:", disease)
    print("Funds required for treatment:", funds)
    print("Image Data Length:", len(image_data))

    conn = sqlite3.connect('Donation.db')
    table_create_query = '''CREATE TABLE IF NOT EXISTS User_Data
    (name TEXT ,contact_info TEXT , disease TEXT , image_data BLOB,funds TEXT)'''
    conn.execute(table_create_query)
    data_insert_query = ''' INSERT INTO User_Data(name,contact_info,disease,image_data,funds) 
    VALUES (?,?,?,?,?)'''
    data_insert_tuple=(name,contact_info,disease,image_data,funds)
    cursor=conn.cursor()
    cursor.execute(data_insert_query,data_insert_tuple)
    conn.commit()
    conn.close()
    messagebox.showinfo('Success','Donation post added successfully')
    open_main_page()

def open_main_page():
    print("Opening viewDonation page...")
    root.destroy()
    subprocess.run(["python", "viewDonation.py"])
root = Tk()
root.geometry("800x600+100+100")
logo_name(root)
topbar, sidebar, buttons = create_sidebar(root, open_Volunteer_page, open_donation_page, open_rescue_section,
                                          open_adoption)
root.title("Donation Page")

frame = Frame(root, bg='white')
frame.place(x=162, y=0)  # Adjusted position to be next to the sidebar

    # Create a frame for the button and label
button_frame = Frame(root, bg="white")
button_frame.pack(side=TOP, fill=X)

    # Create the main frame
main_frame = Frame(root, bg="white")
main_frame.place(relx=0.6, rely=0.45, anchor=CENTER)

    # Add the label
heading = Label(main_frame, text='Post to collect funds', font=('Microsoft Yahei UI Light', 18, 'bold underline'), bg='white', fg='firebrick1')
heading.grid(row=0, column=0, padx=55, pady=10, columnspan=2)

    # Add the entry fields
fields = [
        ('Name', 1),
        ('Contact Info', 5),
        ('Disease', 7),
        ('Funds required for treatment(In INR)', 9)  # Corrected row number
    ]

for text, row in fields:
    label = Label(main_frame, text=text, font=('Microsoft Yahei UI Light', 10, 'bold'), bg='white', fg='firebrick1')
    label.grid(row=row, column=0, sticky='w', padx=40, pady=(12, 0))

global name_entry, contact_entry, disease_entry, upload_label, funds_entry

name_entry = Entry(main_frame, width=30, font=('Microsoft Yahei UI Light', 10, 'bold'), bg='firebrick1', fg='white')
name_entry.grid(row=2, column=0, sticky='w', padx=40)

contact_entry = Entry(main_frame, width=30, font=('Microsoft Yahei UI Light', 10, 'bold'), bg='firebrick1', fg='white')
contact_entry.grid(row=6, column=0, sticky='w', padx=40)

disease_entry = Entry(main_frame, width=30, font=('Microsoft Yahei UI Light', 10, 'bold'), bg='firebrick1', fg='white')
disease_entry.grid(row=8, column=0, sticky='w', padx=40)

funds_entry = Entry(main_frame, width=30, font=('Microsoft Yahei UI Light', 10, 'bold'), bg='firebrick1', fg='white')
funds_entry.grid(row=10, column=0, sticky='w', padx=40)  # Corrected row number

    # Image Upload
upload_frame = Frame(root)
upload_frame.place(relx=0.6, rely=0.8, anchor=CENTER)

upload_label = Label(upload_frame, text="Upload Image:", font=('Microsoft Yahei UI Light', 10, 'bold'), bg='white', fg='firebrick1')
upload_label.pack(side=LEFT)

select_button = Button(upload_frame, text="Select Image", command=select_image, font=('Microsoft Yahei UI Light', 10, 'bold'), bg='firebrick1', fg='white')
select_button.pack(side=LEFT, padx=(0, 10))

    # Submit Button
submit_frame = Frame(root)
submit_frame.place(relx=0.6, rely=0.9, anchor=CENTER)

submit_button = Button(submit_frame, text="Post", command=submit_form, font=('Microsoft Yahei UI Light', 10, 'bold'), bg='firebrick1', fg='white')
submit_button.pack(side=TOP, pady=10)

# create_components()

root.mainloop()
