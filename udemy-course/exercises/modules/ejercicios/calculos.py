from operaciones import suma, resta, multiplicacion, division

a, b, c, d = (10, 5, 0, "Hola")

print("{} + {} = {}".format(a, b, suma.sumar(a, b)))
print("{} - {} = {}".format(b, d, resta.restar(b, d)))
print("{} * {} = {}".format(b, b, multiplicacion.multiplicar(b, b)))
print("{} / {} = {}".format(a, c, division.dividir(a, c)))
