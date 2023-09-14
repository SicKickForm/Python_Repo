import random

# Rock-Paper-Scissor

Rounds = int(input('How many rounds are You playing? '))
print('Modes are: Solo player (S), Multi player (M)')
Mode = input('What mode are you playing? ')
count = 1
player1_points = 0
player2_points = 0

if Mode == 'M':
    while count <= Rounds:
        Choices = ['rock', 'paper', 'scissor']
        print('Choices are: ' + str(Choices))
        Player1 = input('Enter 1st choice: ')
        Player2 = input('Enter 2nd choice: ')
        if Player1 == 'rock':
            if Player2 == 'scissor':
                print('Player 1 won')
                player1_points += 1
                count += 1
            elif Player2 == 'paper':
                print('Player 2 won')
                player2_points += 1
                count += 1
            else:
                print('Wrong choice')
        if Player1 == 'paper':
            if Player2 == 'scissor':
                print('Player 2 won')
                player2_points += 1
                count += 1
            elif Player2 == 'rock':
                print('Player 1 won')
                player1_points += 1
                count += 1
            else:
                print('Wrong choice')
        if Player1 == 'scissor':
            if Player2 == 'rock':
                print('Player 2 won')
                player2_points += 1
                count += 1
            elif Player2 == 'paper':
                print('Player 1 won')
                player1_points += 1
                count += 1
            else:
                print('Wrong choice')

elif Mode == 'S':
    while count <= Rounds:
        Choices = ['rock', 'paper', 'scissor']
        print('Choices are: ' + str(Choices))
        Player1 = input('Enter Your choice: ')
        Player2 = random.choice(Choices)
        print('Player2 chose ' + Player2)
        if Player1 == 'rock':
            if Player2 == 'scissor':
                print('Player 1 won')
                player1_points += 1
                count += 1
            elif Player2 == 'paper':
                print('Player 2 won')
                player2_points += 1
                count += 1
        if Player1 == 'paper':
            if Player2 == 'scissor':
                print('Player 2 won')
                player2_points += 1
                count += 1
            elif Player2 == 'rock':
                print('Player 1 won')
                player1_points += 1
                count += 1
        if Player1 == 'scissor':
            if Player2 == 'rock':
                print('Player 2 won')
                player2_points += 1
                count += 1
            elif Player2 == 'paper':
                print('Player 1 won')
                player1_points += 1
                count += 1
        else: 
            print("Wrong choice")
else:
    print('Wrong mode')

print('Player1 points are ' + str(player1_points))
print('Player2 points are ' + str(player2_points))
if player1_points > player2_points:
    print('Player1 is the total winner')
elif player2_points > player1_points:
    print('Player2 is the total winner')
else:
    print('Total result is tie')
    