# if_else/elif statement
PW = 'A1234b5678'
Password_1 = input('Enter Your password:')
if Password_1 == PW:
    print('Access Granted, Welcome.')
else:
    print('Access Denied, Try Again.')
    Password_2 = input('Enter Your password again:')
    if Password_2 == PW:
        print('Access Granted, Welcome.')
    else:
        print('Access Denied, Try Again.')
        Password_3 = input('Enter Your password again:')
        if Password_3 == PW:
            print('Access Granted, Welcome.')
        elif Password_3 != PW:
            print('Access Denied, Try Again later.')

# While statement
i = 0
if i == 0:
    print('Start')
    while i < 10:
        i += 1
        print(i)
        if i == 3 or i == 6 or i == 9:
            continue
        while i == 10:
            print('End')
            i += 1
            while i > 10:
                break

# For statement
i = 0
PW = 'A1234B5678'
Password_I = input('Enter Your password:')
for Character in PW:
    if Password_I[i] == list(Character):
        i += 1
        if i == 11:
            print('Access Granted, Welcome.')
    elif Password_I[i] != Character[i]:
        i = 12
        if i == 12:
            print('Access Denied, Try Again later.')
            break
