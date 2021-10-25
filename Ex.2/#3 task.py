def hello(func):
    def inner(x):
        print("hello")
        return func(x)
    return inner

@hello
def square(x):
    return x*x
@hello
def cube(x):
    return x*x*x

print(square(4))
print(cube(4))