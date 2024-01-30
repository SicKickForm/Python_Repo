# Nested if-else/elif statement
Num = int(input('Enter a number:'))
if Num == 0:
    pass
elif Num != 0:
    if Num > 0:
        print('Positive')
    else:
        print('Negative')

# Short-hand Nested if_else/elif statement
print('Positive') if Num > 0 else print('Negative') if Num < 0 else print('0')

# ------------------------------------------------------------------------------- #

# Nested while statement
while Num == 0:
    continue
else:
    while Num > 0:
        print('Positive')
        break
    else:
        print('Negative')
del Num

# ------------------------------------------------------------------------------- #

# Nested for statement
i = 1
for Friends in ['SicKickForm', 'Dia', 'akaTeen']:
    for Consumables in ('Food', 'Dessert', 'Drink'):
        for Menu in {'Heavy', 'Medium', 'Light'}:
            print(i, Friends, Consumables, Menu)
            i += 1
else:
    print(str(i) + ' Home')
del Friends, Consumables, Menu

# ------------------------------------------------------------------------------- #

# iteration (iterable and iterator)
# You can Use iteration with iter() and next() commands
Names = ('SicKickForm', 'Dia', 'akaTeen', 'Siren')
Community = iter(Names)
for i in Names:
    print(next(Community))
del Names, Community

# ------------------------------------------------------------------------------- #

# Generators
# Generators can iterate through iterators without saving them in memory
# Generators usually include functions and loops
# Use yield statement instead of storing the values and returning them
# You can convert generator results into lists to display them


def Countdown(Max):
    for i in range(Max):
        yield(i)


print(Countdown(10))
print(list(Countdown(10)))
# List comprehensions can also be a genrator
print(i for i in range(10))
print(list(i for i in range(10)))

# ------------------------------------------------------------------------------- #
