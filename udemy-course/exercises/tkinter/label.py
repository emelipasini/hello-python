from tkinter import *

root = Tk()

# frame = Frame(root, width=480, height=320)
# frame.pack()

# label = Label(root, text="Hola mundo")
# label.place(x=0, y=0)

# Variables dinamicas
text = StringVar()
text.set("Nuevo texto")

# Imagen
image = PhotoImage(file="imagen.gif")
Label(root, image=image, bd=0).pack()

Label(root, text="Hola mundo").pack(anchor="nw")
Label(root, text="Una etiqueta").pack(anchor="center")
Label(root, text="Otra etiqueta mas").pack(anchor="se")

label = Label(root, text="Especial")
label.pack(anchor="center")
label.config(bg="lightgreen", fg="blue", font=("Verdana", 15))
label.config(textvariable=text)

root.mainloop()
