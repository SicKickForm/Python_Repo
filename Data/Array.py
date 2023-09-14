# Casting list (Ordered, Indexed, Changeable, Duplicatable)
# Use lists if you have a collection of data that does not need random access
Community_Partners = ['Vandal', 'Saboteur', 'Muse']
Community_Partners[1:2] = ['Siren', 'Brute', 'Prowler']
print(Community_Partners)
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
# Showing the highest element in list
print(max(Community_Partners))
# Showing the lowest element in list
print(min(Community_Partners))
Community_Partners.remove('Vandal')
Community_Partners.pop(1)
Community_Partners.append('Muse')
Community_Partners.insert(0, 'Vandal')
print(Community_Partners)
Community_Partners.clear()
Community_Partners.extend(Info)
print(Community_Partners)
# Sorting the elements from the lowest to the highest
Community_Partners.sort()
print(Community_Partners)
# Use the key command to sort list based on an assignment or function
Community_Partners.sort(key=str.upper)
print(Community_Partners)
# Sorting the elements from the highest to the lowest
Community_Partners.sort(reverse=True)
print(Community_Partners)
# Reverses all list element positions
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
# List comprehension
Cubes = [i**2 for i in range(11)]
print(Cubes)
del (Community_Partners, Dog, Snake, Charming, Info, Friends, Cubes)

# ------------------------------------------------------------------------------- #

# Creating tuple (Ordered, Indexed, Unchangeable, Duplicatable)
# Use tuples when your data should not change
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

# ------------------------------------------------------------------------------- #

# Creating set (Unordered, Unindexed, Unchangeable, Unduplicatable)
# Use a set if you need uniqueness for the elements
Members = {'SicKickForm', 'Dia'}
Age = set((18, 17, 20))
Newbie = {'akaTeen', 22}
# Set methods
Members.add('Siren')
Members.update(Age)
# A ∪ B
print(Members | Newbie)
print(Members)
Members = Members.union(Newbie)
print(len(Members))
print(Members)
Members.remove('Siren')
Members.discard(20)
Missing = Members.pop()
print(Members)
print(Missing)
Crewmates = Members.copy()
# A ∩ B = ∅
print(Crewmates.isdisjoint(Newbie))
# B ⊆ A
print(Crewmates.issuperset(Newbie))
# A ⊆ B
print(Crewmates.issubset(Members))
# A ∩ B
print(Members & Newbie)
Similarity = Members.intersection(Newbie)
print(Similarity)
# (A - B) ∩ (B - A)
print(Members ^ Newbie)
Difference = Members.symmetric_difference(Newbie)
print(Difference)
# A - B
print(Members - Newbie)
print(Newbie - Members)
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

# ------------------------------------------------------------------------------- #

# Creating dictionary (Ordered, Unindexed, Changeable, Unduplicatable)
# Use a dictionary when you need a logical association between keys and values
# Use a dictionary when you need fast lookup for your data based on the key
Members = {
    'Names': ('SicKickForm', 'Dia', 'Siren'),
    'Age': (18, 17, 20)}
Members['Crewmates'] = (('Vandal', 'Saboteur', 'Muse'))
print(Members)
print(Members['Names'])
print(Members['Names'][1])
# Nested dictionary
# You can also use post-written dicts as an object in a new dict
# You can only use unchangeable objects as keys in dict
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
print(Members.get('Member4', 'Not Available'))
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

# ------------------------------------------------------------------------------- #
