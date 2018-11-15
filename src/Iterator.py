from src.Node import Node


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
                    raise StopIteration
                else:
                    self.front = self.front.nextNode
                    self.aux = self.front.nextNode
            else:
                self.aux = self.aux.nextNode
        return self.pos



