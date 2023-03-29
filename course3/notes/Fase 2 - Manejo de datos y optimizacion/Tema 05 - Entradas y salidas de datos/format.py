import sys

if len(sys.argv) == 2:
    number = sys.argv[1]
    count = len(number)

    if int(number) < 1 or int(number) > 9999:
        print("Error - Debe ingresar un numero del 1 al 9999")
    else:
        for i in range(count):
            print("{:04d}".format(int(number[count-1-i]) * 10 ** i))
else:
    print("Error - Debes ingresar un numero del 1 al 9999")
