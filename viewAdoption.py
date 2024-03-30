from tkinter import *
import tkinter as tk
from sidebar import create_sidebar
import subprocess
from commmon_components import logo_name
from PIL import Image, ImageTk
import sqlite3
from io import BytesIO

class AdoptionApp:
    def __init__(self, root):
        self.root = root
        logo_name(self.root)
        self.root.geometry("800x600+100+100")

        # Retrieve data from the database
        self.data = self.retrieve_data_from_db()

        # Display data along with the image
        self.display_data_with_image()

    def open_lecture_page(self):
        print("Opening Lecture Page...")
        self.root.destroy()
        subprocess.run(["python", "lecture_page.py"])

    def open_Volunteer_page(self):
        print("Opening Volunteer Page...")
        self.root.destroy()
        subprocess.run(["python", "Volunteer_page.py"])

    def open_teacher_section(self):
        print("Opening Teacher Section Page...")
        self.root.destroy()
        subprocess.run(["python", "teacher_section.py"])

    def open_Rescue(self):
        print("Opening Rescue Page...")
        self.root.destroy()
        subprocess.run(["python", "Rescue.py"])

    def retrieve_data_from_db(self):
        conn = sqlite3.connect('Data.db')
        cursor = conn.cursor()
        cursor.execute("SELECT name, contact_info, breed, vaccinated, image_data FROM User_Data")
        data = cursor.fetchall()  # Fetch all data entries
        conn.close()
        return data

    def display_data_with_image(self):
        if self.data:
            # Use the create_sidebar function to create the sidebar
            topbar, sidebar, buttons = create_sidebar(self.root, self.open_Volunteer_page, self.open_lecture_page, 
                                                      self.open_Rescue, self.open_teacher_section)

            # Create a frame to contain all the data frames
            data_frame = tk.Frame(self.root)
            data_frame.pack()

            # Counter to keep track of entries in the current row
            entry_count = 0

            for row in self.data:
                name, contact_info, breed, vaccinated, image_data = row

                # Create a frame for each data entry
                info_frame = tk.Frame(data_frame, padx=10, pady=10, bd=2, relief=tk.RIDGE)
                info_frame.grid(row=entry_count // 3, column=entry_count % 3)

                # Display name
                name_label = tk.Label(info_frame, text="Owner Name: " + name)
                name_label.pack()

                # Display contact info
                # Display contact info
                contact_label = tk.Label(info_frame, text="Contact Info: " + str(contact_info))
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
                max_width = 150
                max_height = 150
                image.thumbnail((max_width, max_height))
                photo = ImageTk.PhotoImage(image)
                image_label = tk.Label(info_frame, image=photo)
                image_label.image = photo
                image_label.pack()

                # Increment entry count
                entry_count += 1

        else:
            print("No data found in the database.")

# Create root window
root = Tk()

# Create the application instance
app = AdoptionApp(root)

# Start the Tkinter event loop
root.mainloop()
