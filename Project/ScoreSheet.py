import os
import shutil

# Score Sheet

class Lessons:
    def __init__(self, name):
        self.name = name
        self.grade = None

    def set_grade(self, grade):
        self.grade = grade

    def __str__(self):
        return f"{self.name}: {self.grade}"

class Students:
    def __init__(self, f_name, l_name, age, national_id, year, math_score=None, physics_score=None, computer_science_score=None, history_score=None, student_id=None, border=None):
        self.fname = f_name
        self.lname = l_name
        self.age = age
        self.national_id = national_id
        self.year = year
        self.math = Lessons("Math Score")
        self.physics = Lessons("Physics Score")
        self.computer_science = Lessons("Computer Science Score")
        self.history = Lessons("History Score")
        self.math.set_grade(math_score)
        self.physics.set_grade(physics_score)
        self.computer_science.set_grade(computer_science_score)
        self.history.set_grade(history_score)
        self.student_id = student_id
        self.border = border

    def __str__(self):
        return f"First Name: {self.fname}\tLast Name: {self.lname}\tAge: {self.age}\nNational ID: {self.national_id}\tEntrance Year: {self.year}\tStudent Id: {self.student_id}\n{self.border}\n{self.math}\n{self.physics}\n{self.computer_science}\n{self.history}"


def Create_Score_Report(Sample_Student):
    global Create_Score_Report
    file = open(f"{Sample_Student.student_id}.txt", "w+")
    file.write(str(Sample_Student))
    file.close()


F_NAME = input("Enter First Name: ")
L_NAME = input("Enter Last Name: ")
AGE = input("Enter Age: ")
NATIONAL_ID = input("Enter National Id: ")
YEAR = input("Enter The 4Digit Entrance Year: ")
MATH = input("Enter Math Score: ")
PHYSICS = input("Enter Physics Score: ")
CS = input("Enter Computer Science Score: ")
HISTORY = input("Enter History Score: ")
STUDENT_ID = f"{NATIONAL_ID}{YEAR}"
BORDER = "--------------------------------------------------------------------"

Sample_Student = Students(F_NAME, L_NAME, AGE, NATIONAL_ID,
                          YEAR, MATH, PHYSICS, CS, HISTORY, STUDENT_ID, BORDER)
Create_Score_Report(Sample_Student)

# ------------------------------------------------------------------------------- #

# Find Score Sheet

SID = input("Enter The Student Id You Are Looking For\n(Note: Student Id Is National Id Followed By 4Digit Entrance Year): ")
SID += ".txt"

Score_Reports = 'D:\Github\Github\Code\Python_Repo'
Result = 'D:\Github\Github\Code\Python_Repo\Result'
Request = os.path.join(Score_Reports, SID)

if not os.path.isfile(Request):
    print("There Is Noone With That National Id")
else:
    if not os.path.isdir(Result):
        os.makedirs(Result)
        shutil.copy2(Request, os.path.join(Result, SID))
    else:
        shutil.copy2(Request, os.path.join(Result, SID))
