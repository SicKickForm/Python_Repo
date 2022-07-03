import datetime
import random
from math import sin
from scipy.optimize import minimize
import matplotlib.pyplot as Plt
import numpy as Np
from tkinter import *
from tkinter import messagebox


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

# Sin(X)
X = Np.arange(0, 2*Np.pi, 0.157)
Y = Np.sin(X)
Plt.plot(X, Y)
Plt.ylabel('( Y )')
Plt.xlabel('( X )')
Plt.title("Sin(X)")
Plt.show()
# Bar
Scores = Np.random.randint(0, 20, 100)
print('Scores:\n', Scores)
Scores_Bool = Scores >= 10
Passed = Scores[Scores_Bool]
print('Passed Scores:\n', Passed)
Data = {'10 - 12': list(filter(lambda X: X <= 12, Passed)),
        '12 - 14': list(filter(lambda X: 12 < X <= 14, Passed)),
        '14 - 16': list(filter(lambda X: 14 < X <= 16, Passed)),
        '16 - 18': list(filter(lambda X: 16 < X <= 18, Passed)),
        '18 - 20': list(filter(lambda X: 18 < X <= 20, Passed)),
        }
print('Sorted Scores:\n', Data)
Values_Len = []
Keys_Name = list(Data.keys())
for i in list(Data.values()):
    Values_Len.append(len(i))
Values_Sum = 0
for i in list(Data.values()):
    for j in i:
        Values_Sum += j
Values_Min = Values_Sum / len(Passed)
Keys_Name.append('AVG')
Values_Len.append(Values_Min)
Plt.bar(Keys_Name, Values_Len)
Plt.show()

# GUI Calculator


class Calc(Frame):
    def __init__(self, master):
        Frame.__init__(self)
        self.master.title("Calculator")
        self.master.configure(background='white')
        self.master.resizable(width=False, height=False)
        self.master.geometry("465x541+540+120")
        self.master = master

        self.Screen = Text(master, height=2, width=30, pady=6, padx=6,
                           bg="#000000", fg="#dddddd", font=('Helvetica', 20, 'bold'))
        self.Screen.grid(row=0, column=0, columnspan=4)
        self.Screen.insert(INSERT, "0")

        Btn_1 = Button(master, text="1", width=6, height=2, bd=4,
                       bg='#000000', fg="#dddddd", font=('Helvetica', 20, 'bold'),
                       command=lambda: self.Num_Input(1))
        Btn_1.grid(row=2, column=0)

        Btn_2 = Button(master, text="2", width=6, height=2, bd=4,
                       bg='#000000', fg="#dddddd", font=('Helvetica', 20, 'bold'),
                       command=lambda: self.Num_Input(2))
        Btn_2.grid(row=2, column=1)

        Btn_3 = Button(master, text="3", width=6, height=2, bd=4,
                       bg='#000000', fg="#dddddd", font=('Helvetica', 20, 'bold'),
                       command=lambda: self.Num_Input(3))
        Btn_3.grid(row=2, column=2)

        Btn_4 = Button(master, text="4", width=6, height=2, bd=4,
                       bg='#000000', fg="#dddddd", font=('Helvetica', 20, 'bold'),
                       command=lambda: self.Num_Input(4))
        Btn_4.grid(row=3, column=0)

        Btn_5 = Button(master, text="5", width=6, height=2, bd=4,
                       bg='#000000', fg="#dddddd", font=('Helvetica', 20, 'bold'),
                       command=lambda: self.Num_Input(5))
        Btn_5.grid(row=3, column=1)

        Btn_6 = Button(master, text="6", width=6, height=2, bd=4,
                       bg='#000000', fg="#dddddd", font=('Helvetica', 20, 'bold'),
                       command=lambda: self.Num_Input(6))
        Btn_6.grid(row=3, column=2)

        Btn_7 = Button(master, text="7", width=6, height=2, bd=4,
                       bg='#000000', fg="#dddddd", font=('Helvetica', 20, 'bold'),
                       command=lambda: self.Num_Input(7))
        Btn_7.grid(row=4, column=0)

        Btn_8 = Button(master, text="8", width=6, height=2, bd=4,
                       bg='#000000', fg="#dddddd", font=('Helvetica', 20, 'bold'),
                       command=lambda: self.Num_Input(8))
        Btn_8.grid(row=4, column=1)

        Btn_9 = Button(master, text="9", width=6, height=2, bd=4,
                       bg='#000000', fg="#dddddd", font=('Helvetica', 20, 'bold'),
                       command=lambda: self.Num_Input(9))
        Btn_9.grid(row=4, column=2)

        Btn_0 = Button(master, text="0", width=6, height=2, bd=4,
                       bg='#000000', fg="#dddddd", font=('Helvetica', 20, 'bold'),
                       command=lambda: self.Num_Input(0))
        Btn_0.grid(row=5, column=1)

        Btn_Plus = Button(master, text="+", width=6, height=2, bd=4,
                          bg='#0011cc', fg="#dddddd", font=('Helvetica', 20, 'bold'),
                          command=lambda: self.Num_Input("+"))
        Btn_Plus.grid(row=1, column=3)

        Btn_Minus = Button(master, text="-", width=6, height=2, bd=4,
                           bg='#0011cc', fg="#dddddd", font=('Helvetica', 20, 'bold'),
                           command=lambda: self.Num_Input("-"))
        Btn_Minus.grid(row=2, column=3)

        Btn_Multip = Button(master, text="*", width=6, height=2, bd=4,
                            bg='#0011cc', fg="#dddddd", font=('Helvetica', 20, 'bold'),
                            command=lambda: self.Num_Input("*"))
        Btn_Multip.grid(row=3, column=3)

        Btn_Divide = Button(master, text="/", width=6, height=2, bd=4,
                            bg='#0011cc', fg="#dddddd", font=('Helvetica', 20, 'bold'),
                            command=lambda: self.Num_Input("/"))
        Btn_Divide.grid(row=4, column=3)

        Btn_LeftP = Button(master, text="(", width=6, height=2, bd=4,
                           bg='#0011cc', fg="#dddddd", font=('Helvetica', 20, 'bold'),
                           command=lambda: self.Num_Input("("))
        Btn_LeftP.grid(row=1, column=1)

        Btn_RightP = Button(master, text=")", width=6, height=2, bd=4,
                            bg='#0011cc', fg="#dddddd", font=('Helvetica', 20, 'bold'),
                            command=lambda: self.Num_Input(")"))
        Btn_RightP.grid(row=1, column=2)

        Btn_Dot = Button(master, text=".", width=6, height=2, bd=4,
                         bg='#0011cc', fg="#dddddd", font=('Helvetica', 20, 'bold'),
                         command=lambda: self.Num_Input("."))
        Btn_Dot.grid(row=5, column=2)

        Btn_Calculate = Button(master, text="=", width=6, height=2, bd=4,
                               bg='#0011cc', fg="#dddddd", font=('Helvetica', 20, 'bold'),
                               command=self.Output)
        Btn_Calculate.grid(row=5, column=3)

        Btn_Clear = Button(master, text="Clear", width=6, height=2, bd=4,
                           bg='#0011cc', fg="#dddddd", font=('Helvetica', 20, 'bold'),
                           command=self.C)
        Btn_Clear.grid(row=1, column=0)

        Btn_Exit = Button(master, text="Exit", width=6, height=2, bd=4,
                          bg='#0011cc', fg="#dddddd", font=('Helvetica', 20, 'bold'),
                          command=self.Exit)
        Btn_Exit.grid(row=5, column=0)

    def Num_Input(self, num):
        if self.Screen.get("0.0", END) == "0\n":
            self.Screen.delete("0.0", END)
        self.Screen.insert(INSERT, str(num))

    def Output(self):
        res = self.Calculation(self.Screen.get("0.0", END)[:-1])
        self.Screen.delete("0.0", END)
        self.Screen.insert(INSERT, str(res))

    def Calculation(self, Exp):
        if Exp == "ERROR":
            return "ERROR"
        try:
            return(float(Exp))
        except ValueError:
            if ")" in Exp:
                Index = 0
                StartIndex = 0
                EndIndex = 0
                for i in range(0, len(Exp)):
                    if Exp[i] == "(":
                        Index += 1
                        StartIndex = i
                    if Exp[i] == ")":
                        Index -= 1
                if Index != 0:
                    messagebox.showerror(
                        "Error", "Brackets don't match!")
                    return "ERROR"
                for i in range(StartIndex, len(Exp)):
                    if Exp[i] == ")":
                        EndIndex = i
                        break
                New_Exp = Exp[:StartIndex] + str(self.Calculation(
                    Exp[StartIndex+1:EndIndex])) + Exp[EndIndex+1:]
                return self.Calculation(New_Exp)
            elif "+" in Exp:
                New_Exp2 = Exp.split("+")
                Rest = self.Calculation(New_Exp2[0])
                for j in New_Exp2[1:]:
                    Rest += self.Calculation(j)
                return Rest
            elif "-" in Exp:
                New_Exp2 = Exp.split("-")
                Rest = self.Calculation(New_Exp2[0])
                for j in New_Exp2[1:]:
                    Rest -= self.Calculation(j)
                return Rest
            elif "*" in Exp:
                New_Exp2 = Exp.split("*")
                Rest = self.Calculation(New_Exp2[0])
                for j in New_Exp2[1:]:
                    Rest *= self.Calculation(j)
                return Rest
            elif "/" in Exp:
                New_Exp2 = Exp.split("/")
                Rest = self.Calculation(New_Exp2[0])
                for j in New_Exp2[1:]:
                    try:
                        Rest /= self.Calculation(j)
                    except ZeroDivisionError:
                        messagebox.showerror("Error", "ERROR: Division by 0!")
                        return "ERROR"
                return Rest
            else:
                messagebox.showerror("Error", "ERROR: Invalid expression!")
                return "ERROR"

    def C(self):
        self.Screen.delete("0.0", END)
        self.Screen.insert(INSERT, "0")

    def Exit(self):
        Exit_Req = messagebox.askyesno("Calculator", "Do You want to exit?")
        if Exit_Req == True:
            Root.destroy()


Root = Tk()
App = Calc(Root)
Root.mainloop()
