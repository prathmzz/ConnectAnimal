from tkinter import *
import tkinter as tk
from sidebar import *  # Import the create_sidebar function
import subprocess
from commmon_components import logo_name

def open_post_donation_page():
     root.destroy()
     subprocess.run(["python", "donation_form.py"])

def  open_viewDonation():
    root.destroy()
    import viewDonation

root = Tk()
logo_name(root,"Donation")
root.geometry("800x600+100+100")

# Use the create_sidebar function to create the sidebar
topbar,sidebar, buttons = create_sidebar(root,open_Volunteer_page, open_donation_page, open_rescue_section, open_adoption)


button_frame = Frame(root, bg="white")
button_frame.pack(side=TOP, fill=X)
add_donation_button = Button(button_frame, text="Request Donation", fg="white", bg="#eb4163", bd=0,font=("Jungle Fever", 12,"bold"), padx=20, pady=10,command=open_post_donation_page)
add_donation_button.pack(side=TOP, fill=X, padx=20, pady=(50, 0))

view_donation_post = Button(button_frame, text="Donate ", fg="white", bg="#eb4163", bd=0,font=("Jungle Fever", 12,"bold"), padx=20, pady=10,command=open_viewDonation)
view_donation_post.pack(side=TOP, fill=X, padx=20, pady=(50, 0))

# Load and resize the image
image = Image.open("images/bg-2.png")
image = image.resize((700, 250), Image.LANCZOS)  # Resize the image to fill remaining space
photo = ImageTk.PhotoImage(image)

# Create a label to display the image
image_label = Label(root, image=photo)
image_label.image = photo  # Keep a reference to avoid garbage collection
image_label.pack(fill=BOTH, expand=True,pady=(128,0))

root.mainloop()
