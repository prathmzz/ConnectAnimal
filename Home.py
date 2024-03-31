from tkinter import *
from PIL import Image, ImageTk
from sidebar import *
from commmon_components import logo_name


def open_home(root):
    pass

def next_image():
    global image_index
    image_index = (image_index + 1) % len(image_array)

    # Update the image
    image_path = "Images/" + image_array[image_index]
    storyImage = Image.open(image_path).resize((300, 300), Image.LANCZOS)
    storyPhoto = ImageTk.PhotoImage(storyImage)
    imagelabel1.config(image=storyPhoto)
    imagelabel1.image = storyPhoto

def prev_image():
    global image_index
    image_index = (image_index - 1) % len(image_array)

    # Update the image
    image_path = "Images/" + image_array[image_index]
    storyImage = Image.open(image_path).resize((300, 300), Image.LANCZOS)
    storyPhoto = ImageTk.PhotoImage(storyImage)
    imagelabel1.config(image=storyPhoto)
    imagelabel1.image = storyPhoto

root = Tk()
root.geometry("800x600+100+100")
logo_name(root)
topbar, sidebar, buttons = create_sidebar(root, open_Volunteer_page, open_donation_page, open_rescue_section,open_adoption)
welcome_label = Label(root, text="Welcome to Animal Connect", font=("kristen itc", 20, "underline"))
welcome_label.pack(pady=20)

button_frame = Frame(root, bg="lightblue", height=400)
button_frame.pack(side=TOP, fill=X)

previous_image = Image.open("Images/previous.png").resize((30, 30))
previous_photo = ImageTk.PhotoImage(previous_image)
previousButton = Button(button_frame, image=previous_photo, bg="lightblue",bd=0, command=prev_image)
previousButton.place(rely=0.5, anchor=W, relx=0.05)

nextImage = Image.open("Images/next-button.png").resize((30, 30))
nextphoto = ImageTk.PhotoImage(nextImage)
nextButton = Button(button_frame, image=nextphoto, bg="lightblue", bd=0, command=next_image)
nextButton.place(anchor=E, rely=0.5, relx=0.95)

image_array = ["adopt.jpg", "donation.jpg","Rescue.jpg","volunteeer.jpg"]
image_index = 3

image_path = "Images/" + image_array[image_index]  # Change to your image path
# Open and resize the image using Lanczos resampling
storyImage = Image.open(image_path).resize((300, 300), Image.LANCZOS)
storyPhoto = ImageTk.PhotoImage(storyImage)
imagelabel1 = Label(button_frame, image=storyPhoto)
imagelabel1.image = storyPhoto
imagelabel1.place(anchor=CENTER, relx=0.5, rely=0.5)




root.mainloop()
