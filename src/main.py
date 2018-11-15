from src import FileHandler
from src.Iterator import Iterator
from src.PerfNum import isPerfect

print("IMPORTANTE: EL ARCHIVO DEBE TENER UN SOLO NUMERO ENTERO POR CADA LINEA")
print("Introduce la ruta del archivo: ")
path = input()
data = FileHandler.fileToArray(path)
myiterator = iter(data)
sum = 0
generator = Iterator(data)
for index in generator:
    sum = 0
    for anIndex in index:
        sum = sum + anIndex
    if isPerfect(sum):
        print("La combinacion de las posiciones: " + str(index) + " genera el numero perfecto: " + str(sum))
    else:
        pass
print("Ejecucion terminada")