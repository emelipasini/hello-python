import random
import math

def leer_numero(inicio, fin, mensaje):
    
    while True:
        try:
            valor = int(input(mensaje))
        except:
            print("Error, numero no valido")
        else:
            if inicio <= valor <= fin:
                break
    
    return valor

def generador():
    numeros = leer_numero(1, 20, "¿Cuantos números quieres generar? [1-20]:")
    modo = leer_numero(
        1, 3, "¿Cómo quieres redondear los números? [1]Al alza [2]A la baja [3]Normal:"
    )

    list= []
    for i in range(numeros):
        num = random.uniform(0, 101)

        if modo == 1:
            num = math.ceil(num)
        elif modo == 2:
            num = math.floor(num)
        else:
            num = math.floor(num)

        list.append(num)

    return list

print(generador())
