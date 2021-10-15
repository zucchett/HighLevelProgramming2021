def printHelloWorld(*args):
    mylist = []
    for i in range(1, 101):
        output = ""
        if (i % 15 == 0):
            output += "|Hello World| "
        elif (i % 3 == 0):
            output += "Hello "
        elif (i % 5 == 0):
            output += "World "
        else:
            mylist.append(i)
            print(i, end=" ")
        mylist.append(output)
        print(output, end="")
    mylist2 = [x for x in mylist if x]
    return mylist2

mytuple = printHelloWorld()

def printTubleHelloWorld(*args):
    print("\n")
    for i in range(100):
        if mytuple[i] == "|Hello World| ":
            mytuple[i] = "|Python Works|"
        elif mytuple[i] == "Hello ":
            mytuple[i] = "Python"
        elif mytuple[i] == "World ":
            mytuple[i] = "Works"
        print(mytuple[i], end=" ")
printTubleHelloWorld()