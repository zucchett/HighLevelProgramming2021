#!/usr/bin/env python
# coding: utf-8

# 1. The HelloWorld replacement
# 
# a) Write a program that prints the numbers from 1 to 100. But for multiples of three print "Hello" instead of the number and for the multiples of five print "World". For numbers which are multiples of both three and five print "HelloWorld".
# 
# b) Put the result in a tuple and substitute "Hello" with "Python" and "World" with "Works".

# In[9]:


for i in range(1,101):
    
    if i%3 == 0 and i%5== 0 :
        print ('HelloWorld')
    elif i%3 == 0:
        print('Hello')
    elif i%5 == 0: 
        print ('World')
   
    elif i%3 !=0 and i%5 !=0:
         print(i)


# 2\. The swap function
# 
# Write a function that swap the values of two input variables x and y (whatever the type). Try to do that also without a temporary variable

# In[19]:


def swap(x,y):
    print(y,x)
    
swap(3,5)  


def swap1(x,y):
    S=[]
    
    S.append(x)
    S.append(y)
    
    x = S[1]
    y = S[0]
    print(x,y)
    
swap1(6,7)    


# 3\. Computing the distance
# 
# Write a function that calculates and returns the euclidean distance between two points *u* and *v*, where *u* and *v* are both 2-tuples *(x,y)*. For example, if *u=(3,0)* and *v=(0,4)*, the function should return 5

# In[31]:


def distance(x1,y1,x2,y2):

    u=(x1,y1)
    v=(x2,y2)
    
    d= pow((pow(x2-x1,2) + pow(y2-y1,2)),0.5)
    print('The calculated distance is ',d)
    

    

distance(3,0,0,4)   


# 4\. Counting letters
# 
# Write a program to calculate the number of times each character occurs in a given string *s*. Ignore differences in capitalization

# In[41]:


st = 'Esraa Alnajjar'
st = st.lower()

s=[]
s.append(st[0])

for i in range (len(st)):
    if st[i] not in s:
        s.append(st[i])

for i in range (len(s)):
    c=st.count(s[i])
    print (s[i], c)
    


# In[2]:


s = "Write a program that prints the numbers from 1 to 100. But for multiples of three print Hello instead of the number and for the multiples of five print World. For numbers which are multiples of both three and five print HelloWorld."


# 5\. Isolating the unique
# 
# Write a function that determines and count the unique numbers in the list:

# In[80]:


def isolute(list):
   
    c= 0
    uni-num=[]
    uni-num.append(list[0])    
    l=[]
    
    for i in range(len(list)):
         if list(i) not in uni-num:
                uni-num.append(list[i])
    for i in range (len(uni-num)):
         if list.count(uni-num) == 1:
             c = c+1
             l.append(uni-num[i])
         
    print("No. of unique numbers is",c)
    return (l)
         
isolute([36, 45, 58, 3, 74, 96, 64, 45, 31, 10, 24, 19, 33, 86, 99, 18, 63, 70, 85,
 85, 63, 47, 56, 42, 70, 84, 88, 55, 20, 54, 8, 56, 51, 79, 81, 57, 37, 91,
 1, 84, 84, 36, 66, 9, 89, 50, 42, 91, 50, 95, 90, 98, 39, 16, 82, 31, 92, 41,
 45, 30, 66, 70, 34, 85, 94, 5, 3, 36, 72, 91, 84, 34, 87, 75, 53, 51, 20, 89, 51, 20])         
      
         


# In[5]:


l = [36, 45, 58, 3, 74, 96, 64, 45, 31, 10, 24, 19, 33, 86, 99, 18, 63, 70, 85,
 85, 63, 47, 56, 42, 70, 84, 88, 55, 20, 54, 8, 56, 51, 79, 81, 57, 37, 91,
 1, 84, 84, 36, 66, 9, 89, 50, 42, 91, 50, 95, 90, 98, 39, 16, 82, 31, 92, 41,
 45, 30, 66, 70, 34, 85, 94, 5, 3, 36, 72, 91, 84, 34, 87, 75, 53, 51, 20, 89, 51, 20]


# Do the same without using user-defined functions, but exploiting only the Python data structures.

# 6\. Combination of functions
# 
# Write two functions - one that returns the square of a number, and one that returns the cube. Now write a third function that returns the number raised to the 6th power using the two previous functions.

# In[63]:


def square(x):
    print (pow(x,2))
    
    
def cube(y):
    print (pow(y,3))

def sixthpower(z):
    print (square(x)*cube(y))
    
square(2)
cube(3)
sixthpower(2)


# 7\. Cubes
# 
# Create a list of the cubes of x for x in *[0, 10]* using:
# 
# a) a for loop
# 
# b) a list comprehension

# In[65]:


#a) For loop:

cub=[]

for i in range (0, 11):
    c=i**3
    cub.append(c)
    
print(cub)
    
    
#b) List comprehension :

cub=[i**3 for i in range (11)]
print(cub)


# 8\. Nested list comprehension
# 
# A Pythagorean triple is an integer solution to the Pythagorean theorem $a^2+b^2=c^2$. The first Pythagorean triple is (3,4,5). Find and put in a tuple all unique Pythagorean triples for the positive integers a, b and c less than 100.

# In[66]:


from math import gcd

c=5
L=[]

while (c<100):
    c2=c**2
    
    for i in range (3, 100):
        a2=i**2
        
        for j in range (i+1, 100):
            
            b2=j**2
            
            if (a2+b2==c2) and (gcd(i, j)==1):
                tup=(i, j, c)
                L.append(tup)
                
    c=c+1

T=tuple(L)
print (T)


# 9\. Normalization
# 
# Write a function that takes a tuple of numbers and returns it with the entries normalized to one

# In[ ]:


def func():
    
    tup = tuple(input("enter tuple: "))

    x = float(min(tup))
    y = float(max(tup))

    tip = ()

    for i in range (len(tup)):
        a = float(tup[i]-x)
        b = float(y-x)
        tip += (a/b)
        #tip=tip+tip_1

    return tip

func()


# In[ ]:




