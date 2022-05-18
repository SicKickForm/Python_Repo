# Nested if-else/elif statement
Num = int(input('Enter a number:'))
if Num == 0:
    pass
elif Num != 0:
    if Num > 0:
        print('Positive')
    else:
        print('Negative')
# Short hand Nested if_else/elif statement
print('Positive') if Num > 0 else print('Negative') if Num < 0 else print('0')

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

# Assertion
# Use assert command to execute a sanity-check inside code
Age = int(input('Enter Your age:'))
assert Age > 6, 'Under-Age'
print('G Check')
assert Age > 10, 'Under-Age'
print('PG Check')
assert Age > 13, 'Under-Age'
print('PG-13 Check')
assert Age > 17, 'Under-Age'
print('R and NC-17 Check')

# Try except statement
# The try block lets You test a block of code for errors
# The except block lets You ignore the error for now
# The else block is executed when there is no error
# The finally block is executed regardless of the result of try-except blocks
try:
    Age > 18
except ValueError:
    print('Enter Your age again')
except:
    print('You are not qualified')
else:
    print('You are qualified')
finally:
    print('The test is over')
# Use raise command to create an exception with message inside code
if Age < 18:
    raise Exception('You are not qualified')
else:
    print('You are qualified')
del Age

# All any enumerate statements
# All statement is True if all iterable members have the condition
# Any statement is True if atleast one iterable member has the condition
# Enumerate statement iterates through iterable members with their index
Ages = [17, 14, 13, 22]
if all(i < 18 for i in Ages):
    print('Not qualified')
if any(i > 18 for i in Ages):
    print('Qualified')
for i in enumerate(Ages):
    print(i)
del Ages
