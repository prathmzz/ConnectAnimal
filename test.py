import tkinter as tk
from tkinter import filedialog
import sqlite3
from PIL import Image, ImageTk
from io import BytesIO

# Function to open a file dialog and select an image
def select_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
    if file_path:
        with open(file_path, "rb") as file:
            image_data = file.read()
        insert_image_to_database(image_data)
        display_image_from_database(image_data)

# Function to insert image data into SQLite database
def insert_image_to_database(image_data):
    conn = sqlite3.connect("image_data.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS Images (id INTEGER PRIMARY KEY, image BLOB)")
    cursor.execute("INSERT INTO Images (image) VALUES (?)", (image_data,))
    conn.commit()
    conn.close()

# Function to display an image from SQLite database
def display_image_from_database(image_data):
    image = Image.open(BytesIO(image_data))
    photo = ImageTk.PhotoImage(image)
    label.config(image=photo)
    label.image = photo

# Create Tkinter window
root = tk.Tk()
root.title("Image Viewer")

# Create a button to select an image
select_button = tk.Button(root, text="Select Image", command=select_image)
select_button.pack(pady=10)

# Create a label to display the selected image
label = tk.Label(root)
label.pack()

root.mainloop()
