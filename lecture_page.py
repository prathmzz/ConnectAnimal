# from tkinter import *
# import tkinter as tk
# from PIL import Image, ImageTk
# from sidebar import create_sidebar
# import subprocess
# def open_lecture_page():
#     print("Opening Lecture Page...") 
#     root.destroy()

#     subprocess.run(["python", "lecture_page.py"])
# def open_Volunteer_page():
#     print("Opening Volunteer Page...")
#     root.destroy()

#     subprocess.run(["python", "Volunteer_page.py"])
# def open_teacher_section():
#     print("Opening Teacher Section Page...")
#     root.destroy()

#     subprocess.run(["python", "teacher_section.py"])
# def open_Rescue():
#     print("Opening Rescue Page...")
#     root.destroy()

#     subprocess.run(["python", "Rescue.py"])

# root = Tk()
# root.title("Animal Connect")
# root.geometry("800x600+100+100")

# # Call create_sidebar with the required arguments
# topbar, sidebar, buttons = create_sidebar(root, open_lecture_page, open_Volunteer_page, open_teacher_section, open_Rescue)

# # Add specific content for the lecture page
# # label = Label(root, text="Lecture Page Content")
# # button_frame = Frame(root, bg="white")
# # button_frame.pack(side=TOP, fill=X)
# # # Add the two additional buttons in the middle
# # add_campaign_button = Button(button_frame, text="Post for donation", fg="white", bg="#eb4163", bd=0, padx=20, pady=10)
# # add_campaign_button.pack(side=TOP, fill=X, padx=20, pady=(50, 0))  # Adjust pady to add space
# # view_campaign_button = Button(button_frame, text="View Donation", fg="white", bg="#eb4163", bd=0, padx=20, pady=10)
# # view_campaign_button.pack(side=TOP, fill=X, padx=20, pady=(10, 0))  # Adjust pady to add space
# # # label.pack()
# label = tk.Label(root, text="Donation Page")

# # Pack the label widget to display it in the window
# label.pack()

# root.mainloop()
from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
import subprocess
from sidebar import *  # Import the create_sidebar function
from commmon_components import logo_name


# def open_donation_page():
#     print("Opening Lecture Page...")
#     subprocess.run(["python", "lecture_page.py"])
#
# def open_Volunteer_page():
#     print("Opening Volunteer Page...")
#     subprocess.run(["python", "Volunteer_page.py"])
#
# def open_rescue_section():
#     print("Opening Teacher Section Page...")
#     subprocess.run(["python", "Rescue.py"])
#
# def open_adoption():
#     print("Opening Rescue Page...")
#     subprocess.run(["python", "teacher_section.py"])
def open_donation_form():
    print("Opening Donation Form...")
    root.destroy()
    subprocess.run(["python", "donation_form.py"])

root = Tk()
logo_name(root)
root.geometry("800x600+100+100")

# Call create_sidebar with the required arguments
topbar, sidebar, buttons = create_sidebar(root, open_Volunteer_page, open_donation_page, open_rescue_section, open_adoption)

# # Add specific content for the lecture page
# label = tk.Label(root, text="Donation Page")
# label.pack()

# Add a button to request for donation
request_donation_button = Button(root, text="Request Donation", command=open_donation_form, bg="red", fg="white", font=("Arial", 10), padx=10, pady=10)
request_donation_button.place(relx=0.6, rely=0.15, anchor=N)

explanation_text = "Click the button above to request donation. Fill in the required information in the form."
explanation_label = Label(root, text=explanation_text, fg="black", font=("Arial", 10), padx=5, pady=5)
explanation_label.place(relx=0.6, rely=0.24, anchor=N)




root.mainloop()