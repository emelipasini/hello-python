def sumar(a, b):
    try:
        result = a + b
        
    except TypeError:
        return "Error: Tipo de dato no válido"
    else:
        return result
