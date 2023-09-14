import random

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
Items = [1, 2, 3, 4, 5, 6, 7, 8]

def Jackpot():
    global Win, Lose, Attempt
    Item1 = random.choice(Items)
    Item2 = random.choice(Items)
    Item3 = random.choice(Items)
    print('         ', '-------------')
    print('         ', '|', random.choice(Items), '|', random.choice(Items), '|', random.choice(Items), '|')
    print('         ', '-------------')
    print('Your Row:', '|', Item1, '|', Item2, '|', Item3, '|')
    print('         ', '-------------')
    print('         ', '|', random.choice(Items), '|', random.choice(Items), '|', random.choice(Items), '|')
    print('         ', '-------------')
    
    if Item1 == Item2 == Item3:
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
