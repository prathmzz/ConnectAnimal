from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
from tkinter import messagebox
from sidebar import create_sidebar  # Import the create_sidebar function

def open_Volunteer_page():
    print("Opening Volunteer Page...")

def open_lecture_page():
    print("Opening Lecture Page...")

def open_Rescue():
    print("Opening Rescue Page...")

def open_teacher_section():
    print("Opening Teacher Section...")

def open_image():
    # Open a file dialog to select an image file
    file_path = filedialog.askopenfilename(filetypes=[("Image files", ".png;.jpg;.jpeg;.gif")])

    # Check if a file was selected
    if file_path:
        # Open the image file
        image = Image.open(file_path)

        # Resize the image to fit within a maximum width and height
        max_width = 300
        max_height = 200
        image.thumbnail((max_width, max_height))

        # Display the image in a label
        photo = ImageTk.PhotoImage(image)

        # Destroy the "Open Image" button
        button.destroy()

        # Create a new label to display the image
        image_label = Label(frame, image=photo)
        image_label.photo = photo  # Keep a reference to avoid garbage collection
        image_label.grid(row=2, column=0, padx=40, pady=(12, 0))

def newPost():
    pet_name = nameEntry.get()
    messagebox.showinfo("Adoption Information", f"{pet_name} is ready to get adopted!")

    # Destroy the frame after displaying the message
    frame.destroy()

root = Tk()
root.title("Volunteer Page")

root.geometry("800x600+100+100")

# Use the create_sidebar function to create the sidebar
sidebar, topbar, buttons = create_sidebar(root, open_Volunteer_page, open_lecture_page, open_Rescue, open_teacher_section)

frame =Canvas(root, bg="white")
frame.pack(side=TOP, fill=BOTH, expand=True)

imageLabel = Label(frame,text='License/ Proof of Identity:',font=('Microsost Yahei UI Light',10,'bold'),bg='white',fg='black')
imageLabel.grid(row=1,column=0,sticky='w',padx=40,pady=(12,0))

button = Button(frame, text="Open Image", command=open_image)
button.grid(row=2, column=0, padx=40, pady=(12, 0))

phoneNumberLabel = Label(frame,text='Name:',font=('Microsost Yahei UI Light',10,'bold'),bg='white',fg='black')
phoneNumberLabel.grid(row=3,column=0,sticky='w',padx=40,pady=(12,0))

phoneNumberEntry = Entry(frame,width=30,font=('Microsost Yahei UI Light',10,'bold'),bg='#ffe3e3', fg='white')
phoneNumberEntry.grid(row=4,column=0,sticky='w',padx=40)

nameLabel = Label(frame,text='Contact:',font=('Microsost Yahei UI Light',10,'bold'),bg='white',fg='black')
nameLabel.grid(row=5,column=0,sticky='w',padx=40,pady=(12,0))

nameEntry = Entry(frame,width=30,font=('Microsost Yahei UI Light',10,'bold'),bg='#ffe3e3',fg='white')
nameEntry.grid(row=6,column=0,sticky='w',padx=40)

ageLabel = Label(frame,text='Email:',font=('Microsost Yahei UI Light',10,'bold'),bg='white',fg='black')
ageLabel.grid(row=7,column=0,sticky='w',padx=40,pady=(12,0))

ageEntry = Entry(frame,width=30,font=('Microsost Yahei UI Light',10,'bold'),bg='#ffe3e3',fg='white')
ageEntry.grid(row=8,column=0,sticky='w',padx=40)

addressLabel = Label(frame,text='Address:',font=('Microsost Yahei UI Light',10,'bold'),bg='white',fg='black')
addressLabel.grid(row=9,column=0,sticky='w',padx=40,pady=(12,0))

adressEntry = Entry(frame,width=30,font=('Microsost Yahei UI Light',10,'bold'),bg='#ffe3e3',fg='white')
adressEntry.grid(row=10,column=0,sticky='w',padx=40)

descLabel = Label(frame,text='Description:',font=('Microsost Yahei UI Light',10,'bold'),bg='white',fg='black')
descLabel.grid(row=11,column=0,sticky='w',padx=40,pady=(12,0))

descEntry = Entry(frame,width=30,font=('Microsost Yahei UI Light',10,'bold'),bg='#ffe3e3',fg='white')
descEntry.grid(row=12,column=0,sticky='w',padx=40)

termandconditions = Checkbutton(frame,text='I agree to the terms & conditions',font=('Microsost Yahei UI Light',8,'bold'),fg='firebrick1',bg='white',activebackground='white',activeforeground='firebrick1',cursor='hand2')
termandconditions.grid(row=13,column=0,padx=2,pady=13)

postButton = Button(frame,text='POST',font=('Open Sans',16,'bold'),fg='white',bg='red',cursor='hand2',bd=0,width=19,foreground='white',command=newPost)
postButton.grid(row=14,column=0,padx=2,pady=13)

for button in buttons:
    button.config(command=open_Volunteer_page)

root.mainloop()

