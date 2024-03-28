import tkinter as tk
import webbrowser

def open_whatsapp_chat():
    # Specify the phone number with country code
    phone_number = "1234567890"
    # Construct the WhatsApp URL
    whatsapp_url = f"https://wa.me/{phone_number}"
    # Open the URL in a web browser
    webbrowser.open(whatsapp_url)

root = tk.Tk()
root.title("WhatsApp Enquiry Chat")

# Create a button to open WhatsApp chat
whatsapp_button = tk.Button(root, text="Click here to start WhatsApp Chat", command=open_whatsapp_chat)
whatsapp_button.pack(pady=20)

root.mainloop()
