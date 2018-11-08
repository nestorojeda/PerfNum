class Combinations:
    def __init__(self, n, r):
        self.arr = [1] * int(r)
        self.init_value = 0
        self.i = -1
        self.recursion_count = 0
        self.count = 0

    def generate_combinations(self, n, r):
        self.i += 1

        if r == 0:
            yield self.arr
        else:
            if self.i != 0:
                self.init_value = self.arr[self.i - 1]

            self.arr[self.i] = self.init_value + 1

            for x in range(self.arr[self.i], int(n) + 1):
                self.arr[self.i] = x
                yield from self.generate_combinations(n, r - 1)
        self.i -= 1


def isPerfect(index):
    n = 0
    for x in index:
        n += int(data[x - 1])
    sum1 = 0
    for i in range(1, n):
        if n % i == 0:
            sum1 = sum1 + i
    if sum1 == n:
        print("Numero perfecto hallado")
        print(n)
        print("Combinando las posiciones")
        print(index)
    else:
        pass


def filetoarray(file):
    i = 0
    d = f.readlines()
    return d


f = open("datafile", "r")
data = filetoarray(f)
r = int(input('Enter r = '))
generator = Combinations(len(data), r)
generator = generator.generate_combinations(len(data), r)
try:
    while True:
        index = next(generator)
        isPerfect(index)
except StopIteration as se:
    print('Ejecución terminada')
