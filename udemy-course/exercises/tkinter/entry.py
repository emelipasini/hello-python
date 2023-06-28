from tkinter import *

root = Tk()

label = Label(root, text="Nombre ")
label.grid(row=0, column=0, sticky="w", padx=5, pady=5)

entry = Entry(root)
entry.grid(row=0, column=1, sticky="w", padx=5, pady=5)
entry.config(state="disabled")

label2 = Label(root, text="Apellido ")
label2.grid(row=1, column=0, sticky="w", padx=5, pady=5)

entry2 = Entry(root)
entry2.grid(row=1, column=1, sticky="w", padx=5, pady=5)
entry2.config(justify="center")

label3 = Label(root, text="Contraseña ")
label3.grid(row=3, column=0, sticky="w", padx=5, pady=5)

entry3 = Entry(root)
entry3.grid(row=3, column=1, sticky="w", padx=5, pady=5)
entry3.config(justify="center", show="*")

# frame = Frame(root)
# frame.pack()

# entry = Entry(frame)
# entry.pack(side="right")

# label = Label(frame, text="Nombre  ")
# label.pack(side="left")

# frame2 = Frame(root)
# frame2.pack()

# entry2 = Entry(frame2)
# entry2.pack(side="right")

# label2 = Label(frame2, text="Apellido ")
# label2.pack(side="left")

root.mainloop()
