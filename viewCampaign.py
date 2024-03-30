from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import webbrowser
import subprocess
import mysql.connector
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

        # Resize the WhatsApp logo image
        whatsapp_image = Image.open("images/whatsapp (1).png")
        whatsapp_photo = ImageTk.PhotoImage(whatsapp_image)

        whatsappButton = Button(campaign_frame, image=whatsapp_photo, bg='white', command=self.whatsapp_clicked, bd=0, padx=5, pady=15)
        whatsappButton.image = whatsapp_photo
        whatsappButton.grid(row=4)

    def whatsapp_clicked(self):
        print("redirecting to whatsapp chat")
        whatsapp_url = f"https://wa.me/{self.campaign_contact_number}"
        webbrowser.open(whatsapp_url)

def fetch_campaigns_from_db():
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='userdata',
                                             user='root',
                                             password='Palve@08')  # Update with your MySQL password
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

# Initialize an empty list for campaigns
campaign_list = fetch_campaigns_from_db()

root = Tk()
logo_name(root)
root.geometry("800x600+100+100")

# Create the top bar
topbar,sidebar, buttons = create_sidebar(root,open_Volunteer_page, open_donation_page, open_rescue_section, open_adoption)


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
