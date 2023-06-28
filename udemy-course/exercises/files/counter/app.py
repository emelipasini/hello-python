from io import open
import sys

def open_file(filename, mode):
    file = open(filename, mode, encoding="utf8")
    file.seek(0)
    return file

try:
    counter_file = open_file("counter.txt", "a+")
    count = counter_file.readline()
    counter_file.close()

    if len(count) == 0:
        count = 0

    count = int(count)
        
    if len(sys.argv) == 2:
        if sys.argv[1] == "inc":
            count += 1
        elif sys.argv[1] == "dec":
            count -= 1

    counter_file = open_file("counter.txt", "w")
    counter_file.write(str(count))
    counter_file.close()

    print(count)

except:
    print("Error: Corrupted file. Cleaning...")
    counter_file = open_file("counter.txt", "w")
    counter_file.write("0")
    counter_file.close()
    print("File cleaned")
