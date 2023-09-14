# Odd Even Prime

print('Shall We begin? ')
Start_Request = str(input('Type Yes to start and No to quit: '))
Result = []

def Odd(Start, End):
    for i in range(Start, End):
        if i % 2 == 1:
            Result.append(i)
    return Result

def Even(Start, End):
    for i in range(Start, End):
        if i % 2 == 0:
            Result.append(i)
    return Result

def Prime(Start, End):
    for i in range(Start, End):
        if i > 1:
            for j in range(2, i):
                if i % j == 0:
                    break
            else:
                Result.append(i)
    return Result

def Check():
    if Start_Request == 'Yes':
        Start = int(input('Enter starting point: '))
        End = int(input('Enter final point: '))
        End += 1
        print('Available sets are: Odd, Even, Prime')
        User_set = str(input('Which set do you want: '))
        
        if User_set == 'Odd':
            print('Odd numbers are: ')
            Odd(Start, End)
            
        elif User_set == 'Even':
            print('Even numbers are: ')
            Even(Start, End)
            
        elif User_set == 'Prime':
            print('Prime numbers are: ')
            Prime(Start, End)
        
        else: 
            print("Unavailable set")
        
        print('Shall the program continue? ')
        Continue_Request = str(input('Type Yes to continue and No to quit: '))
        if Continue_Request == 'Yes':
            Check()
        elif Continue_Request == 'No':
            pass
    elif Start_Request == 'No':
        pass


Check()
