import tkinter as tk
from tkinter import filedialog, messagebox
import sqlite3
# Define global variables
image_data = None

def select_image():
    global image_data
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
    if file_path:
        with open(file_path, "rb") as file:
            image_data = file.read()
        label_image.config(text=file_path)

def submit_form():
    name = name_entry.get()
    contact_info = contact_entry.get()
    breed = breed_entry.get()
    vaccinated = vaccinated_var.get()
    
    if not all([name, contact_info, breed]):
        messagebox.showerror("Error", "Please fill in all fields.")
        return
    
    if not image_data:
        messagebox.showerror("Error", "Please select an image.")
        return
    
    # Process the data as needed, for example, you can save it to a database
    print("Name:", name)
    print("Contact Info:", contact_info)
    print("Breed:", breed)
    print("Is Vaccinated:", vaccinated)
    print("Image Data Length:", len(image_data))

    conn = sqlite3.connect('Data.db')
    table_create_query = '''CREATE TABLE IF NOT EXISTS User_Data
    (name TEXT ,contact_info INT , breed TEXT , vaccinated BOOL , image_data BLOB)'''
    conn.execute(table_create_query)
    data_insert_query = ''' INSERT INTO User_Data(name,contact_info,breed,vaccinated,image_data) 
    VALUES (?,?,?,?,?)'''
    data_insert_tuple=(name,contact_info,breed,vaccinated,image_data)
    cursor=conn.cursor()
    cursor.execute(data_insert_query,data_insert_tuple)
    conn.commit()
    conn.close()

root = tk.Tk()
root.title("Pet Registration Form")

# Name
tk.Label(root, text="Name of Owner:").grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1, padx=10, pady=5)

# Contact Info
tk.Label(root, text="Contact Info:").grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
contact_entry = tk.Entry(root)
contact_entry.grid(row=1, column=1, padx=10, pady=5)

# Breed
tk.Label(root, text="Breed of Pet:").grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)
breed_entry = tk.Entry(root)
breed_entry.grid(row=2, column=1, padx=10, pady=5)

# Vaccinated
vaccinated_var = tk.BooleanVar()
tk.Checkbutton(root, text="Is your pet Vaccinated?", variable=vaccinated_var).grid(row=3, column=0, columnspan=2, padx=10, pady=5)

# Image Upload
tk.Label(root, text="Upload Image:").grid(row=4, column=0, padx=10, pady=5, sticky=tk.W)
select_button = tk.Button(root, text="Select Image", command=select_image)
select_button.grid(row=4, column=1, padx=10, pady=5)
label_image = tk.Label(root, text="", wraplength=300)
label_image.grid(row=5, column=0, columnspan=2, padx=10, pady=5)

# Submit Button
submit_button = tk.Button(root, text="Submit", command=submit_form)
submit_button.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()
