from tkinter import *
import webbrowser
import subprocess
import mysql.connector
from PIL import Image, ImageTk
from commmon_components import logo_name
from sidebar import *


class Campaign_Details:
    def __init__(self, campaign_name, campaign_location, campaign_description, campaign_contact_number):
        self.campaign_name = campaign_name
        self.campaign_location = campaign_location
        self.campaign_description = campaign_description
        self.campaign_contact_number = campaign_contact_number

    def display_campaign(self, row):
        campaign_frame = Frame(frame, bg='white', highlightbackground="black", highlightthickness=1)
        campaign_frame.grid(row=row, column=0, padx=20, pady=10, sticky="w")

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

        # Button to open Google Form link
        google_form_button = Button(campaign_frame, text='Fill Form', font=('Microsoft Yahei UI Light', 10), bg='white', fg='firebrick1', command=self.open_google_form)
        google_form_button.grid(row=4, columnspan=2, pady=10)

    def open_google_form(self):
        print("Opening Google Form...")
        google_form_url = self.campaign_description
        webbrowser.open(google_form_url)


def fetch_campaigns_from_db():
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='userdata',
                                             user='root',
                                             password='v2wcoder@mysql#123')  # Update with your MySQL password
        cursor = connection.cursor()

        # SQL query to select all campaigns from the database
        sql_query = "SELECT * FROM campaigns"
        cursor.execute(sql_query)

        campaigns = []
        for row in cursor.fetchall():
            # Create Campaign_Details objects for each row retrieved from the database
            campaign = Campaign_Details(row[1], row[2], row[4], row[3])
            campaigns.append(campaign)

        return campaigns

    except mysql.connector.Error as error:
        print(f"Failed to fetch campaigns: {error}")
        return []

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()


def open_Volunteer_page():
    root.destroy()
    subprocess.run(["python", "Volunteer_page.py"])


def open_donation_page():
    root.destroy()
    subprocess.run(["python", "donation_page.py"])


# Initialize an empty list for campaigns
campaign_list = fetch_campaigns_from_db()

root = Tk()
logo_name(root)
root.geometry("800x600+100+100")

# Create the top bar
topbar, sidebar, buttons = create_sidebar(root, open_Volunteer_page, open_donation_page, open_rescue_section, open_adoption)

# Create a frame for the content
content_frame = Frame(root, bg="white", width=600, height=550)
content_frame.pack(side=RIGHT, fill=BOTH, expand=True)

# Add a canvas for scrolling
canvas = Canvas(content_frame, bg="white")
canvas.pack(side=LEFT, fill=BOTH, expand=True)

# Add a scrollbar
scrollbar = Scrollbar(content_frame, orient=VERTICAL, command=canvas.yview)
scrollbar.pack(side=RIGHT, fill=Y)

# Configure canvas scrolling
canvas.configure(yscrollcommand=scrollbar.set)
canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

# Create a frame inside the canvas to hold the campaign details
frame = Frame(canvas, bg='white')

# Add the frame to the canvas
canvas.create_window((0, 0), window=frame, anchor='nw')

button_frame = Frame(content_frame, bg="white")
button_frame.pack(side=TOP, fill=X)
add_campaign_button = Button(button_frame, text="Back to volunteer page", fg="white", bg="#eb4163", bd=0, padx=20, pady=10, command=open_Volunteer_page)
add_campaign_button.pack(side=RIGHT, fill=X, padx=(50, 250), pady=(25, 25))

# Display each campaign from the list
for index, campaign in enumerate(campaign_list):
    campaign.display_campaign(index)

root.mainloop()
