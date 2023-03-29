import sys

if len(sys.argv) == 3:
    text = sys.argv[1]
    times = int(sys.argv[2])

    for time in range(times):
        print(text)
else:
    print("Error - Introduce los argumentos correctamente")
    print("Ejemplo: python app.py [texto] [numero]")
