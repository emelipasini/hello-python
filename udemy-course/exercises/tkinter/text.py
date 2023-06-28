from tkinter import *

root = Tk()

text = Text(root)
text.pack()
text.config(width=30, height=10, font=("Consolas", 12), padx=10, pady=10, selectbackground="red")

root.mainloop()
