# Any statement followed by a () is a function
# Defining function
# You can assign variables when calling function to choose from
# Assign default variables after non-default variables
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
# Use global command to change or create a global variable inside function
# Global variables can be used in functions but not contrariwise
# Use list to return multiple arguments
Sign = '----'


def Func9(X, Y):
    global Sign
    Sign = '++++'
    print(Sign)
    return[X + Y, X - Y, X * Y, X / Y]


print(Func9(8, 2)[0])
print(Func9(8, 2)[1])
print(Func9(8, 2)[2])
print(Func9(8, 2)[3])
print(Func9(8, 2))
