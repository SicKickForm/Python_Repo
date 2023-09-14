# Total Score

Cmd = input('Enter Q to quit or U to use : ')

def TS(Lesson_Count, Points, Credits):
    for i in range(Lesson_Count):
        Sample = {
            'Lesson': input("Enter lesson's name: "),
            'Credit': int(input("Enter lesson's credit: ")),
            'Score': int(input("Enter lesson's score: ")),
        }
        Sample['Point'] = Sample['Score'] * Sample['Credit']
        Points += Sample['Point']
        Credits += Sample['Credit']
    print('Yout total score is:', Points / Credits)


if Cmd == 'U':
    Lesson_Count = int(input('How many lessons? '))
    Points = 0
    Credits = 0
    TS(Lesson_Count, Points, Credits)
elif Cmd == 'Q':
    print('Program Over')

# ------------------------------------------------------------------------------- #

# Total Score 2

Lesson_Count2 = int(input("How many lessons?"))
Points2 = []
TPoints = TCredits = 0

for i in range(Lesson_Count2):
    Points2.append(int(input("Enter lesson's credit: ")))
    Points2.append(int(input("Enter lesson's score: ")))

for i in range(2*Lesson_Count2):
    if i%2 == 1:
        TPoints += Points2[i] * Points2[i-1]
    elif i%2 == 0:
        TCredits += Points2[i]
print('Your total score is: ', TPoints / TCredits)

# ------------------------------------------------------------------------------- #

# Total Score 3

Add_Lesson = input("Type + to add a lesson and R for result: ")
Total = []

class Lesson():
    def __init__(self, score, credit):
        self.score = score
        self.credit = credit
        self.point = self.score * self.credit

def Result():
    TPoints2 = TCredits2 = 0
    for i in range(len(Total)):
        if i%2 == 1:
            TPoints2 += Total[i] * Total[i-1]
        elif i%2 == 0:
            TCredits2 += Total[i]
    print('Your total score is: ', TPoints2 / TCredits2)

def add():
    Lesson_Sample = Lesson(int(input("Credit: ")),int(input("Score: ")) )
    Total.insert(0, Lesson_Sample.credit)
    Total.insert(0, Lesson_Sample.score)
    Add_Lesson = input("Type + to add a lesson and R for result: ")
    if Add_Lesson == "+":
        add()
    elif Add_Lesson == "R":
        Result()

add()
