import math
def pyth_triple(n):
    for b in range(n):
        for a in range(1, b):
            c = math.sqrt(a * a + b * b)
            if c % 1 == 0 and (c<100):
                print(a, b, int(c))

print(pyth_triple(100))
