from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import webbrowser
import subprocess
from commmon_components import logo_name



class Campaign_Details:
    def __init__(self, campaign_name, campaign_location, campaign_description, campaign_contact_number):
        self.campaign_name = campaign_name
        self.campaign_location = campaign_location
        self.campaign_description = campaign_description
        self.campaign_contact_number = campaign_contact_number

    def display_campaign(self, row):
        campaign_frame = Frame(frame, bg='white', highlightbackground="black", highlightthickness=1)
        campaign_frame.grid(row=row, column=0, padx=20, pady=10, sticky="w")
        # campaign_frame.pack()

        campaign_name_label = Label(campaign_frame, text='Campaign Name:', font=('Microsoft Yahei UI Light', 10, 'bold'), bg='white', fg='firebrick1')
        campaign_name_label.grid(row=0, column=0, sticky='w')

        campaign_name_value = Label(campaign_frame, text=self.campaign_name, font=('Microsoft Yahei UI Light', 10), bg='white', fg='firebrick1')
        campaign_name_value.grid(row=0, column=1, sticky='w')

        campaign_location_label = Label(campaign_frame, text='Location:', font=('Microsoft Yahei UI Light', 10, 'bold'), bg='white', fg='firebrick1')
        campaign_location_label.grid(row=1, column=0, sticky='w')

        campaign_location_value = Label(campaign_frame, text=self.campaign_location, font=('Microsoft Yahei UI Light', 10), bg='white', fg='firebrick1')
        campaign_location_value.grid(row=1, column=1, sticky='w')

        campaign_description_label = Label(campaign_frame, text='Description:', font=('Microsoft Yahei UI Light', 10, 'bold'), bg='white', fg='firebrick1')
        campaign_description_label.grid(row=2, column=0, sticky='w')

        campaign_description_value = Label(campaign_frame, text=self.campaign_description, font=('Microsoft Yahei UI Light', 10), bg='white', fg='firebrick1')
        campaign_description_value.grid(row=2, column=1, sticky='w')

        campaign_contact_label = Label(campaign_frame, text='Contact Number:', font=('Microsoft Yahei UI Light', 10, 'bold'), bg='white', fg='firebrick1')
        campaign_contact_label.grid(row=3, column=0, sticky='w')

        campaign_contact_value = Label(campaign_frame, text=self.campaign_contact_number, font=('Microsoft Yahei UI Light', 10), bg='white', fg='firebrick1')
        campaign_contact_value.grid(row=3, column=1, sticky='w')

        # Resize the WhatsApp logo image
        whatsapp_image = Image.open("images/whatsapp (1).png")
        whatsapp_photo = ImageTk.PhotoImage(whatsapp_image)

        whatsappButton = Button(campaign_frame, image=whatsapp_photo, bg='white', command=whatsapp_clicked, bd=0,
                                padx=5, pady=15)
        whatsappButton.image = whatsapp_photo
        whatsappButton.grid(row=4)


def whatsapp_clicked():
    print("redirecting to whatsapp chat")
    vedant= +918779784305
    eesha = 9653360204
    phone_number = vedant
    whatsapp_url = f"https://wa.me/{phone_number}"
    webbrowser.open(whatsapp_url)


def append_campaign(campaign, campaign_list):
    campaign_list.append(campaign)
    print("campaign added successfully")

def open_Volunteer_page():
    root.destroy()
    subprocess.run(["python", "Volunteer_page.py"])
# Initialize an empty list for campaigns
campaign_list = []

# Create some sample Campaign_Details objects
campaign1 = Campaign_Details("vedant camp", "Location 1", "Description 1", "+918779784305")
campaign2 = Campaign_Details("eesha camp", "Location 2", "Description 2", "9653360204")

# Append campaigns to the list
append_campaign(campaign1, campaign_list)
append_campaign(campaign2, campaign_list)

root = Tk()
logo_name(root)
root.geometry("800x600+100+100")

# Create the top bar
topbar = Frame(root, bg="#ed5876", width=600, height=50)
topbar.pack(side=TOP, fill=X)

title = Button(topbar, text="Animal Connect", font=("Arial", 15, "bold"), bd=0, bg="#ed5876", fg="#ffffff", activebackground='#eb4163')
title.pack(side=LEFT, padx=20, pady=10)

user_icon_image = PhotoImage(file="images/settings_icon.png").subsample(2)
user_icon = Label(topbar, image=user_icon_image, bg="#ed5876")
user_icon.pack(side=RIGHT, padx=10, pady=10)

user_name = Label(topbar, text="Animal Connect", font=("Arial", 16), bg="#ed5876", fg="#ffffff")
user_name.pack(side=RIGHT, pady=10)

# Create the sidebar
sidebar = Frame(root, width=200, height=600, bg="#eb4163")
sidebar.pack(side=LEFT, fill=Y)

menu_items = [
    ("Volunteer", "home_icon.png"),
    ("Donation", "lecture_icon.png"),
    ("Adoption", "user_icon.png"),
    ("Rescue", "teacher_icon.png"),
]

buttons = []

for item in menu_items:
    image = Image.open("Images/" + item[1])
    photo_image = ImageTk.PhotoImage(image)
    button = Button(sidebar, text=item[0], image=photo_image, compound=LEFT, fg="white", bg="#eb4163", bd=0, padx=20,
                    pady=10, anchor="w")
    button.image = photo_image
    button.pack(anchor="w", fill=X)
    buttons.append(button)

# Create a frame for the content
content_frame = Frame(root, bg="white", width=600, height=550)
content_frame.pack(side=RIGHT, fill=BOTH, expand=True)
button_frame = Frame(content_frame, bg="white")
button_frame.pack(side=TOP, fill=X)
add_campaign_button = Button(button_frame, text="Back to volunteer page", fg="white", bg="#eb4163", bd=0, padx=20, pady=10,command=open_Volunteer_page)
add_campaign_button.pack(side=RIGHT, fill=X, padx=(50, 250), pady=(25, 25))  
# Create a frame for the campaign details
frame = Frame(content_frame, bg='white')
frame.pack(fill=BOTH, expand=True)

# Display each campaign from the list
for index, campaign in enumerate(campaign_list):
    campaign.display_campaign(index)



root.mainloop()
