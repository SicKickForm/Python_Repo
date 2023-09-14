# Assign default variables after non-default variables
# Functions that don't access anything external are called pure functions
# Functional programming is using only pure functions


def Introduce(Age1, Age2, Age3, Name='SicKickForm'):
    print(Name + ' is ' + str(Age2))


Introduce(Age1=19, Age2=18, Age3=17)

# ------------------------------------------------------------------------------- #

# Use * to import values form the tuple using their index


def Introduce2(*Name):
    print(Name[2] + ' is 17')


Introduce2('Siren', 'SicKickForm', 'Dia', 'akaTeen', 'FarmerJohn', 'Jimmie')

# ------------------------------------------------------------------------------- #

# You can also import values from a variable while calling the function


def Introduce3(Name):
    print(Name[5] + ' is 21')


Members = 'Siren', 'SicKickForm', 'Dia', 'akaTeen', 'FarmerJohn', 'Jimmie'
Introduce3(Members)

# ------------------------------------------------------------------------------- #

# Use ** to import values from the dictionary using their index


def Introduce4(**Info):
    print(Info['Name'] + ' is ' + str(Info['Age']))


Introduce4(Name='FarmerJohn', Age=23)

# ------------------------------------------------------------------------------- #

# Use return command to assign values to function output
# Using return command stops function execution


def Introduce5(Name, Age):
    return(Name + ' is ' + str(Age))
    print('You won\'t see this')


print(Introduce5('Siren', 20))

# ------------------------------------------------------------------------------- #

# functions Recursion


def Introduce6(Func, Name, Age):
    print(Func(Name, Age))


Introduce6(Introduce5, 'akaTeen', 22)

# ------------------------------------------------------------------------------- #

def Fibo(i):
    if(i > 0):
        result = i + Fibo(i - 1)
        print(result)
    else:
        result = 0
    return result


Fibo(6)

# ------------------------------------------------------------------------------- #

# Use pass command to skip an empty function


def Empty():
    pass


Empty()

# ------------------------------------------------------------------------------- #

# Use a list to return multiple arguments


def Operations(X, Y):
    return[X + Y, X - Y, X * Y, X / Y]


print(Operations(8, 2)[0])
print(Operations(8, 2)[1])
print(Operations(8, 2)[2])
print(Operations(8, 2)[3])
print(Operations(8, 2))

# ------------------------------------------------------------------------------- #

# Use lambda as an anonymous function inside the main function
# lambda function takes only one expression


print((lambda X: X**5 / 5)(3))

def Anonymous(Lambda_Func, Num):
    return Lambda_Func(Num)


print(Anonymous(lambda X: X**3, 5))

# ------------------------------------------------------------------------------- #

# Use map function to iterate through iterable elements and apply a function


def MAP(X):
    return X ** 2


Nums = range(11)
print(list(map(MAP, Nums)))

# ------------------------------------------------------------------------------- #

# Use filter function to iterate through iterable elements and remove the odd ones
# Use a function with a boolean value to check if elements fit the predicate


print(list(filter(lambda X: X < 6, Nums)))

# ------------------------------------------------------------------------------- #

# Decoration
# Decorator is an inner function that can be returned
# Decorator function is imported inside main function as an argument
# Use @ statement to decorate the main function with it's inner function


def DecoMain(Deco):
    def DecoFunc():
        print('This is a decoration test')
        Deco()
        print('Nice')
    return DecoFunc()


@DecoMain
def Deco():
    print('It works')

# ------------------------------------------------------------------------------- #

# Recursion
# Recursion is calling a function inside itself
# Recursion can also be two different functions calling eachother
# You need to create a base case to break the recursion process
# Recursion can be infinite without a base case break


def RecEven(Num):
    if Num % 2 == 0:
        print('Even')
    else:
        RecOdd(Num)


def RecOdd(A):
    if A % 2 == 1:
        print('Odd')
    else:
        A = round(A)
        RecEven(A)


RecEven(12.6)

# ------------------------------------------------------------------------------- #

# Function polymorphism
# Polymorphism refers to functions that work differently on various objects
print(len("ABCD"))
print(len([1, 2, 3, 4]))

del (Introduce, Introduce2, Introduce3, Introduce4, Introduce5, Introduce6, 
    Fibo, Empty, Operations, Anonymous, MAP, DecoMain, RecEven, RecOdd )
