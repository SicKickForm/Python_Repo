# Creating string value (Pascal case)
UserName = 'SicKickFormOfHumanKind'

# Crafting integer value (Snake case)
Average_Score = 18

# Casting float value (Camel case)
termsPassed = float(12.5)

# Showing variable datatype
print(type(UserName))

# Deleting variable
del (UserName, Average_Score, termsPassed)

# Creating Boolean comparison
# True (int(1))
7 == 7.0
10 <= 10
# One by one alphabetical comparison (M > E)
'Money' >= 'Education'
(1 == 1 and 7 == 7.0)
(1 >= 0 or 7 == 8)
(not 12 == 1.2)
# False (int(0))
11 != 11
66 > 75
# One by one alphabetical comparison (H > G)
'Hello' == "GoodBye"
(1 == 1 and -70 >= 0)
(1 == 0.1 or 5 >= (3 * 2))
(not 10 == 10.0)

# Creating list
Digits = list(range(10))
# List slices
print(Digits[3])
print(Digits[-2])
print(Digits[2:5])
print(Digits[-2:2])
print(Digits[4:])
print(Digits[:8])
print(Digits[0:10:3])
print(Digits[1::2])
print(Digits[::-1])
print(Digits * 2)
Community_Partners = [
    'Vandal',
    'Saboteur',
    'Muse']
Dog, Snake, Charming = Community_Partners
Community_Partners[1:2] = ['Siren', 'Brute', 'Prowler']
Community_Partners[1:4] = ['Saboteur']
Info = list(('SicKickForm', 18, 12.5))
Info = (Info + ['Siren', 'Prowler', 'Brute'])
# Strings are also a list
print(Info[0][3:7])
# List methods
Community_Partners.append('Siren')
Community_Partners.insert(0, 'Brute')
# Checking variable existence
print('Brute' in Community_Partners)
# Checking variable absence
print('Siren' not in Community_Partners)
print(len(Community_Partners))
print(Community_Partners.index('Vandal'))
# Showing the highest value in list
print(max(Community_Partners))
# Showing the lowest value in list
print(min(Community_Partners))
# Sorting the values from the least to the most
print(Community_Partners.sort())
# Sorting the values from the most to the least
print(Community_Partners.sort(reverse=True))
# Make a copy of the list
Friends = list(Community_Partners)
print(Friends)
Friends = Community_Partners.copy()
print(Friends)
print(Community_Partners.count('Vandal'))
Community_Partners.remove('Vandal')
print(Community_Partners.pop(0))
print(Community_Partners)
# Reverses all list values position
Community_Partners.reverse()
print(Community_Partners)
Community_Partners.extend(Info)
print(Community_Partners)
Community_Partners.clear()
print(Community_Partners)
Community_Partners = Community_Partners + Friends
print(Community_Partners)
del (Community_Partners, Dog, Snake, Charming, Digits, Info, Friends)

# User input value
UserName = str(input('What\'s Your name?'))
Age = int(input('How ald are You?'))
Final_Score = float(input('What was Your final score?'))
# Inputs without defined dataType are counted as strings
del (UserName, Age, Final_Score)

# Creating tuple
Odd_Numbers = (1, 3, 5, 7)
print(Odd_Numbers)
First, Second, Third, Fourth = Odd_Numbers
print(First)
# Tuple methods
print(len(Odd_Numbers))
print(type(Odd_Numbers))
Odd_Numbers_List = list(Odd_Numbers)
print(Odd_Numbers_List)
Odd_Numbers_List.append(9)
Odd_Numbers = tuple(Odd_Numbers_List)
print(Odd_Numbers)
print(Odd_Numbers * 2)
del (Odd_Numbers, Odd_Numbers_List)

# Creating set
Members = {'SicKickForm', 'Dia', }
print(Members)
Age = set((18, 17))
print(Age)
# Set methods
Members.add('Siren')
Age.add(20)
Members.update(Age)
print(Members)
Newbie = {'akaTeen', 22}
Members = Members.union(Newbie)
print(Members)
Missing = Members.pop()
print(Members)
print(Missing)
Members.intersection_update(Newbie)
print(Members)
Members.discard('akaTeen')
Members.discard(22)
print(Members)
Members.clear()
del (Members, Age, Missing)

# Creating dictionary
Members = {
    'Names': ('SicKickForm', 'Dia', 'Siren'),
}
print(Members)
Members['Crewmates', 'Age'] = (('SicKickForm', 'Dia', 'Siren'), (18, 17, 20))
print(Members)
print(Members['Names'])
# Dictionary methods
print(Members.get('Age'))
Members.update({'Names': ('SicKickForm', 'Dia', 'Siren', 'akaTeen')})
Members.update({'Age': (18, 17, 20, 22)})
Members.update({'Crewmates': ('SicKickForm', 'Dia', 'Siren', 'akaTeen')})
print(Members)
print(Members.keys())
print(Members.values())
print(Members.popitem())
print(Members)
del Members['Age']
print(Members)
Members.clear()
print(Members)
del Members
