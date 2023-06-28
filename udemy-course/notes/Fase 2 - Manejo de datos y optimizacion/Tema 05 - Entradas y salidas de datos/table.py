import sys

if len(sys.argv) == 3:
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    
    if(a < 1 or a > 9 or b < a or b > 9):
        print("Error - los numeros deben ser positivos del 1 al 9")
    else:
        for i in range(a):
            for j in range(b):
                print(" * ",end="")
            print()
else:
    print("Error - Debes introductir 2 numeros enteros del 1 al 9")
    print("Por ejemplo python table.py 5 5")