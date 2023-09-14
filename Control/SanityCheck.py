# Assertion
# assert command executes a sanity-check inside code
Age = int(input('Enter Your age:'))
assert Age > 6, 'Under-Age'
print('G Check')
assert Age > 10, 'Under-Age'
print('PG Check')
assert Age > 13, 'Under-Age'
print('PG-13 Check')
assert Age > 17, 'Under-Age'
print('R and NC-17 Check')

# ------------------------------------------------------------------------------- #

# try except statement
# try block runs the program to check for errors
# except block handles the error as intended
# else block is executed when there is no error
# finally block is executed regardless of try-except blocks result
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

# exception command creates an error with output message
if Age < 18:
    raise Exception('You are not qualified')
else:
    print('You are qualified')
del Age

# ------------------------------------------------------------------------------- #

# all any enumerate statements
# all statement is True if all iterable elements meet the condition
# any statement is True if atleast one iterable element meets the condition
# enumerate statement iterates through iterable elements 
Ages = [17, 14, 13, 22]
if all(i < 18 for i in Ages):
    print('Not qualified')
if any(i > 18 for i in Ages):
    print('Qualified')
for i in enumerate(Ages):
    print(i)
del Ages

# ------------------------------------------------------------------------------- #