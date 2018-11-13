from Node import Node


class Iterator(object):
    front = Node()
    aux = Node()
    rear = Node()

    def __init__(self, lista):
        self.front = None
        self.aux = None
        self.rear = None
        for e in lista:
            self.insert(e)

    def __iter__(self,l):
        self.__init__(l)
        return self

    def insert(self, num):
        if self.rear is None:
            self.rear = Node()
            self.front = self.rear
        else:
            self.rear.nextNode = Node()
            self.rear = self.rear.nextNode
            self.aux = self.front.nextNode
        self.rear.info = num

    def __next__(self):
        pos = [self.front.info, self.aux.info]
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
        return pos
