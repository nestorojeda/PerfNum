from src import FileHandler
from src.Iterator import Iterator
from src.PerfNum import isPerfect
import time
import sys


path = sys.argv[1]
n = int(sys.argv[2])
start_time = time.time()
data = FileHandler.fileToArray(path)


if n <= len(data):
    myiterator = iter(data)
    generator = Iterator(len(data), n)
    for index in generator:
        sum = 0
        for i in index:
            sum = sum + data[i]
        if isPerfect(sum):
            print("La combinacion de las posiciones: " + str(index) + " genera el numero perfecto: " + str(sum))
        else:
            pass
else:
    print("No puede haber más valores a permutar que valores en la lista")
print("Ejecución terminada")