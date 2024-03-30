from tkinter import *
import tkinter as tk
from sidebar import * # Import the create_sidebar function
import subprocess
from commmon_components import logo_name



root = Tk()
logo_name(root)
root.geometry("800x600+100+100")

# Use the create_sidebar function to create the sidebar
topbar,sidebar, buttons = create_sidebar(root,open_Volunteer_page, open_donation_page, open_rescue_section, open_adoption)
welcome_label = Label(root, text="Welcome to Animal Connect", font=("Arial", 20))
welcome_label.pack(pady=20)
root.mainloop()