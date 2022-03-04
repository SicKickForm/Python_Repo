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
