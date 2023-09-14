# Guess

print("What goes up but never comes down?")
Answer = "Age"

for i in range(3):
    Guess = input("Enter your guess: ")
    Guess.capitalize
    if Guess == Answer:
        print('YOU WON!')
        break
    elif Guess != Answer and i == 0:
        print('Wrong, Try again')
    elif Guess != Answer and i == 1:
        print('Wrong, last choice')
    elif Guess != Answer and i == 2:
        print('YOY LOST! The answer is "Age"')
