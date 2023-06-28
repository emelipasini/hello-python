import sys
import os

from tkinter import Tk, PhotoImage, Label


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS # type: ignore
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

root = Tk()
image = PhotoImage(file=resource_path("public/relax.png"))
Label(image=image).pack(padx=50, pady=50)
root.mainloop()
