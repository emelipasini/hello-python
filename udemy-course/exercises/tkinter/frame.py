from tkinter import *

root = Tk()

root.title("Hola mundo")
root.iconbitmap("hola.ico")
root.resizable(True, True)

root.config(cursor="arrow")
root.config(bg="blue")
root.config(bd=15)
root.config(relief="ridge")

frame = Frame(root, width=480, height=320)
# anchor: e(ast) w(est) n(orth) s(outh)
frame.pack(side="bottom", anchor="e")
# frame.pack(fill="x")
# frame.pack(fill="y", expand=1)
# frame.pack(fill="both", expand=1)
frame.config(cursor="pirate")
frame.config(bg="lightblue")
frame.config(bd=25)
frame.config(relief="sunken")

root.mainloop()
