# Message output
print('Ready?')
# Use \n to move cursor to the next line
print('Three!\nTwo!\nOne!\nGo')
# You can use ''' to write multi-line messages or comments (Docstrings)
print('''Hello\tWorld!
I'm SicKickFormOFHumanKind
And this is My message output file''')
print('So that ' + 'I can take some quick looks ' + "in future")
print("Again" + (' and again') * 2)
# Use \r to move cursor to start of the line
print('''The Enter key follows the \\r\\n command in windows systems and
\\n command in linux or unix systems.''')

# Message output methods
Age = 18
Term = 12.5
Project = 'programming'
Major = 'Computer-Science '
# Insert variables into the message
Info = ('I\'m {} and I\'ve passed {} percent of {} project in {}.')
print(Info.format(str(Age), str(Term), Project.capitalize(), Major.strip()))
Major.replace('c', 'C')
for X in Major.upper():
    print((X + " ") * 2)
[print(X) for X in Major.upper() * 2]
for X in Project:
    for Y in range(2):
        print(X, Y)
Sub_Title = Project + ' language'
print(Sub_Title.split(' '))
Options = (', '.join(('A' "B" 'C' "D")))
print(Options)
del (Age, Term, Project, Major, Info, Sub_Title, Options)

# Simple mathematical operators
A = ((5 - 2) * (12 / (16 % 6)) + (2 ** (9 // (16 ** (1/2)))))
# ((3) * (12 / (4)) + (2 ** (9 // (4.0)))
# ((3 * (3.0)) + (2 ** (2.0)))
# ((9.0) + (4.0))
# (13.0)

# Quick mathematical operators
A += 2
# A = A + 2 = 15.0
A -= 3.0
# A = A - 3.0 = 12.0
A *= -2
# A = A * -2 = -24.0
A /= -8.0
# A = A / -8.0 = 3.0
A **= 4/2
A = pow(A, 2.0)
# A = A ** 2.0 = 9.0
A //= (8 % 3)
# A = A // 2.0 = 4.0
A %= 2 * (2.25 ** (1/2))
# A = A % 2 * (1.5) = A % 3.0 = 1.0
A = abs(A)
# A = |A| = +1.0
A = max(A, 2)
# A = 2
A = min(A, 2)
# A = 1.0
A = round(A)
# A = 1
del A
