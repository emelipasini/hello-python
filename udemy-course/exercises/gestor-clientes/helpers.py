import os
import re
import platform

def limpiar_pantalla():
    """Limpia la pantalla según el sistema operativo"""
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

    # Version ternario
    # os.system("cls") if platform.system() == "Windows" else os.system("clear")

def leer_texto(min=0, max=0, mensaje=None):
    """Lee un texto de la entrada estándar y valida la longitud"""
    print(mensaje) if mensaje else None

    while True:
        texto = input("> ")
        
        if len(texto) >= min and len(texto) <= max:
            return texto
        else:
            print(f"El texto debe tener entre {min} y {max} caracteres")

def validar_dni(dni, lista):
    if not re.match("^[0-9]{7}[A-Z]$", dni):
        print("El DNI no cumple con el formato.")
        return False
    
    for cliente in lista:
        if cliente.dni == dni:
            print("El DNI ya existe.")
            return False
        
    return True
