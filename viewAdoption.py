from tkinter import *
import tkinter as tk
from tkinter import ttk  # Import ttk for themed scrollbar
from sidebar import *
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
            topbar, sidebar, buttons = create_sidebar(self.root, open_Volunteer_page, open_donation_page, open_rescue_section, open_adoption)

            # Create a canvas for pet cards
            self.canvas = tk.Canvas(self.root)
            self.canvas.pack(side=LEFT, fill=BOTH, expand=True)

            # Create a frame inside the canvas to contain the pet cards
            pet_frame = tk.Frame(self.canvas)
            self.canvas.create_window((0, 0), window=pet_frame, anchor=NW)

            pet_frame.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))

            # Add scrollbar
            scrollbar = ttk.Scrollbar(self.root, orient=VERTICAL, command=self.canvas.yview)
            scrollbar.pack(side=RIGHT, fill=Y)

            # Configure canvas to use scrollbar
            self.canvas.configure(yscrollcommand=scrollbar.set)

            # Counter to keep track of entries in the current row
            entry_count = 0

            for row in self.data:
                name, contact_info, breed, vaccinated, image_data = row

                # Create a frame for each data entry
                info_frame = tk.Frame(pet_frame, padx=10, pady=10, bd=2, relief=tk.RIDGE, width=200, height=200)
                info_frame.grid(row=entry_count // 3, column=entry_count % 3, padx=5, pady=5)

                # Display name
                name_label = tk.Label(info_frame, text="Owner Name: " + name)
                name_label.pack()

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

            # Bind mouse wheel event for scrolling
            self.canvas.bind_all("<MouseWheel>", self._on_mousewheel)

        else:
            print("No data found in the database.")

    def _on_mousewheel(self, event):
        self.canvas.yview_scroll(int(-1*(event.delta/120)), "units")

# Create root window
root = Tk()

# Create the application instance
app = AdoptionApp(root)

# Start the Tkinter event loop
root.mainloop()
