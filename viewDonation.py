from tkinter import *
import tkinter as tk
from tkinter import ttk
from sidebar import *
import subprocess
from commmon_components import logo_name
from PIL import Image, ImageTk
import sqlite3
from io import BytesIO
import webbrowser


class AdoptionApp:
    def __init__(self, root):
        self.root = root
        logo_name(self.root)
        self.root.geometry("800x600+100+100")

        # Retrieve data from the database
        self.data = self.retrieve_data_from_db()

        # Display data along with the image
        self.display_data_with_image()

        # Bind mouse wheel event for scrolling
        self.root.bind("<MouseWheel>", self._on_mousewheel)

    def retrieve_data_from_db(self):
        conn = sqlite3.connect('Donation.db')
        cursor = conn.cursor()
        cursor.execute("SELECT name, contact_info, disease, image_data,funds FROM User_Data")
        data = cursor.fetchall()
        conn.close()
        return data

    def whatsapp_clicked(self, contact_number):
        print("redirecting to whatsapp chat")
        if contact_number[:3] != "+91":
            contact_number = "+91" + contact_number
        whatsapp_url = f"https://wa.me/{contact_number}"
        webbrowser.open(whatsapp_url)

    def display_data_with_image(self):
        if self.data:
            topbar, sidebar, buttons = create_sidebar(self.root, open_Volunteer_page, open_donation_page, open_rescue_section, open_adoption)

            self.canvas = tk.Canvas(self.root)
            self.canvas.pack(side=LEFT, fill=BOTH, expand=True)

            pet_frame = tk.Frame(self.canvas)
            self.canvas.create_window((0, 0), window=pet_frame, anchor=NW)

            pet_frame.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))

            scrollbar = ttk.Scrollbar(self.root, orient=VERTICAL, command=self.canvas.yview)
            scrollbar.pack(side=RIGHT, fill=Y)

            self.canvas.configure(yscrollcommand=scrollbar.set)

            for row in self.data:
                name, contact_info, disease, image_data,funds = row

                info_frame = tk.Frame(pet_frame, bd=2, relief=tk.RIDGE)
                info_frame.pack(fill=tk.BOTH, expand=True, pady=5)

                details_frame = tk.Frame(info_frame, relief=tk.RIDGE)
                details_frame.pack(side=LEFT, padx=30, pady=20)

                name_label = tk.Label(details_frame, text="Owner Name: " + name)
                name_label.pack()

                disease_label = tk.Label(details_frame, text="disease: " + disease)
                disease_label.pack()

                contact_label = tk.Label(details_frame, text="Contact Info: " + str(contact_info))
                contact_label.pack()

                funds_label = tk.Label(details_frame, text="Funds Required: " + str(funds))
                funds_label.pack()


                # Create WhatsApp button with current contact_info
                whatsapp_image = Image.open("images/whatsapp (1).png")
                whatsapp_photo = ImageTk.PhotoImage(whatsapp_image)
                whatsappButton = Button(details_frame, image=whatsapp_photo, bg='white',
                                        command=lambda contact_info=contact_info: self.whatsapp_clicked(contact_info),
                                        bd=0, padx=5, pady=15)
                whatsappButton.image = whatsapp_photo
                whatsappButton.pack()

                image = Image.open(BytesIO(image_data))
                max_width = 150
                max_height = 150
                image.thumbnail((max_width, max_height))
                photo = ImageTk.PhotoImage(image)
                image_label = tk.Label(info_frame, image=photo)
                image_label.image = photo
                image_label.pack(side=RIGHT, padx=20)

        else:
            print("No data found in the database.")

    def _on_mousewheel(self, event):
        self.canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")


root = Tk()
app = AdoptionApp(root)
root.mainloop()
