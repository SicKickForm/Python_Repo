import datetime
import random
from math import sin
from scipy.optimize import minimize

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

# Dice

Numbers = [1, 2, 3, 4, 5, 6]
print('Which mode do you play?')
Mode = input('Enter S for solo and D for duo mode: ')
if Mode == 'S':
    def Play():
        def solo():
            Play_Command = input('Enter P to play or Q to quit: ')
            if Play_Command == 'P':
                Roll_Command = input('Enter R to roll: ')
                if Roll_Command == 'R':
                    P_Num = random.choice(Numbers)
                    S_Num = random.choice(Numbers)
                    print('Your dice is ' + str(P_Num))
                    print('System dice is ' + str(S_Num))
                    P1_Point = 0
                    P2_Point = 0
                    if P_Num > S_Num:
                        print('You Won!')
                        P1_Point += 1
                    elif P_Num == S_Num:
                        print('Tie!')
                    elif S_Num > P_Num:
                        print('Opponent Lost!')
                        P2_Point += 1
                    print('Player: ' + str(P1_Point) +
                          'Opponent: ' + str(P2_Point))
                else:
                    print('Game Over')
        solo()
        Play()
    Play()
elif Mode == 'D':
    People = int(input('How many people you play with? '))
    Rounds = int(input('How many rounds You play? '))
    # 2.Duo Player
    if People == 2:
        for i in range(Rounds):
            P1_Point = 0
            P2_Point = 0
            P1_Roll_Command = input(('Player Enter R to toll: '))
            if P1_Roll_Command == 'R':
                P1_Num = random.choice(Numbers)
                print('Player dice is ' + str(P1_Num))
            else:
                print('Try Again')
            P2_Roll_Command = input(('Opponent Enter R to roll:'))
            if P2_Roll_Command == 'R':
                P2_Num = random.choice(Numbers)
                print('Opponent dice is ' + str(P2_Num))
                if P1_Num > P2_Num:
                    print('Player Won!')
                    P1_Point += 1
                elif P1_Num == P2_Num:
                    print('Tie!')
                elif P2_Num > P1_Num:
                    print('Opponent Won!')
                    P2_Point += 1
        print('Player: ' + str(P1_Point) + ' Opponent' + str(P2_Point))
    elif People == 3:
        for i in range(Rounds):
            P1_Point = 0
            P2_Point = 0
            P3_Point = 0
            P1_Roll_Command = input(('Player Enter R to toll: '))
            if P1_Roll_Command == 'R':
                P1_Num = random.choice(Numbers)
                print('Player dice is ' + str(P1_Num))
            else:
                print('Try Again')
            P2_Roll_Command = input(('Opponent Enter R to roll:'))
            if P2_Roll_Command == 'R':
                P2_Num = random.choice(Numbers)
                print('Opponent dice is ' + str(P2_Num))
            P3_Roll_Command = input(('Player Enter R to toll: '))
            if P3_Roll_Command == 'R':
                P3_Num = random.choice(Numbers)
                print('Player dice is ' + str(P3_Num))
            else:
                print('Try Again')
            if P1_Num > P2_Num and P1_Num > P3_Num:
                print('Player 1 Won!')
                P1_Point += 1
            elif P2_Num > P1_Num and P2_Num > P3_Num:
                print('Player 2 Won!')
                P2_Point += 1
            elif P3_Num > P1_Num and P3_Num > P2_Num:
                print('Player 3 Won!')
                P3_Point += 1
            print('Player 1: ' + str(P1_Point) + ' Player 2: ' +
                  str(P2_Point) + ' Player 3: ' + str(P3_Point))

# Total Score


def TS():
    Lesson_Number = int(input('How many lessons? '))
    Points = 0
    Credits = 0
    for i in range(Lesson_Number):
        P = {
            'Lesson': input("Enter lesson's name: "),
            'Credit': int(input("Enter lesson's credit: ")),
            'Score': int(input("Enter lesson's score: ")),
        }
        Result = {
            'Lesson': P['Lesson'],
            'Credit': P['Credit'],
            'Score': P['Score'],
            'Point': P['Score'] * P['Credit']
        }
        Points += Result['Point']
        Credits += Result['Credit']
    print('Yout total score is:', Points / Credits)
    Cmd = input('Enter Q to quit or U to use : ')
    if Cmd == 'U':
        TS()
    elif Cmd == 'Q':
        print('Program Over')


TS()

# Total score 2

Dict = {
    'Lessons': {
        'L1', 'L2', 'L3'},
    'Scores': {
        'L1': 17, 'L2': 14, 'L3': 19},
    'Credits': {
        'L1': 3, 'L2': 4, 'L3': 2}}

TPoints = list(map(
    lambda A: Dict['Scores'][A] * Dict['Credits'][A], Dict['Lessons']
))
TCredits = list(map(
    lambda A: Dict['Credits'][A], Dict['Lessons']
))
print('Your total score is: ', sum(TPoints) / sum(TCredits))

# Jackpot

print('''
Welcome To Our Community
Your World Of Jackpots Awaits
We're so glad you're here! You are now a part of our amazing community 
Whether you've joined to win or just to have fun, we've got something for you.
Let's go! ''')
Attempt = 0
Win = 0
Lose = 0


def Jackpot():
    global Win
    global Lose
    global Attempt
    Items = [1, 2, 3, 4, 5, 6, 7, 8]
    Item1 = random.choice(Items)
    Item2 = random.choice(Items)
    Item3 = random.choice(Items)
    Item4 = random.choice(Items)
    Item5 = random.choice(Items)
    Item6 = random.choice(Items)
    Item7 = random.choice(Items)
    Item8 = random.choice(Items)
    Item9 = random.choice(Items)
    print('         ', '-------------')
    print('         ', '|', Item1, '|', Item2, '|', Item3, '|')
    print('         ', '-------------')
    print('Your Row:', '|', Item4, '|', Item5, '|', Item6, '|')
    print('         ', '-------------')
    print('         ', '|', Item7, '|', Item8, '|', Item9, '|')
    print('         ', '-------------')
    if Item4 == Item5 == Item6:
        print('Jackpot! YOU WON')
        Win += 1
        Attempt += 1
    else:
        print('You lost! Better luck next time')
        Lose += 1
        Attempt += 1


def Result():
    print('Games Played: ', Attempt)
    print('Games Won: ', Win)
    print('Games Lost: ', Lose)


def Run():
    Command = input('Please Enter P to play or Q to quit: ')
    if Command.upper() == 'P':
        Jackpot()
        Run()
    elif Command.upper() == 'Q':
        print('Game Over')
    else:
        print("Sorry I didn't get that! Please Try again")
        Run()


Run()
Result()

# Total score 3


class Cls():
    def __init__(self, name, score, credit):
        self.name = name
        self.score = score
        self.credit = credit
        self.point = self.score * self.credit


L1 = Cls('Programming', 14, 4)
L2 = Cls('Algebra', 17, 3)
L3 = Cls('Calculus', 18, 3)
L4 = Cls('History', 19, 2)
Lessons = [L1, L2, L3, L4]

TP = 0
TC = 0
for i in Lessons:
    TP += i.point
    TC += i.credit

print('Your total score is', TP / TC)

# Scipy


def Eqn(X):
    return X**2 + sin(X) + 3


print(minimize(Eqn, 0, method='BFGS'))
