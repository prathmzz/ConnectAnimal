import tkinter as tk
from PIL import Image, ImageTk
import sqlite3
from io import BytesIO

def retrieve_data_from_db():
    conn = sqlite3.connect('Data.db')
    cursor = conn.cursor()
    cursor.execute("SELECT name, contact_info, breed, vaccinated, image_data FROM User_Data")
    data = cursor.fetchall()  # Fetch all data entries
    conn.close()
    return data

def display_data_with_image(data):
    if data:
        root = tk.Tk()
        root.title("Pet Information")

        # Counter to keep track of entries in the current row
        entry_count = 0
        # Frame to contain the current row of data entries
        current_row_frame = None

        for row in data:
            name, contact_info, breed, vaccinated, image_data = row

            # Create a frame for each data entry
            info_frame = tk.Frame(root, padx=10, pady=10, bd=2, relief=tk.RIDGE)
            info_frame.grid(row=entry_count // 4, column=entry_count % 4)

            # Display name
            name_label = tk.Label(info_frame, text="Name: " + name)
            name_label.pack()

            # Display contact info
            contact_label = tk.Label(info_frame, text="Contact Info: " + contact_info)
            contact_label.pack()

            # Display breed
            breed_label = tk.Label(info_frame, text="Breed: " + breed)
            breed_label.pack()

            # Display vaccinated
            vaccinated_label = tk.Label(info_frame, text="Vaccinated: " + ("Yes" if vaccinated else "No"))
            vaccinated_label.pack()

            # Display image
            image = Image.open(BytesIO(image_data))
            # Resize the image to fit inside the frame
            max_width = 200
            max_height = 200
            image.thumbnail((max_width, max_height))
            photo = ImageTk.PhotoImage(image)
            image_label = tk.Label(info_frame, image=photo)
            image_label.image = photo
            image_label.pack()

            # Increment entry count
            entry_count += 1

        root.mainloop()
    else:
        print("No data found in the database.")

# Retrieve all data from the database
data = retrieve_data_from_db()

# Display data along with the image
display_data_with_image(data)
