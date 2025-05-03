import tkinter as tk
from tkinter import font
from PIL import Image, ImageTk

def show_home(root, width, height):
    # Load and resize background image
    bg_image = Image.open("assets/backgrounds/main_menu_bg.png")
    bg_image = bg_image.resize((width, height), Image.LANCZOS)
    bg_photo = ImageTk.PhotoImage(bg_image)

    # Create background label
    bg_label = tk.Label(root, image=bg_photo)
    bg_label.image = bg_photo  # Keep a reference
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    # Button callbacks
    def start_game():
        print("Start pressed - go to level selection")

    def show_about():
        about_window = tk.Toplevel(root)
        about_window.title("About")
        about_window.geometry("400x200")
        tk.Label(about_window,
                 text="DSA World by Your Name\nLearn DSA with visuals!",
                 font=("Courier", 16)).pack(pady=20)

    def exit_game():
        root.destroy()

    # Buttons with semi-transparent background
    btn_style = {
        "font": ("Courier", 20, "bold"),
        "width": 15,
        "fg": "white",
        "relief": "raised",
        "bd": 3
    }
    posx = 0.46
    posy = 0.55
    diff = 0.1

    # Center coordinates for buttons
    start_btn = tk.Button(root,
                          text="Start",
                          bg="#32CD32",
                          command=start_game,
                          **btn_style)
    start_btn.place(relx=posx, rely=posy, anchor="center")

    about_btn = tk.Button(root,
                          text="About",
                          bg="#FFA500",
                          command=show_about,
                          **btn_style)
    about_btn.place(relx=posx, rely=posy + diff, anchor="center")

    exit_btn = tk.Button(root,
                         text="Exit",
                         bg="#FF4500",
                         command=exit_game,
                         **btn_style)
    exit_btn.place(relx=posx, rely=posy + diff * 2, anchor="center")

  