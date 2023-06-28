import csv

import config

class Cliente:
    def __init__(self, dni, nombre, apellido):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido

    def __str__(self):
        return f"({self.dni}) {self.nombre} {self.apellido}"
    
class Clientes:
    lista = []

    with open(config.DATABASE_PATH) as fichero:
        reader = csv.reader(fichero, delimiter=";")
        for dni, nombre, apellido in reader:
            cliente = Cliente(dni, nombre, apellido)
            lista.append(cliente)

    @staticmethod
    def buscar(dni):
        for cliente in Clientes.lista:
            if cliente.dni == dni:
                return cliente
        return None
    
    @staticmethod
    def crear(dni, nombre, apellido):
        cliente = Clientes.buscar(dni)
        if cliente is None:
            cliente = Cliente(dni, nombre, apellido)
            Clientes.lista.append(cliente)

            Clientes.guardar()
            return cliente
        else:
            raise Exception("El cliente ya existe")
    
    @staticmethod
    def modificar(dni, nombre, apellido):
        cliente = Clientes.buscar(dni)
        if cliente is not None:
            cliente.nombre = nombre
            cliente.apellido = apellido

            Clientes.guardar()
            return cliente
        else:
            raise Exception("El cliente no existe")
    
    @staticmethod
    def borrar(dni):
        cliente = Clientes.buscar(dni)
        if cliente is not None:
            Clientes.lista.remove(cliente)
            
            Clientes.guardar()
            return cliente
        else:
            raise Exception("El cliente no existe")
        
    @staticmethod
    def guardar():
        with open(config.DATABASE_PATH, "w", newline="\n") as fichero:
            writer = csv.writer(fichero, delimiter=";")
            for cliente in Clientes.lista:
                writer.writerow((cliente.dni, cliente.nombre, cliente.apellido))
    