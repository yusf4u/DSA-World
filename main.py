from tkinter import Tk
from screens import home

root = Tk()
root.title("DSA World")
w = 1280
h = 740
root.geometry("1280x740")
root.resizable(False, False)

home.show_about(root)

root.mainloop()
