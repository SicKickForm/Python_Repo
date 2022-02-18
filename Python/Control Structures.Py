# Nested if_else/elif statement
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

# Nested While statement
while Num == 0:
    continue
else:
    while Num > 0:
        print('Positive')
        break
    else:
        print('Negative')
del Num

# Nested For statement
i = 1
for Places in range(1, 4):
    for Friends in ['SicKickForm', 'Dia', 'akaTeen']:
        for Consumables in ('Food', 'Dessert', 'Drink'):
            for Menu in {'Heavy', 'Medium', 'Light'}:
                print(i, Places, Friends, Consumables, Menu)
                i += 1
else:
    print(str(i) + ' Home')
del i, Places, Friends, Consumables, Menu
