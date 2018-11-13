import PerfNum
import FileHandler
import Iterator

f = open("datafile", "r")
data = FileHandler.fileToArray(f)
xiter = Iterator.Iterator(data)
index = xiter.next()
sum = 0
for anIndex in index:
    sum = sum + anIndex
    if PerfNum.isPerfect(sum):
      print("La combinacion: ")
      print(index)
      print("genera el numero perfecto")
      print(sum)