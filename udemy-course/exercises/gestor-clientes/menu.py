import database as db
from helpers import limpiar_pantalla, leer_texto, validar_dni

def iniciar():

    while True:
        limpiar_pantalla()

        print("========================")
        print("  Bienvenido al Gestor  ")
        print("========================")
        print("[1] Listar los clientes")
        print("[2] Buscar un cliente")
        print("[3] Agregar un cliente")
        print("[4] Modificar un cliente")
        print("[5] Borrar un cliente")
        print("[6] Cerrar el gestor")
        print("========================")

        opcion = input("> ")
        limpiar_pantalla()

        if opcion == "1":
            for cliente in db.Clientes.lista:
                print(cliente)
        elif opcion == "2":
            dni = leer_texto(min=8, max=8, mensaje="Ingrese el DNI del cliente: ").upper()
            cliente = db.Clientes.buscar(dni)
            print(cliente) if cliente else print("No se encontró el cliente")
        elif opcion == "3":
            dni = None
            while True:
                dni = leer_texto(min=8, max=8, mensaje="Ingrese el DNI del cliente: ").upper()
                dni_is_valid = validar_dni(dni, db.Clientes.lista)
                if dni_is_valid:
                    break

            nombre = leer_texto(min=2, max=20, mensaje="Ingrese el nombre del cliente: ").capitalize()
            apellido = leer_texto(min=2, max=20, mensaje="Ingrese el apellido del cliente: ").capitalize()

            db.Clientes.crear(dni, nombre, apellido)
            print("Cliente agregado correctamente")
        elif opcion == "4":
            dni = leer_texto(min=8, max=8, mensaje="Ingrese el DNI del cliente: ").upper()

            cliente = db.Clientes.buscar(dni)
            if cliente:
                nombre = leer_texto(
                    min=2, max=20, mensaje=f"Ingrese el nuevo nombre del cliente: [{cliente.nombre}]"
                ).capitalize()
                apellido = leer_texto(
                    min=2, max=20, mensaje=f"Ingrese el nuevo apellido del cliente: [{cliente.apellido}]"
                ).capitalize()

                db.Clientes.modificar(cliente.dni, nombre, apellido)
                print("Cliente modificado correctamente")
            else:
                print("No se encontró el cliente")
        elif opcion == "5":
            dni = leer_texto(min=8, max=8, mensaje="Ingrese el DNI del cliente: ").upper()

            cliente = db.Clientes.buscar(dni)
            if cliente:
                db.Clientes.borrar(cliente.dni)
                print("Cliente borrado correctamente")
            else:
                print("No se encontró el cliente")
        elif opcion == "6":
            print("Cerrando el gestor...")
            break
        else:
            print("Opción incorrecta")

        input("\nPresione ENTER para continuar...")

