# Any statement followed by a () is a function
# You can assign variables when calling function to choose from
# Assign default variables after non-default variables
# Functions that don't access anything outside them are called pure functions
# Functional programming is using only pure functions
def Func1(Age1, Age2, Age3, Name='SicKickForm'):
    print(Name + ' is ' + str(Age2))


Func1(Age1=19, Age2=18, Age3=17)
# Use * to get values form the given tuple using their index


def Func2(*Name):
    print(Name[2] + ' is 17')


Func2('Siren', 'SicKickForm', 'Dia', 'akaTeen', 'FarmerJohn', 'Jimmie')
# You can also call a function using a variable


def Func3(Name):
    print(Name[5] + ' is 21')


Members = 'Siren', 'SicKickForm', 'Dia', 'akaTeen', 'FarmerJohn', 'Jimmie'
Func3(Members)
# Use ** to get values from the given dictionary using their index


def Func4(**Info):
    print(Info['Name'] + ' is ' + str(Info['Age']))


Func4(Name='FarmerJohn', Age=23)
# Use return command to assign values to functions
# Using return command stops function execution


def Func5(Name, Age):
    return(Name + ' is ' + str(Age))
    print('You won\'t see this')


print(Func5('Siren', 20))
# functions Recursion


def Func6(Func, Name, Age):
    print(Func(Name, Age))


Func6(Func5, 'akaTeen', 22)


def Func7(i):
    if(i > 0):
        result = i + Func7(i - 1)
        print(result)
    else:
        result = 0
    return result


Func7(6)
# Use pass command to ignore an empty function


def Func8():
    pass


Func8()
# Use list to return multiple arguments


def Func9(X, Y):
    return[X + Y, X - Y, X * Y, X / Y]


print(Func9(8, 2)[0])
print(Func9(8, 2)[1])
print(Func9(8, 2)[2])
print(Func9(8, 2)[3])
print(Func9(8, 2))
# Use lambda function as an anonymous function inside another
# lambda function takes only one expression


def Func10(Lambda_Func10, N):
    return Lambda_Func10(N)


print(Func10(lambda X: X**3, 5))

print((lambda X: X**5 / 5)(3))

# Use map function to iterate through iterable elements and apply a function


def Func11(X):
    return X ** 2


Nums = range(10)
print(list(map(Func11, Nums)))

# Use filter function to iterate through iterable elements and remove odd ones
# Use a function with a boolean value to check if element fit the predicate
print(list(filter(lambda X: X < 6, Nums)))

# Decoration
# Decorator is a function that:
# Includes an inner function and returns it
# Takes another function as its argument
# Use @ statement to decorate the decorator function with it's argument function


def Func12(A):
    def Func12_2():
        print('This is a decoration test')
        A()
        print('Nice')
    return Func12_2()


@Func12
def Func12_3():
    print('It works')

# Recursion
# Recursion is calling a function inside itself
# Recursion can also be two different functions calling eachother
# Recursion can be infinite without a base case
# You might need to create a base case to use at the end of recursion process


def Func13(A):
    if A % 2 == 0:
        print('Even')
    else:
        Func13_2(A)


def Func13_2(A):
    if A % 2 == 1:
        print('Odd')
    else:
        A = round(A)
        Func13(A)


Func13(12.6)

del (Func1, Func2, Members, Func3, Func4, Func5, Func6, Func7, Func8, Func9,
     Func10, Func11, Nums, Func12, Func12_3, Func13, Func13_2)
