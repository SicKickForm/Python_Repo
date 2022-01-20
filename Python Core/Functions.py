import datetime

# Any statement followed by a () is a function
# Defining function
# Use return command to assign a value to function's statement
# Using return command stops function execution


def Func1(Name='Siren', Age=20):
    return(Name + ' is ' + str(Age) + ' years old')
    print('You won\'t see this')


print(Func1())
print(Func1('SicKickForm', 18))
# Combining functions


def Func1_2(Func, Name, Age):
    print(Func(Name, Age))


Func1_2(Func1, 'Dia', 17)
del (Func1, Func1_2)
# Defining index based function


def Func2(*Name):
    print(Name[3] + ' is 22 years old')


Func2('Siren', 'SicKickForm', 'Dia', 'akaTeen')
del Func2
# Use list to return multiple arguments


def Func3(X, Y):
    return[X + Y, X - Y, X * Y, X / Y]


print(Func3(8, 2)[0])
print(Func3(8, 2)[1])
print(Func3(8, 2)[2])
print(Func3(8, 2)[3])
del Func3

# Modules
# datetime module
print(datetime.datetime.now())
print(datetime.datetime.now().year)
print(datetime.datetime.now().strftime('%A'))
print(datetime.datetime.now().strftime('%a'))
print(datetime.datetime.now().strftime('%w'))
print(datetime.datetime.now().strftime('%d'))
print(datetime.datetime.now().strftime('%y'))
print(datetime.datetime.now().strftime('%H'))
