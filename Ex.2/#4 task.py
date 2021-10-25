def recur_factorial(n):
   if n == 1:
       return n
   else:
       return n*recur_factorial(n-1)

def none_recur_factorial(n):
    factorial = 1
    if n == 1:
        return n
    else:
        for i in range(1, n+1):
            factorial = factorial * i
        return factorial

num = 7

if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   print("The factorial of", num, "is", recur_factorial(num))

if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   print("The factorial of", num, "is", none_recur_factorial(num))