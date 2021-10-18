def square(a):
    a = a**2
    return a

def cube(a):
    a = a**3
    return a

def sixth_power(a):
    a = cube(square(a))
    return a

print(sixth_power(2))