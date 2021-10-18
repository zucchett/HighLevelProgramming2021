#!/usr/bin/env python
# coding: utf-8

# # Modules/packages/libraries
# 
# Definitions:
# 
#   * Modules:
#   A module is a file which contains python functions, global variables etc. It is nothing but .py file which has python executable code / statement.
# 
#   * Packages:
#   A package is a collection of Python modules: while a module is a single Python file, a package is a directory of Python modules containing an additional `__init__.py` file, to distinguish a package from a directory that just happens to contain a bunch of Python scripts. Packages can be nested to any depth, provided that the corresponding directories contain their own `__init__.py` file.
#   
#   * Libraries:
#   A library is a collection of various packages. There is no difference between package and python library conceptually.
#   
# Modules/packages/libraries can be easily "imported" and made functional in your python code. A set of libriaries comes with every python installation. Others can be installed locally and then imported. Your own code sitting somewhere else in your local computer can be imported too.
# 
# Further details on packages and how to create them can be found on the online Python documentation. We may find the need of creating our own during the course.

# In[1]:


# import all the "stuff" that is in the math library                        #Calling the libraries
import math
print(math.pi)

# you can give math a label for convenience
import math as m
print(m.pi)

# alternatively you can import only a given "thing" from the library
from math import pi    #you can add several libraries at once, just list them separated by a ", "
print(pi)

# or just get everything (try to avoid this if you only need specific "things")
from math import *
print(sqrt(7))


# To know which modules are there for you to use just type:

# In[2]:


import sys
for k, v in sys.modules.items():
    print(k)

# Alternative for older python versions
# print(help('modules') )


# `pip` is a special package. It is used from the command line to install properly (e.g. matching the version of the local packages) new packages. It can also be used from within python to check i.e. the set installed packages and their versions. N.B.: only the installed packages on top of the default ones will be listed 

# In[3]:


import sys

if sys.version_info >= (3, 8):
    from importlib import metadata as importlib_metadata
else:
    import importlib_metadata

dists = importlib_metadata.distributions()
for dist in dists:
    name = dist.metadata["Name"]
    version = dist.version
    print("found distribution %s version %s" % (name, version))

#import pip
#sorted(["%s==%s" % (i.key, i.version) for i in pip.get_installed_distributions()])


# # Functions

# In[4]:


def square(x):
    """Square of x."""
    #print(id(x))       # another way by using id, comment the last function.
    return x*x

def cube(x):
    """Cube of x."""
    #print(id(x))
    return x*x*x

# create a dictionary of functions
funcs = {
    'square': square,
    'cube': cube,
}

x = 3
#print(id(x))
print(square(x))
print(cube(x))

for func in sorted(funcs):
    print (func, funcs[func](x))    #calling function name(dic) with func. value


# ## Functions arguments

# What if the function tries to modify an immutable object set as default argument?

# In[5]:


def modify(x):  # x is just define in function scope
    x += 2
    return x

x = 1   #define the variable in the global scope
print(x)
print(modify(x))
print(x)                       


# Now imagine we have a list *x =[1, 2, 3]*, i.e. a mutable object. If within the function the content of *x* is directly changed (e.g. *x[0] = 999*), then *x* changes outside the funciton as well. 

# In[6]:


def modify(x):
    x[0] = 999
    return x

x = [1,2,3]
print(x)
print(modify(x))    #we dont create a new variable as the above example, but modify its value so it will change
print(x)


# However, if *x* is reassigned within the function to a new object (e.g. another list), then the copy of the name *x* now points to the new object, but *x* outside the function is unchanged.

# In[7]:


def no_modify(x):
    x = [4,5,6]
    return x

x = [1,2,3]
print(x)
print(no_modify(x))    # its seem as we have define a function scope variable, so it will not change outside the founction
print(x)


# ### Initialization of function arguments

# A Python behaviour that may not be intuitive, and you should pay attention to:

# In[10]:


def f(x = []):
    x.append(1)
    return x

print(f())
print(f())
print(f(x = [9,9,9]))
print(f())
print(f())


# What actually happens: a new list is created once when the function is defined, and the same list is used in each successive call.
# 
# Python’s default arguments are evaluated once when the function is defined, not each time the function is called (like it is in say, Ruby). This means that if you use a mutable default argument and mutate it, you will and have mutated that object for all future calls to the function as well. Check this [post](https://docs.python-guide.org/writing/gotchas/).
# 
# What you should do instead: create a new object each time the function is called, by using a default arg to signal that no argument was provided (None is often a good choice).

# In[12]:


def f(x = None):
    if x is None:
        x = []            #it's defint as empty everytime :)
    x.append(1)
    return x

print(f())
print(f())
print(f(x = [9,9,9]))
print(f())
print(f())


# ## Higher order functions
# 
# A function that uses another function as an input argument or returns a function is known as a higher-order function (HOF). The most familiar examples are `map` and `filter`.

# ### map
# 
# The map function applies a function to each member of a collection

# In[13]:


x = list(map(square, range(5))) 
print(x)

# Note the difference w.r.t python 2. In python 3 map retuns an iterator so you can do stuff like:
for i in map(square, range(5)): print(i)


# ### filter
# 
# The filter function applies a predicate to each member of a collection, retaining only those where the predicate is True

# In[14]:


def is_even(x):
    return x % 2 == 0

print(list(filter(is_even, range(5))))


# In[15]:


list(map(square, filter(is_even, range(5))))


# ### reduce
# 
# The reduce function reduces a collection using a binary operator to combine items two at a time. More often than not, reduce can be substituted with a more efficient `for` loop. It is worth mentioning it for its key role in big-data applications together with map (the map-reduce paradigm). 
# N.B.: it no longer exist as built-in function in python 3, it is now part of the `functools` library

# In[16]:


from functools import reduce

def my_add(x, y):
    print("Adding", x, "and", y)
    return x + y

# another implementation of the sum function
reduce(my_add, [1,2,3,4,5])


# ### zip
# 
# zip is useful when you need to iterate over matched elements of multiple lists

# In[18]:


xs = [1, 2, 3, 4]
ys = [10, 20, 30, 40]
zs = ['a', 'b', 'c', 'd', 'e']

for x, y, z in zip(xs, ys, zs):  # for breif iterate
    print(x, y, z)


# ### Custom HOF

# Python allows you to define custom HOF, or in general functions that accept as arguments other functions

# In[19]:


def custom_sum(xs, transform):
    """Returns the sum of xs after a user specified transform."""
    return sum(map(transform, xs))

xs = range(5)
print(custom_sum(xs, square))
print(custom_sum(xs, cube))  #calling a function within a function


# ### Returning a function

# Other than passed as arguments, functions can also be returned

# In[21]:


def make_logger(target):
    def logger(data):
        with open(target, 'a') as f:
            f.write(data + '\n')
    return logger

foo_logger = make_logger('foo.txt')    #foo.txt will be created if not there already
foo_logger('Hello')
foo_logger('World')


# In[22]:


get_ipython().system(" cat 'foo.txt'")


# ## Anonimous functions (lambda)
# 
# When using functional style, there is often the need to create specific functions that perform a limited task as input to a HOF such as map or filter. In such cases, these functions are often written as anonymous or lambda functions. 
# The syntax is as follows:
# 
# lambda *arguments* : *expression*
# 
# 
# If you find it hard to understand what a lambda function is doing, it should probably be rewritten as a regular function.

# In[23]:


sum = lambda x, y: x+y   #lambda arg. : expression
sum(3, 4)


# In[24]:


for i in map(lambda x: x*x, range(5)): print(i)


# In[25]:


# what does this function do?
from functools import reduce
s1 = reduce(lambda x, y: x + y, map(lambda x: x**2, range(1,10)))
print(s1)


# ## Recursive functions 

# In[26]:


def fib1(n):
    """Fib with recursion."""

    # base case
    if n==0 or n==1:
        return 1
    # recursive case
    else:
        return fib1(n-1) + fib1(n-2)

    
print([fib1(i) for i in range(10)])


# In[27]:


# In Python, a more efficient version that does not use recursion is

def fib2(n):
    """Fib without recursion."""
    a, b = 0, 1
    for i in range(1, n+1):
        a, b = b, a+b
    return b

print([fib2(i) for i in range(10)])


# In[28]:


# check indeed the timing:

get_ipython().run_line_magic('timeit', 'fib1(20)   # %timeit :: real tieme for the function to be excuted, so the 2nd one prefer')
get_ipython().run_line_magic('timeit', 'fib2(20)')


# ## Decorators
# 
# Decorators are a type of HOF that take a function and return a wrapped function that provides additional useful properties.
# 
# Examples:
# 
#   - logging
#   - Just-In-Time (JIT) compilation
#   - ...
#   
# Without using decorators:

# In[29]:


def my_decorator(func):  
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

def say_whee():
    print("Whee!")

say_whee = my_decorator(say_whee)


# In[30]:


say_whee()


# Python allows you to use decorators in a simpler way with the @ symbol, sometimes called the “pie” syntax

# In[31]:


def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_whee():
    print("Whee!")


# In[32]:


say_whee()


# ## Useful Modules
# 
# You may want to have a look at the content of the following modules for further usage of (HO) functions:
#   - [operator](https://docs.python.org/3/library/operator.html)
#   - [functools](https://docs.python.org/3/library/functools.html)
#   - [itertools](https://docs.python.org/3/library/itertools.html)
#   - [toolz](https://pypi.org/project/toolz/)
#   - [funcy](https://pypi.org/project/funcy/)

# ## Iterators
# 
# Iterators represent streams of values. Because only one value is consumed at a time, they use very little memory. Use of iterators is very helpful for working with data sets too large to fit into RAM.
# 
# The iterator object is initialized using the `iter()` method on iterable objects like lists, tuples, dicts, and sets. It uses the `next()` method for iteration.

# In[35]:


# Iterators can be created from sequences with the built-in function iter()
xs = [1,2,3]
x_iter = iter(xs)

print(x_iter)
print(next(x_iter))
print(next(x_iter))
print(next(x_iter))
#print(next(x_iter))   # there is no iter after the third one (it's just iterate for 3 times)


# In[36]:


# Most commonly, iterators are used (automatically) within a for loop
# which terminates when it encouters a StopIteration exception

x_iter = iter(xs)
for x in x_iter:
    print(x)


# # Classes and Objects
# 
# Old school object-oriented programming is possible and often used in python. Classes are defined similarly to standard object-oriented languages, with similar functionalities.
# 
# The main python doc [page](https://docs.python.org/3.6/tutorial/classes.html) is worth reading through.

# In[37]:


# Class definition
class Pet:
    
    # Class attributes, common for all instances of the same class
    name = None
    age = None
    
    # Class methods
    # the "constructor"
    def __init__(self, name, age):  # inizialize the elements of the class
        # Instance attributes
        self.name = name
        self.age = age
    
    # class functions take the "self" parameter!
    def set_name(self, name):
        self.name = name
    
    def get_name(self):
        return self.name
    
    # You can define methods like the two above, but it's not usually necessary because you can get/set the values directly
    
    def convert_age(self, factor):
        self.age *= factor
# End class definition

buddy = Pet("buddy", 12) # Create instance of class "Pet"
print(buddy.name, buddy.age)
buddy.age = 3
print(buddy.age)
print(buddy.get_name(), buddy.name) # Same result


# Class inheritance is present in Python too:

# In[38]:


# ineritance is straightforward
class Dog(Pet):
    
    # the following variables is "global", i.e. holds for all "Dog" objects
    species = "mammal"
    
    # functions can be redefined as usual
    def convert_age(self):
        self.age *= 7
    def set_species(self, species):
        self.species = species
        
puppy = Dog("toby", 10) # When "puppy" object is instantiated, the parent class "Pet" constructor is called
print(puppy.name)
puppy.convert_age() # Call "Dog" class method "convert_age" (and not parent's class "Pet" method, which has been overridden)
print(puppy.age)
puppy.species = "dog"
print(puppy.species)


# In[39]:


puppy2 = Dog("fido", 6)
print(puppy2.species)


# The child class attributes are not accessible by an instance of the parent class:

# In[45]:


buddy = Pet("buddy", 12)   # we cant define the instance by the parent class we just make an object of the child class
#buddy = Dog("buddy", 12)

print(buddy.species)


# In[ ]:




