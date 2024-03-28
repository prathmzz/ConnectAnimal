from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import pymysql
import subprocess
from commmon_components import logo_name


# Functionality Part
def login_user():
    if usernameEntry.get() == '' or passwordEntry.get() == '':
        messagebox.showerror('Error', 'All fields are required')
    else:
        try:
            con = pymysql.connect(host='localhost', user='root', password='Palve@08', database='userdata')
            mycursor = con.cursor()

            query = 'select * from data where username=%s and password=%s'
            mycursor.execute(query, (usernameEntry.get(), passwordEntry.get()))
            row = mycursor.fetchone()

            if row is None:
                messagebox.showerror('Error', 'Invalid username or password')
            else:
                messagebox.showinfo('Welcome', 'Login is successful')
                open_main_page()

            con.close()

        except pymysql.Error as e:
            messagebox.showerror('Error', f'Connection issue: {e}')

def open_main_page():
    print("Opening main page...")
    login_window.destroy()
    subprocess.run(["python", "Home.py"])

def open_signup_page():
    login_window.destroy()
    import signup

# GUI part
login_window = Tk()
logo_name(login_window)
login_window.geometry('990x660+50+50')
login_window.resizable(0, 0)

bgImage = ImageTk.PhotoImage(file='images/1.jpg')
bgLabel = Label(login_window, image=bgImage)
bgLabel.place(x=0, y=0)

heading = Label(login_window, text='USER LOGIN', font=('Microsoft Yahei UI Light', 23, 'bold underline'), bg='white', fg='firebrick1')
heading.place(x=605, y=120)

# Username Entry
usernameEntry = Entry(login_window, width=25, font=('Microsoft Yahei UI Light', 11, 'bold'), bd=0, fg='firebrick1')
usernameEntry.place(x=580, y=200)
usernameEntry.insert(0, "Username")

# Password Entry
passwordEntry = Entry(login_window, width=25, font=('Microsoft Yahei UI Light', 11, 'bold'), bd=0, fg='firebrick1')
passwordEntry.place(x=580, y=260)
passwordEntry.insert(0, "Password")

openeye = PhotoImage(file='images/openeye.png')
eyeButton = Button(login_window, image=openeye, bd=0, bg='white', activebackground='white', cursor='hand2')
eyeButton.place(x=800, y=255)

forgetButton = Button(login_window, text='Forget Password?', bd=0, bg='white', activebackground='white', cursor='hand2', fg='firebrick1', font=('Microsoft Yahei UI Light', 9, 'bold'))
forgetButton.place(x=715, y=295)

loginButton = Button(login_window, text='Login', font=('Open Sans', 16, 'bold'), fg='white', bg='firebrick1', cursor='hand2', bd=0, width=19, foreground='white', command=login_user)
loginButton.place(x=578, y=350)

orLabel = Label(login_window, text='--------------OR--------------', font=('Open Sans', 16), fg='firebrick1', bg='white')
orLabel.place(x=583, y=400)

facebook_logo = PhotoImage(file='images/facebook.png')
fbLabel = Label(login_window, image=facebook_logo, bg='white')
fbLabel.place(x=640, y=440)

google_logo = PhotoImage(file='images/google.png')
gogLabel = Label(login_window, image=google_logo, bg='white')
gogLabel.place(x=690, y=440)

twitter_logo = PhotoImage(file='images/twitter.png')
twitterLabel = Label(login_window, image=twitter_logo, bg='white')
twitterLabel.place(x=740, y=440)

signUpLabel = Label(login_window, text='Dont Have An Account?', font=('Open Sans', 9, 'bold'), fg='firebrick1', bg='white')
signUpLabel.place(x=590, y=500)

newaccountButton = Button(login_window, text='Create new one!', font=('Open Sans', 9, 'bold underline'), fg='blue', bg='white', cursor='hand2', bd=0, foreground='blue',command=open_signup_page)
newaccountButton.place(x=727, y=500)

login_window.mainloop()