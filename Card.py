import tkinter as tk

def switch_to_card_page(root, cards_frame, display_cards, switch_to_main_menu):
    input_frame = root.nametowidget('input_frame')
    main_menu_frame = root.nametowidget('main_menu_frame')  # Retrieve main_menu_frame by name

    input_frame.pack_forget()
    main_menu_frame.pack_forget()
    cards_frame.pack(fill=tk.BOTH, expand=True)

    display_cards()

    switch_to_main_frame = tk.Frame(cards_frame)
    switch_to_main_frame.pack(pady=10)
    switch_to_main_button = tk.Button(switch_to_main_frame, text="Switch to Main", command=switch_to_main_menu)
    switch_to_main_button.pack()
