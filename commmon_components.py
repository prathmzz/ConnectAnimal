from tkinter import *
# from PIL import ImageTk
# from tkinter import messagebox
# import pymysql


def logo_name(considered_root,page=None):
    if page:{
        considered_root.title("Animal Connect - " + page)
    }
    else:
        considered_root.title("Animal Connect")

    logo_image = PhotoImage(file="images/paw.png")  # Replace "your_logo.png" with the path to your logo
    # Set app logo as window icon
    considered_root.iconphoto(True, logo_image)


# def back(root,page){
#     root.destroy()
#     import (page + "py")
# }