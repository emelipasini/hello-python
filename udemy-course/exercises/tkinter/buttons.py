from tkinter import *

def hello():
    print("Hello!")

def create_label():
    Label(root, text="Dynamically created label").pack()

def add():
    a = float(n1.get())
    b = float(n2.get())
    r.set(a + b)

root = Tk()
root.config(bd=15)

n1 = StringVar()
n2 = StringVar()
r = StringVar()

Label(root, text="Primer numero").pack()
Entry(root, justify="center", textvariable=n1).pack()
Label(root, text="Segundo numero").pack()
Entry(root, justify="center", textvariable=n2).pack()
Button(root, text="Add", command=add).pack()
Label(root, text="Resultado").pack()
Entry(root, justify="center", textvariable=r, state="disabled").pack()



root.mainloop()
