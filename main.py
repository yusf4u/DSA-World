
from tkinter import Tk
from screens import home

root = Tk()
root.title("DSA World")
w = 1280
h = 740
root.geometry(f"{w}x{h}")
root.resizable(False, False)

home.show_home(root, w, h)
root.mainloop()
