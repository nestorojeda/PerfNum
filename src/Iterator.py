class Iterator:
    global index
    global size

    def __init__(self, size, n):
        self.size = size
        self.index = [None] * n
        for i in range(0, n):
            self.index[i] = i

    def __iter__(self):
        return self

    def __next__(self):
        res = self.index.copy() ## Se copia el estado actual de index para enviarlo una vez se modifique
        ##En caso de que el elemento más significativo haya llegado a su última posición, no quedan iteraciones posibles
        if self.index[0] == (self.size - len(self.index)):
            raise StopIteration
        else:
            for i in range((len(self.index) - 1), -1, -1):
                ##Busca el primer elemento en la posición menos significativa que no ha llegado a su máximo valor,
                ##lo aumenta en una unidad y cambia los elementos del array menos significativos que él
                if self.index[i] < (self.size - len(self.index)):
                    self.index[i] = self.index[i] + 1
                    for j in range((i + 1), len(self.index)):
                        self.index[j] = self.index[j - 1] + 1
                    break
        return res
