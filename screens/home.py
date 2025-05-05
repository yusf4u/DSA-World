import tkinter as tk
from PIL import Image, ImageTk

def show_home(root, width, height):
    from screens.menu_page import show_menu  # Lazy import

    # Clear previous widgets
    for widget in root.winfo_children():
        widget.destroy()

    # Load and display background
    bg_image = Image.open("assets/backgrounds/bg.png")
    bg_image = bg_image.resize((width, height), Image.LANCZOS)
    bg_photo = ImageTk.PhotoImage(bg_image)

    bg_label = tk.Label(root, image=bg_photo)
    bg_label.image = bg_photo
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    # Button actions
    def start_game():
        show_menu(root, width, height)

    def show_about():
        about_window = tk.Toplevel(root)
        about_window.title("About")
        about_window.geometry("400x200")
        tk.Label(about_window,
                 text="DSA World by Your Name\nLearn DSA with visuals!",
                 font=("Courier", 16)).pack(pady=20)

    def exit_game():
        root.destroy()

    # Button styling
    btn_style = {
        "font": ("Courier", 20, "bold"),
        "width": 15,
        "fg": "white",
        "relief": "raised",
        "bd": 3
    }

    # Adjusted button positions (more central in the image's empty space)
    base_y = 0.55
    spacing = 0.12  # more spacing to match visual aesthetics

    tk.Button(root, text="Start", bg="#32CD32", command=start_game, **btn_style).place(relx=0.5, rely=base_y, anchor="center")
    tk.Button(root, text="About", bg="#FFA500", command=show_about, **btn_style).place(relx=0.5, rely=base_y + spacing, anchor="center")
    tk.Button(root, text="Exit", bg="#FF4500", command=exit_game, **btn_style).place(relx=0.5, rely=base_y + spacing * 2, anchor="center")