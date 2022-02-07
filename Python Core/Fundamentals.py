# Message output
print('Ready?')
# Use \n to move cursor to the next line
print('Three!\nTwo!\nOne!\nGo')
print('\110\145\154\154\157' + ' ' + '\x57\x6f\x72\x6c\x64')
# You can use ''' to write multi-line messages or comments (Docstrings)
print('''I\'m SicKickForm\t\bOfHumanKind
And this is My message output file''')
print('So that ' + 'I can take some quick looks ' + "in future")
print("Again" + (' and again') * 2)
# Use \r to move cursor to start of the line
print('''The Enter key follows the \\r\\n command in windows systems and
\\n command in linux or unix systems.''')

# Membership operators
Name = 'SicKickForm'
'SicKick' in Name
'Human' not in Name
del Name

# Arithmetic operators
A = 10
B = 2
A + B
# 10 + 2 = 12
A - B
# 10 - 2 = 8
A * B
# 10 * 2 = 20
A / B
# 10 / 2 = 5.0
A ** B
# 10 ** 2 = 100
print(A // B)
# 10 // 2 = 5
print(A % B)
# 10 % 2 = 0.00

# Quick Arithmetic operators
A += B
# A = A + B
A -= B
# A = A - B
A *= B
# A = A * B
A /= B
# A = A / B
A **= B
pow(A, B)
# A = A ** B
A //= B
# A = A // B
A %= B
# A = A % B
A = abs(A)
# A = |A|
# Returns the greatest number
max(A, B)
# Returns the least number
min(A, B)
# Returns the closest integer to number
round(A)
del A, B


# Bit wise operators
# You can use quick bit wise operators too
# Returns the bits that exist in X and Y as a number
X = 8
Y = 3
X & Y
# 00001000 & 00000011 = 00000000 = 0
# Returns the bits that exist in X or Y as a number
X | Y
# 00001000 | 00000011 = 00001011 = 11
# # Returns the bits that exist in X or Y not in X and Y as a number
X ^ Y
# 00001000 ^ 00000011 = 00001011 = 11
# Inverts all the bits
~X
# ~00001000 = 11110111 = -9

# Compersion operators
X == 8
Y != 4
X > Y
Y < X
X >= Y
Y <= X

# Logical operators
Y <= X and X > Y
Y != 4 or Y == 3
not X != 8

# Identity operators
X is 8
Y is not 4
del X, Y
