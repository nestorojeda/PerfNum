class PerfNum:
    def isPerfect(n):
        sum1 = 0
        for i in range(1, n):
            if n % i == 0:
                sum1 = sum1 + i
        return sum1 == n
