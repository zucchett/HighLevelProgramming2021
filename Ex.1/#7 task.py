x = list(range(1, 11))

def cube_list_loop(*args):
    for i in range(1, 10):
        x[i] = x[i]**3
    return x

def cube_list_comprehension(*args):
    num_list = [num**3 for num in x]
    return x

print(cube_list_loop())
print(cube_list_comprehension())