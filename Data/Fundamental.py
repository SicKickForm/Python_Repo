# String multi-assignment (Pascal case)
UserName = Name = 'SicKickFormOfHumanKind'
# String methods
print(Name.ljust(36))
print(Name.center(36))
print(Name.rjust(36))
print(' '.join(Name))
print(Name.capitalize())
print(Name.title())
print(Name.upper())
print(Name.casefold())
print(Name.lower())
print(Name.swapcase())
print(Name.zfill(36))
print(Name.strip())
print(Name.lstrip())
print(Name.rstrip())
print(Name.split('Of'))
print(Name.rsplit('Of'))
print(Name.partition('Of'))
print(Name.rpartition('Of'))
print(Name.count('c'))
print(Name.find('F'))
print(Name.rfind('i'))
print(Name.index('F'))
print(Name.rindex('i'))
print(Name.islower())
print(Name.isupper())
print(Name.istitle())
print(Name.startswith('S'))
print(Name.endswith('d'))
print(Name.isalpha())
print(Name.isdecimal())
print(Name.isdigit())
print(Name.isnumeric())
print(Name.isspace())
print(Name.isidentifier())
print(Name.isprintable())

# ------------------------------------------------------------------------------- #

TeamMate = 'Stå\tlin'
# Encoding complex string with default UTF-8 encoder
print(TeamMate.encode())
print(TeamMate.expandtabs(1))
Translate = TeamMate.maketrans('å', 'a')
print(TeamMate.translate(Translate))
# You can use dictionaries instead of maketrans command
Translate = {'å': 'a'}
print(TeamMate.translate(Translate))
print(TeamMate.replace('å', 'a'))
print(TeamMate.isalnum())

# ------------------------------------------------------------------------------- #

# Insert values into the string using format command
# Use format_map(dict) command to insert multiple values from a dictionary
Age = 18
print(f'His name is {Name} and He is {Age}')
# Use :.2f command to convert number into a two-digit float
Info = '{} is {:.2f} years old'
print(Info.format(Name, 18))
# You can use index numbers to verify the values placement
Info = '{0} is {1} years old'
print(Info.format(Name, 18).splitlines())
del UserName, Name, TeamMate, Translate, Age, Info

# ------------------------------------------------------------------------------- #

# Crafting integer (Snake case)
Wasted_Years = 20
del Wasted_Years

# ------------------------------------------------------------------------------- #

# Casting float (Camel case)
termsPassed = float(12e4)
del termsPassed

# ------------------------------------------------------------------------------- #

# Casting complex
Class_Number = -2+1j

# ------------------------------------------------------------------------------- #

# Casting None
Money = None

# ------------------------------------------------------------------------------- #

# Showing variable datatype
print(type(Class_Number))

# ------------------------------------------------------------------------------- #

# Deleting variable
del Class_Number

# ------------------------------------------------------------------------------- #

# Creating Boolean comparison
# True (1)
7 == 7.0
10 <= 10
# One-by-one alphabetical comparison (M > E)
'Money' >= 'Education'
# False (0)
11 != 11
66 > 75
# One-by-one alphabetical comparison (H > G)
'Hello' == "GoodBye"
bool('')
bool(0)
bool(None)
bool(())
bool({})
bool([])
# Boolean methods
print(isinstance(2, int))

# ------------------------------------------------------------------------------- #

# Creating range
Digits = range(0, 10)
print(Digits[0])
print(Digits[9])
# range slicing
print([i for i in Digits[0:5]])
print([i for i in Digits[5:]])
print([i for i in Digits[:3]])
print([i for i in Digits[-7:-4]])
print([i for i in Digits[6:10:1]])
print([i for i in Digits[0::2]])
print([i for i in Digits[1::2]])
print([i for i in Digits[::-1]])
del Digits

# ------------------------------------------------------------------------------- #