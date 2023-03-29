def saludar():
    print("Saludo desde saludos.saludar()")

class Saludo:
    def __init__(self):
        print("Hola desde Saludo.__init__()")

"""
__name__ cambia dependiendo de donde se este ejecutando.
Si se ejecuta este archivo __name__ vale __main__ pero si se
ejecuta app.py y llama a este archivo, __name__ vale saludos.
Con esto se puede controlar lo que se ejecuta al hacer import
"""
print("__name__ en saludos: ", __name__)

if __name__ == "__main__":
    saludar()
