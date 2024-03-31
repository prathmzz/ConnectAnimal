from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
from sidebar import create_sidebar
from commmon_components import logo_name
import subprocess
import mysql.connector

def open_lecture_page():
    root.destroy()
    subprocess.run(["python", "lecture_page.py"])

def open_Volunteer_page():   
    root.destroy()
    subprocess.run(["python", "Volunteer_page.py"])

def open_teacher_section():   
    root.destroy()
    subprocess.run(["python", "teacher_section.py"])

def open_Rescue():
    root.destroy()

# def open_view_campaign():
#     root.destroy()
#     subprocess.run(["python", "viewCampaign.py"])

# def save_campaign():
#     root.destroy()
#     subprocess.run(["python", "Rescue.py"])

def save_campaign_to_db(name, location, contact_number, description):
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='userdata',
                                             user='root',
                                             password='v2wcoder@mysql#123')  # Update with your MySQL password
        cursor = connection.cursor()

        # SQL query to insert campaign details into the database
        sql_query = "INSERT INTO campaigns (name, location, contact_number, description) VALUES (%s, %s, %s, %s)"
        campaign_data = (name, location, contact_number, description)
        cursor.execute(sql_query, campaign_data)
        connection.commit()

        messagebox.showinfo("Success", "Campaign details saved successfully!")

    except mysql.connector.Error as error:
        messagebox.showerror("Error", f"Failed to save campaign details: {error}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

# Function to handle the "Save Campaign" button click
def save_campaign():
    # Get the campaign details from the entry fields
    name = name_entry.get()
    location = location_entry.get()
    contact_number = contact_entry.get()
    description = description_entry.get()

    # Save the campaign details to the database
    save_campaign_to_db(name, location, contact_number, description)

# Function to open the view campaign page
def open_view_campaign():
    root.destroy()
    subprocess.run(["python", "viewCampaign.py"])


root = Tk()
logo_name(root)
root.geometry("800x600+100+100")

topbar, sidebar, buttons = create_sidebar(root, open_lecture_page, open_Volunteer_page, open_teacher_section, open_Rescue)
frame = Frame(root, bg='white')
frame.place(x=162, y=0)  # Adjusted position to be next to the sidebar
root.title("Volunteer Page")
root.geometry("800x600+100+100")

# Create a frame for the button and label
button_frame = Frame(root, bg="white")
button_frame.pack(side=TOP, fill=X)

# Create the main frame
main_frame = Frame(root, bg="white")
main_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

# Add the label
heading = Label(main_frame, text='CAMPAIGN REGISTER', font=('Microsoft Yahei UI Light', 18, 'bold underline'), bg='white', fg='firebrick1')
heading.grid(row=0, column=0, padx=55, pady=10, columnspan=2)

# Add the entry fields
fields = [
    ('Name of Campaign', 1),
    ('Location', 3),
    ('Contact number', 5),
    ('Description of your Campaign', 7)
]

for text, row in fields:
    label = Label(main_frame, text=text, font=('Microsoft Yahei UI Light', 10, 'bold'), bg='white', fg='firebrick1')
    label.grid(row=row, column=0, sticky='w', padx=40, pady=(12, 0))

    entry = Entry(main_frame, width=30, font=('Microsoft Yahei UI Light', 10, 'bold'), bg='firebrick1', fg='white')
    entry.grid(row=row + 1, column=0, sticky='w', padx=40)


name_entry = Entry(main_frame, width=30, font=('Microsost Yahei UI Light', 10, 'bold'), bg='firebrick1', fg='white')
name_entry.grid(row=2, column=0, sticky='w', padx=40)

location_entry = Entry(main_frame, width=30, font=('Microsost Yahei UI Light', 10, 'bold'), bg='firebrick1', fg='white')
location_entry.grid(row=4, column=0, sticky='w', padx=40)

contact_entry = Entry(main_frame, width=30, font=('Microsost Yahei UI Light', 10, 'bold'), bg='firebrick1', fg='white')
contact_entry.grid(row=6, column=0, sticky='w', padx=40)

description_entry = Entry(main_frame, width=30, font=('Microsost Yahei UI Light', 10, 'bold'), bg='firebrick1', fg='white')
description_entry.grid(row=8, column=0, sticky='w', padx=40)

# Add the terms and conditions checkbox
check = IntVar()
termandconditions = Checkbutton(main_frame, text='I agree to the terms & conditions', font=('Microsoft Yahei UI Light', 8, 'bold'), fg='firebrick1', bg='white', activebackground='white', activeforeground='firebrick1', cursor='hand2', variable=check)
termandconditions.grid(row=9, column=0, padx=2, pady=13, columnspan=2)

# Add the "Add Campaign" button
addCampaign = Button(main_frame, text='Add Campaign', font=('Open Sans', 16, 'bold'), bd=0, bg='firebrick1', fg='white', activebackground='firebrick1', activeforeground='white', width=17, command=save_campaign)
addCampaign.grid(row=10, column=0, pady=10, columnspan=2)

# Add the "View Campaign" button
viewCampaign = Button(main_frame, text='View Campaigns', font=('Open Sans', 16, 'bold'), bd=0, bg='firebrick1', fg='white', activebackground='firebrick1', activeforeground='white', width=17, command=open_view_campaign)
viewCampaign.grid(row=11, column=0, pady=10, columnspan=2)

root.mainloop()
