import tkinter as tk
from PIL import Image, ImageTk
from data_structures.queue_game import QueueGame
  # Import the QueueGame class to use it in this file

# دالة لإظهار صفحة القائمة (Menu)
def show_menu(root, width, height):
    for widget in root.winfo_children():
        widget.destroy()

    # خلفية القائمة
    bg_image = Image.open("assets/backgrounds/menu_bg.png")
    bg_image = bg_image.resize((width, height), Image.LANCZOS)
    bg_photo = ImageTk.PhotoImage(bg_image)

    bg_label = tk.Label(root, image=bg_photo)
    bg_label.image = bg_photo
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    # إعداد الخطوط
    pixel_font = ("Courier", 14, "bold")
    pixel_font_large = ("Courier", 24, "bold")

    # إطار Pixel Art حول العنوان
    title_frame = tk.Frame(root, bg="#222", bd=5, relief="ridge")
    title_label = tk.Label(title_frame,
                           text="CHOOSE YOUR DSA",
                           font=pixel_font_large,
                           fg="#00FFCC",
                           bg="#222",
                           padx=20, pady=10)
    title_label.pack()
    title_frame.place(relx=0.5, rely=0.08, anchor="center")

    # المواضيع
    topics = [
        ("STACK", "#1E90FF"),
        ("QUEUE", "#32CD32"),
        ("CIRCULAR QUEUE", "#FFD700"),
        ("HANOI TOWER", "#FF69B4"),
        ("SORTING LAND", "#FF8C00"),
        ("LINKED LIST", "#9370DB")
    ]

    buttons = []

    btn_style = {
        "font": pixel_font,
        "width": 24,
        "height": 2,
        "fg": "white",
        "relief": "raised",
        "bd": 4,
        "highlightbackground": "#000",
        "highlightthickness": 0,
        "activebackground": "#555"
    }

    # تخصيص الأزرار
    y_offset = 0.2
    for i, (label, color) in enumerate(topics):
        btn = tk.Button(root, text=label, bg=color, **btn_style,
                        command=lambda topic=label: on_topic_click(root, topic))
        btn.place(relx=0.5, rely=y_offset + i * 0.1, anchor="center")
        buttons.append(btn)

    # زر الرجوع مخصص بشكل Pixel
    def go_back():
        from screens.home import show_home
        show_home(root, width, height)

    back_frame = tk.Frame(root, bg="#111", bd=4, relief="ridge")
    back_btn = tk.Button(back_frame,
                         text="← BACK",
                         font=pixel_font,
                         bg="#333",
                         fg="#FFA07A",
                         activebackground="#555",
                         relief="flat",
                         command=go_back)
    back_btn.pack(padx=10, pady=5)
    back_frame.place(relx=0.08, rely=0.04)

    # Effect Transition: Fade-in effect for buttons
    def fade_in(index=0):
        if index < len(buttons):
            buttons[index].lift()  # Move the button to the top layer
            root.after(100, lambda: fade_in(index + 1))

    # Delay the fade-in effect for a smooth transition
    root.after(500, fade_in)

def on_topic_click(root, topic):
    if topic == "QUEUE":
        queue_game_screen(root)

def queue_game_screen(root):
    app = QueueGame(root)
