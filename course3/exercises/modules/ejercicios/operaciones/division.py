def dividir(a, b):
    try:
        result = a / b
        
    except TypeError:
        return "Error: Tipo de dato no válido"
    except ZeroDivisionError:
        return "Error: No es posible dividir entre cero"
    else:
        return result
