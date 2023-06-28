from tkinter import Tk, Toplevel, Frame, Scrollbar, Button, Label, Entry, ttk
from tkinter.messagebox import askokcancel, WARNING

import database as db
from helpers import validar_dni

class CenterWidget:
    def center(self):
        self.update() # type: ignore
        width = self.winfo_width() # type: ignore
        height = self.winfo_height() # type: ignore

        screen_width = self.winfo_screenwidth() # type: ignore
        screen_height = self.winfo_screenheight() # type: ignore

        x = int((screen_width - width) // 2)
        y = int((screen_height - height) // 2)

        self.geometry(f"{width}x{height}+{x}+{y}") # type: ignore

class ClientWindow(Toplevel, CenterWidget):
    def __init__(self, cliente=None, window_type="create"):
        super().__init__(cliente)
        self.title("Nuevo cliente" if window_type == "create" else "Editar cliente")
        self.build(window_type)
        self.center()
        self.transient(cliente)
        self.grab_set()
    
    def build(self, window_type):
        frame = Frame(self)
        frame.pack(padx=20, pady=10)

        Label(frame, text="DNI").grid(row=0, column=0, sticky="e")
        Label(frame, text="Nombre").grid(row=1, column=0, sticky="e")
        Label(frame, text="Apellido").grid(row=2, column=0, sticky="e")

        dni = Entry(frame)
        dni.grid(row=0, column=1, sticky="ew", padx=5, pady=5)
        dni.bind("<KeyRelease>", lambda event: self.validate(event, 0))
        nombre = Entry(frame)
        nombre.grid(row=1, column=1, sticky="ew", padx=5, pady=5)
        nombre.bind("<KeyRelease>", lambda event: self.validate(event, 1))
        apellido = Entry(frame)
        apellido.grid(row=2, column=1, sticky="ew", padx=5, pady=5)
        apellido.bind("<KeyRelease>", lambda event: self.validate(event, 2))

        if window_type == "edit":
            print("edit")
            client = self.master.treeview.focus() # type: ignore
            campos = self.master.treeview.item(client)["values"] # type: ignore
            dni.insert(0, campos[0])
            nombre.insert(0, campos[1])
            apellido.insert(0, campos[2])

        frame = Frame(self)
        frame.pack(pady=10)

        crear = Button(frame, text="Guardar", command=self.edit_client)
        crear.configure(state="disabled") if window_type == "create" else crear.configure(state="normal")
        crear.grid(row=0, column=0, padx=5)
        Button(frame, text="Cancelar", command=self.close).grid(row=0, column=1, padx=5)

        self.validaciones = [0, 0, 0] if window_type == "create" else [1, 1, 1]
        self.crear = crear
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        self.window_type = window_type

    def edit_client(self):
        if self.window_type == "create":
            self.master.treeview.insert( # type: ignore
                parent="", index="end", iid=self.dni.get(), text="",
                values=(self.dni.get(), self.nombre.get(), self.apellido.get())
            )
            db.Clientes.crear(self.dni.get(), self.nombre.get(), self.apellido.get())
        else:
            cliente = self.master.treeview.focus()  # type: ignore
            self.master.treeview.item(  # type: ignore
                cliente, values=(self.dni.get(), self.nombre.get(),
                                self.apellido.get())
            )
            db.Clientes.modificar(self.dni.get(), self.nombre.get(), self.apellido.get())

        self.close()

    def close(self):
        self.destroy()
        self.update()

    def validate(self, event, index):
        valor = event.widget.get()
        if index == 0:
            valido = validar_dni(valor, db.Clientes.lista)
        else:
            valido = valor.isalpha() and len(valor) > 2 and len(valor) < 20

        if valido:
            event.widget.configure(bg="green")
        else:
            event.widget.configure(bg="red")
        
        self.validaciones[index] = valido
        if all(self.validaciones):
            self.crear.configure(state="normal")

class MainWindow(Tk, CenterWidget):
    def __init__(self):
        super().__init__()
        self.title("Gestor de clientes")
        self.build()
        self.center()

    def build(self):
        frame = Frame(self)
        frame.pack()

        treeview = ttk.Treeview(frame)
        treeview["columns"] = ("DNI", "Nombre", "Apellido")

        treeview.column("#0", width=0, stretch=False)
        treeview.column("DNI", anchor="center")
        treeview.column("Nombre", anchor="center")
        treeview.column("Apellido", anchor="center")

        treeview.heading("DNI", text="DNI", anchor="center")
        treeview.heading("Nombre", text="Nombre", anchor="center")
        treeview.heading("Apellido", text="Apellido", anchor="center")

        scrollbar = Scrollbar(frame)
        scrollbar.pack(side="right", fill="y")

        treeview["yscrollcommand"] = scrollbar.set

        for cliente in db.Clientes.lista:
            treeview.insert(
                parent="", index="end", iid=cliente.dni, text="", 
                values=(cliente.dni, cliente.nombre, cliente.apellido)
            )

        treeview.pack()

        frame = Frame(self)
        frame.pack(pady=20)

        Button(frame, text="Crear", command=self.create_client).grid(row=0, column=0, padx=5)
        Button(frame, text="Modificar", command=self.edit_client).grid(row=0, column=1, padx=5)
        Button(frame, text="Borrar", command=self.delete_client).grid(row=0, column=2, padx=5)

        self.treeview = treeview
    
    def create_client(self):
        ClientWindow(self, window_type="create")
    
    def edit_client(self,):
        if self.treeview.focus():
            ClientWindow(self, window_type="edit")

    def delete_client(self):
        cliente = self.treeview.focus()
        if cliente:
            campos = self.treeview.item(cliente)["values"]

            confirmar = askokcancel(
                title="Eliminar cliente",
                message=f"¿Está seguro de eliminar a {campos[1]} {campos[2]}?",
                icon=WARNING
            )

            if confirmar:
                self.treeview.delete(cliente)
                db.Clientes.borrar(campos[0])

if __name__ == "__main__":
    window = MainWindow()
    window.mainloop()
