from Node import Node
import FileHandler

class Iterator:
    front = Node()
    aux = Node()
    rear = Node()

    def __init__(self, l):
        self.front = None
        self.aux = None
        self.rear = None
        for e in l:
            self.insert(e)

    def insert(self, num):
        if self.rear is None:
            self.rear = Node()
            self.front = self.rear
        else:
            self.rear.nextNode = Node()
            self.rear = self.rear.nextNode
            self.aux = self.front.nextNode
        self.rear.info = num


    def __iter__(self):
        return self


    def __next__(self):
        self.pos = [self.front.info, self.aux.info]
        if self.front.info != -1:
            if self.aux == self.rear:
                if self.front.nextNode == self.rear:
                    self.front = Node()
                    self.front.info = -1
                    self.aux = Node()
                    self.aux.info = -1
                else:
                    self.front = self.front.nextNode
                    self.aux = self.front.nextNode
            else:
                self.aux = self.aux.nextNode
        return self.pos
def isPerfect(n):
    sum1 = 0
    for i in range(1, n):
        if n % i == 0:
            sum1 = sum1 + i
    return sum1 == n



path = "datafile"
data = FileHandler.fileToArray(path)
myiterator = iter(data)
sum = 0
generator = Iterator(data)
for index in generator:
    sum = 0
    for anIndex in index:
        sum = sum + anIndex
    if isPerfect(sum):
        print("Hallado el numero perfecto")
        print(sum)
        print("Sumando las posiciones:")
        print(index)
    else:
        pass