from src import FileHandler
from src.Iterator import Iterator
from src.PerfNum import isPerfect
import time

print("IMPORTANTE: EL ARCHIVO DEBE TENER UN SOLO NUMERO ENTERO POR CADA LINEA")
print("Introduce la ruta del archivo: ")
path = input()
start_time = time.time()
list = FileHandler.fileToArray(path)
myiterator = iter(list)
sum = 0
generator = Iterator(list)
for index in generator:
    sum = list[index[0]]+ list[index[1]]
    if isPerfect(sum):
        print("La combinacion de las posiciones: " + str(index) + " genera el numero perfecto: " + str(sum))
    else:
        pass
print("Ejecucion terminada en", time.time() - start_time, "ns")