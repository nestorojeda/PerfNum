import PerfNum
import FileHandler
import Iterator

path = "datafile"
data = FileHandler.fileToArray(path)
myiterator = iter(data)
sum = 0
for index in myiterator:
    print(index)