from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
from sidebar import create_sidebar
from viewCampaign import campaign_list, Campaign_Details, append_campaign


def campaign_add():
    campaign_name = campaignNameEntry.get()
    campaign_location = locationEntry.get()
    campaign_description = descriptionEntry.get()
    campaign_contact_number = numberEntry.get()

    print("Campaign Name:", campaign_name)
    print("Location:", campaign_location)
    print("Description:", campaign_description)
    print("Contact Number:", campaign_contact_number)

    campaign = Campaign_Details(campaign_name, campaign_location, campaign_description, campaign_contact_number)
    append_campaign(campaign,campaign_list)
    print("campaign pathavla")
    messagebox.showinfo("Campaign Added", f"Campaign '{campaign_name}' added successfully!")

root = Tk()
root.title("Volunteer Page")
root.geometry("800x600+100+100")

# Use the create_sidebar function to create the sidebar
sidebar, buttons = create_sidebar(root)

# Create a frame for the buttons in the white portion
button_frame = Frame(root, bg="white")
button_frame.pack(side=TOP, fill=X)

# Add the two additional buttons in the middle
frame = Frame(root, bg='white')
frame.place(x=162, y=0)  # Adjusted position to be next to the sidebar

heading = Label(frame, text='CAMPAIGN REGISTER', font=('Microsoft Yahei UI Light', 18, 'bold underline'), bg='white', fg='firebrick1')
heading.grid(row=0, column=0, padx=55, pady=10)

# email
campaignName = Label(frame, text='Name of Campaign', font=('Microsost Yahei UI Light', 10, 'bold'), bg='white', fg='firebrick1')
campaignName.grid(row=1, column=0, sticky='w', padx=40, pady=(12, 0))

campaignNameEntry = Entry(frame, width=30, font=('Microsost Yahei UI Light', 10, 'bold'), bg='firebrick1', fg='white')
campaignNameEntry.grid(row=2, column=0, sticky='w', padx=40)

# username
locationLabel = Label(frame, text='Location', font=('Microsost Yahei UI Light', 10, 'bold'), bg='white', fg='firebrick1')
locationLabel.grid(row=3, column=0, sticky='w', padx=40, pady=(12, 0))

locationEntry = Entry(frame, width=30, font=('Microsost Yahei UI Light', 10, 'bold'), bg='firebrick1', fg='white')
locationEntry.grid(row=4, column=0, sticky='w', padx=40)

# password
WhatsappNumberLabel = Label(frame, text='Contact number', font=('Microsost Yahei UI Light', 10, 'bold'), bg='white', fg='firebrick1')
WhatsappNumberLabel.grid(row=5, column=0, sticky='w', padx=40, pady=(12, 0))

numberEntry = Entry(frame, width=30, font=('Microsost Yahei UI Light', 10, 'bold'), bg='firebrick1', fg='white')
numberEntry.grid(row=6, column=0, sticky='w', padx=40)

# confirm password
descriptionLabel = Label(frame, text='Description of your Campaign', font=('Microsost Yahei UI Light', 10, 'bold'), bg='white', fg='firebrick1')
descriptionLabel.grid(row=7, column=0, sticky='w', padx=40, pady=(12, 0))

descriptionEntry = Entry(frame, width=30, font=('Microsost Yahei UI Light', 10, 'bold'), bg='firebrick1', fg='white')
descriptionEntry.grid(row=8, column=0, sticky='w', padx=40)

# terms and conditions checkbox
check = IntVar()
termandconditions = Checkbutton(frame, text='I agree to the terms & conditions', font=('Microsost Yahei UI Light', 8, 'bold'), fg='firebrick1', bg='white', activebackground='white', activeforeground='firebrick1', cursor='hand2', variable=check)
termandconditions.grid(row=9, column=0, padx=2, pady=13)

# signup button
addCampaign = Button(frame, text='Add Campaign', font=('Open Sans', 16, 'bold'), bd=0, bg='firebrick1', fg='white', activebackground='firebrick1', activeforeground='white', width=17,command=campaign_add)
addCampaign.grid(row=10, column=0, pady=10)

root.mainloop()
