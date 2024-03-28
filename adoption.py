from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
from tkinter import messagebox
from sidebar import create_sidebar  # Import the create_sidebar function
import subprocess
from commmon_components import logo_name

def viewButton():
    root.destroy()
    subprocess.run(["python", "Card.py"])

def open_lecture_page():
    print("Opening Lecture Page...") 
    root.destroy()
    subprocess.run(["python", "lecture_page.py"])
def open_Volunteer_page():
    print("Opening Volunteer Page...")
    root.destroy()
    subprocess.run(["python", "Volunteer_page.py"])
def open_teacher_section():
    print("Opening Teacher Section Page...")
    root.destroy()
    subprocess.run(["python", "teacher_section.py"])
def open_Rescue():
    print("Opening Rescue Page...")
    root.destroy()
    subprocess.run(["python", "Rescue.py"])

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
logo_name(root)
root.geometry("800x600+100+100")

# Use the create_sidebar function to create the sidebar
topbar,sidebar, buttons = create_sidebar(root,open_Volunteer_page,open_lecture_page,open_Rescue,open_teacher_section)


# # Create a frame for the buttons in the white portion
# button_frame = Frame(root, bg="white")
# button_frame.pack(side=TOP, fill=X)

# Add the two additional buttons in the middle
frame =Canvas(root, bg="white")
frame.pack(side=TOP, fill=BOTH, expand=True)

# # Configure the scroll bar to scroll the frame
# scrollbar = Scrollbar(root, orient=VERTICAL)
# scrollbar.pack(side=RIGHT, fill=Y)

# # Configure the scroll bar to scroll the frame
# scrollbar.config(command=frame.yview)
# frame.config(yscrollcommand=scrollbar.set)

# Create a label widget to display the selected image

imageLabel = Label(frame,text='Pet Image',font=('Microsost Yahei UI Light',10,'bold'),bg='white',fg='firebrick1')
imageLabel.grid(row=1,column=0,sticky='w',padx=40,pady=(12,0))

#image
button = Button(frame, text="Open Image", command=open_image)
button.grid(row=2, column=0, padx=40, pady=(12, 0))

#email
phoneNumberLabel = Label(frame,text='Contact Number/Whatsapp Number',font=('Microsost Yahei UI Light',10,'bold'),bg='white',fg='firebrick1')
phoneNumberLabel.grid(row=3,column=0,sticky='w',padx=40,pady=(12,0))

phoneNumberEntry = Entry(frame,width=30,font=('Microsost Yahei UI Light',10,'bold'),bg='firebrick1',fg='white')
phoneNumberEntry.grid(row=4,column=0,sticky='w',padx=40)

#username
nameLabel = Label(frame,text='Pet Name',font=('Microsost Yahei UI Light',10,'bold'),bg='white',fg='firebrick1')
nameLabel.grid(row=5,column=0,sticky='w',padx=40,pady=(12,0))

nameEntry = Entry(frame,width=30,font=('Microsost Yahei UI Light',10,'bold'),bg='firebrick1',fg='white')
nameEntry.grid(row=6,column=0,sticky='w',padx=40)

#password
ageLabel = Label(frame,text='Age',font=('Microsost Yahei UI Light',10,'bold'),bg='white',fg='firebrick1')
ageLabel.grid(row=7,column=0,sticky='w',padx=40,pady=(12,0))

ageEntry = Entry(frame,width=30,font=('Microsost Yahei UI Light',10,'bold'),bg='firebrick1',fg='white')
ageEntry.grid(row=8,column=0,sticky='w',padx=40)

# confirm password
addressLabel = Label(frame,text='Address',font=('Microsost Yahei UI Light',10,'bold'),bg='white',fg='firebrick1')
addressLabel.grid(row=9,column=0,sticky='w',padx=40,pady=(12,0))

adressEntry = Entry(frame,width=30,font=('Microsost Yahei UI Light',10,'bold'),bg='firebrick1',fg='white')
adressEntry.grid(row=10,column=0,sticky='w',padx=40)

#terms and conditrions checkbox
termandconditions = Checkbutton(frame,text='I agree to the terms & conditions',font=('Microsost Yahei UI Light',8,'bold'),fg='firebrick1',bg='white',activebackground='white',activeforeground='firebrick1',cursor='hand2')
termandconditions.grid(row=11,column=0,padx=2,pady=13)

#Post button
postButton = Button(frame,text='POST',font=('Open Sans',16,'bold'),fg='white',bg='firebrick1',cursor='hand2',bd=0,width=19,foreground='white',command=newPost)
postButton.grid(row=12,column=0,padx=2,pady=13)
# Insert a space between the existing buttons and the new ones
# Label(button_frame, text="").pack(side=TOP, pady=10)



root.mainloop()