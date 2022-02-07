# Creating string (Pascal case)
TeamMate = 'Stå\tlin'
# Multiple variables Assignment
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
# Insert values into the string
# Use format_map(dict) command to insert multiple values from a dictionary
print(f'He is {Name}')
Info = '{} is {} years old'
print(Info.format(Name, 18))
print(Info.format(Name, 18).splitlines())
del UserName, Name, TeamMate, Translate, Info

# Crafting integer (Snake case)
Wasted_Years = 18
del Wasted_Years

# Casting float (Camel case)
termsPassed = float(12e4)
del termsPassed

# Casting complex
Class_Number = -2+1j

# Showing variable datatype
print(type(Class_Number))

# Deleting variable
del Class_Number

# Creating Boolean comparison
# True (1)
7 == 7.0
10 <= 10
# One by one alphabetical comparison (M > E)
'Money' >= 'Education'
# False (int(0))
11 != 11
66 > 75
# One by one alphabetical comparison (H > G)
'Hello' == "GoodBye"
bool('')
bool(0)
bool(None)
bool(())
bool({})
bool([])
# Boolean methods
print(isinstance(2, int))

# Creating range
Digits = range(0, 10)
print(Digits[0])
print(Digits[9])
print([i for i in Digits[0:5]])
print([i for i in Digits[5:]])
print([i for i in Digits[:3]])
print([i for i in Digits[-7:-4]])
print([i for i in Digits[6:10:1]])
print([i for i in Digits[0::2]])
print([i for i in Digits[1::2]])
print([i for i in Digits[::-1]])
del Digits

# Casting list (Ordered, Indexed, Changeable, Duplicatable)
Community_Partners = ['Vandal', 'Saboteur', 'Muse']
Community_Partners[1:2] = ['Siren', 'Brute', 'Prowler']
Community_Partners[1:4] = ['Saboteur']
print(Community_Partners)
Info = list(('Siren', 'Brute', 'Prowler'))
Info = (Community_Partners + Info)
print(Info)
# Unpacking list
Dog, Snake, Charming = Community_Partners
# Strings are also a list
print(Community_Partners[0][0:3])
# List methods
# Showing the highest value in list
print(max(Community_Partners))
# Showing the lowest value in list
print(min(Community_Partners))
Community_Partners.remove('Vandal')
Community_Partners.pop(1)
Community_Partners.append('Muse')
Community_Partners.insert(0, 'Vandal')
print(Community_Partners)
Community_Partners.clear()
Community_Partners.extend(Info)
print(Community_Partners)
# Sorting the values from the least to the most
Community_Partners.sort()
print(Community_Partners)
# Use the command key to sort it based on an assignment or function
Community_Partners.sort(key=str.upper)
print(Community_Partners)
# Sorting the values from the most to the least
Community_Partners.sort(reverse=True)
print(Community_Partners)
# Reverses all list values position
Community_Partners.reverse()
print(Community_Partners)
# Make a copy of the list
Friends = list(Community_Partners)
print(Friends)
Friends = Community_Partners.copy()
print(Friends)
print(len(Community_Partners))
print(Community_Partners.index('Vandal'))
print(Community_Partners.count('Vandal'))
# Checking variable existence
print('Brute' in Community_Partners)
# Checking variable absence
print('Siren' not in Community_Partners)
del (Community_Partners, Dog, Snake, Charming, Info, Friends)

# Creating tuple (Ordered, Indexed, Unchangeable, Duplicatable)
Odd = (1, 3, 5)
Rest = (7, 9)
Odd += Rest
print(Odd)
print(Odd[2])
# Unpacking tuple
First, Second, *Rest = Odd
print(Rest)
# Tuple methods
print(len(Odd))
print(Odd.count(5))
print(Odd.index(5))
# Convert tuple to a list to use list methods and then convert it back to tuple
Odd = list(Odd)
Odd = tuple(Odd)
del Odd, Rest, First, Second

# Creating set (Unordered, Unindexed, Unchangeable, Unduplicatable)
Members = {'SicKickForm', 'Dia'}
Age = set((18, 17, 20))
Newbie = {'akaTeen', 22}
# Set methods
Members.add('Siren')
Members.update(Age)
Members = Members.union(Newbie)
print(len(Members))
print(Members)
Members.remove('Siren')
Members.discard(20)
Missing = Members.pop()
print(Members)
print(Missing)
Crewmates = Members.copy()
print(Crewmates.isdisjoint(Newbie))
print(Crewmates.issuperset(Newbie))
print(Crewmates.issubset(Members))
Similarity = Members.intersection(Newbie)
print(Similarity)
Difference = Members.symmetric_difference(Newbie)
print(Difference)
Difference = Members.difference(Newbie)
print(Difference)
Members.symmetric_difference_update(Newbie)
print(Members)
Members.difference_update(Newbie)
print(Members)
Crewmates.intersection_update(Newbie)
print(Crewmates)
Members.clear()
del (Members, Age, Newbie, Missing,
     Crewmates, Similarity, Difference)

# Casting frozenset
Members = frozenset({'SicKickForm', 'Dia', 'Siren'})
print(Members)
print(type(Members))
del Members

# Creating dictionary (Ordered, Unindexed, Changeable, Unduplicatable)
Members = {
    'Names': ('SicKickForm', 'Dia', 'Siren'),
    'Age': (18, 17, 20)}
Members['Crewmates'] = (('Vandal', 'Saboteur', 'Muse'))
print(Members)
print(Members['Names'])
print(Members['Names'][1])
# Nested dictionary
# You can also use post-written dicts as an object in new dict
Team = {
    'Member1': {'Name': Members['Names'][0],
                'Age': Members['Age'][0]},
    'Member2': {'Name': Members['Names'][1],
                'Age2': Members['Age'][1]},
    'Member3': {'Name': Members['Names'][2],
                'Age3': Members['Age'][2]}}
print(Team['Member2']['Name'])
Status = 'Gone'
# Dictionary methods
Situation = dict.fromkeys(Team, Status)
print(Situation)
print(Members.setdefault('Team_Name', 'KKC'))
Team = Members.copy()
Team = dict(Members)
print(len(Members))
print(Members.items())
print(Members.get('Age'))
Members.update({'Crewmates': ('Vandal', 'Saboteur', 'Muse', 'Prowler')})
print(Members)
print(Members.keys())
print(Members.values())
print(Members.pop('Crewmates'))
print(Members)
del Members['Age']
print(Members)
Members.clear()
print(Members)
del Members

# casting bytes
Num1 = bytes(5)
print(type(Num1))
del Num1

# casting bytearray
Num1 = bytearray(5)
print(type(Num1))
del Num1

# Casting memoryview
Code = memoryview(bytes(5))
print(type(Code))
del Code

# User input value
UserName = str(input('What\'s Your name?'))
Age = int(input('How ald are You?'))
Final_Score = float(input('What was Your final score?'))
# Inputs without defined dataType are counted as strings
del (UserName, Age, Final_Score)
