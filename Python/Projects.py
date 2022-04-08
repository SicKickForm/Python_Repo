import datetime
import random

# Multiplication


def Multiplication(A, B):
    return A * B


Num1 = int(input('Enter 1st number: '))
Num2 = int(input('Enter 2nd number: '))
print('Multiplication is ' + str(Multiplication(Num1, Num2)))

# Calculator
print('Operations are : Addition, Subtraction, Multiplication, Division')
Operation = str(input('Select an operation: '))
Quantity = int(input('How many numbers do you enter? '))
Nums = []
for i in range(Quantity):
    Num = int(input('Enter a number: '))
    Nums.append(Num)
print('Your numbers are ' + str(Nums))


def Ops(Operation):
    if Operation == 'Addition':
        def Addition(A):
            i = 0
            for X in A:
                i += X
            return(i)
        print('Addition is ' + str(Addition(Nums)))
    if Operation == 'Subtraction':
        def Subtraction(A):
            i = Nums[0] * 2
            for X in A:
                i -= X
            return i
        print('Subtraction is ' + str(Subtraction(Nums)))
    if Operation == 'Multiplication':
        def Multiplication(A):
            i = 1
            for X in A:
                i *= X
            return(i)
        print('Multiplication is ' + str(Multiplication(Nums)))
    if Operation == 'Division':
        def Division(A):
            i = Nums[0] ** 2
            for X in A:
                i /= X
            return(i)
        print('Divison is ' + str(Division(Nums)))


Ops(Operation)

# Rock-Paper-Scissor
Rounds = int(input('How many rounds are You playing? '))
print('Modes are: Solo player, Multi player')
Mode = input('What mode are you playing? ')
i = 1
player1_points = 0
player2_points = 0
# 1- Multi player mode
if Mode == 'Multi player':
    while i <= Rounds:
        Choices = ['rock', 'paper', 'scissor']
        print('Choices are: ' + str(Choices))
        Player1 = input('Enter 1st choice: ')
        Player2 = input('Enter 2nd choice: ')
        if Player1 == 'rock':
            if Player2 == 'scissor':
                print('Player 1 won')
                player1_points += 1
                i += 1
            elif Player2 == 'paper':
                print('Player 2 won')
                player2_points += 1
                i += 1
            else:
                print('Wrong choice')
        if Player1 == 'paper':
            if Player2 == 'scissor':
                print('Player 2 won')
                player2_points += 1
                i += 1
            elif Player2 == 'rock':
                print('Player 1 won')
                player1_points += 1
                i += 1
            else:
                print('Wrong choice')
        if Player1 == 'scissor':
            if Player2 == 'rock':
                print('Player 2 won')
                player2_points += 1
                i += 1
            elif Player2 == 'paper':
                print('Player 1 won')
                player1_points += 1
                i += 1
            else:
                print('Wrong choice')
# 2- Solo player mode
elif Mode == 'Solo player':
    while i <= Rounds:
        Choices = ['rock', 'paper', 'scissor']
        print('Choices are: ' + str(Choices))
        Player1 = input('Enter Your choice: ')
        if Player1 in Choices:
            Choices.remove(Player1)
        else:
            print('Wrong Choice')
            Player1 = input('Enter Your choice again: ')
            Choices.remove(Player1)
        Player2 = random.choice(Choices)
        print('Player2 chose ' + Player2)
        if Player1 == 'rock':
            if Player2 == 'scissor':
                print('Player 1 won')
                player1_points += 1
                i += 1
            elif Player2 == 'paper':
                print('Player 2 won')
                player2_points += 1
                i += 1
        if Player1 == 'paper':
            if Player2 == 'scissor':
                print('Player 2 won')
                player2_points += 1
                i += 1
            elif Player2 == 'rock':
                print('Player 1 won')
                player1_points += 1
                i += 1
        if Player1 == 'scissor':
            if Player2 == 'rock':
                print('Player 2 won')
                player2_points += 1
                i += 1
            elif Player2 == 'paper':
                print('Player 1 won')
                player1_points += 1
                i += 1
else:
    print('Wrong mode')
# 3- Final result
print('Player1 points are ' + str(player1_points))
print('Player2 points are ' + str(player2_points))
if player1_points > player2_points:
    print('Player1 is the total winner')
elif player2_points > player1_points:
    print('Player2 is the total winner')
else:
    print('Total result is tie')

# Odd Even Prime

print(datetime.datetime.now())
print('Mohammad Reza Siyahloo')
print('Shall the program begin? ')
Start_Request = str(input('Type Yes to start and No to quit: '))


def Check():
    if Start_Request == 'Yes':
        Start = int(input('Enter starting point: '))
        End = int(input('Enter final point: '))
        End += 1
        print('Available sets are: Odd, Even, Prime')
        User_set = str(input('Which one do you want: '))
        Result = []

        def Odd(Start, End):
            for i in range(Start, End):
                if i % 2 == 1:
                    Result.append(i)
            print(Result)

        def Even(Start, End):
            for i in range(Start, End):
                if i % 2 == 0:
                    Result.append(i)
            print(Result)

        def Prime(Start, End):
            for i in range(Start, End):
                if i > 1:
                    for j in range(2, i):
                        if i % j == 0:
                            break
                    else:
                        Result.append(i)
            print(Result)
        if User_set == 'Odd':
            print('Odd numbers are: ')
            Odd(Start, End)
        elif User_set == 'Even':
            print('Even numbers are: ')
            Even(Start, End)
        elif User_set == 'Prime':
            print('Prime numbers are: ')
            Prime(Start, End)
        print('Shall the program continue? ')
        Continue_Request = str(input('Type Yes to continue and No to quit: '))
        if Continue_Request == 'Yes':
            Check()
        elif Continue_Request == 'No':
            pass
    elif Start_Request == 'No':
        pass


Check()

# Guess
Answer = "Age"
Guess_Attempt = [1, 2, 3]

print("What goes up but never comes down?")
for i in Guess_Attempt:
    Guess = input("Enter your guess: ")
    Guess.capitalize
    if Guess == Answer:
        print('YOU WON!')
        break
    elif Guess != Answer and i == 1:
        print('Wrong, Try again')
    elif Guess != Answer and i == 2:
        print('Wrong, last choice')
    elif Guess != Answer and i == 3:
        print('YOY LOST! The answer is Age')
