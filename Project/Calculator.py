# Calculator

print('Operations are : Addition (+), Subtraction (-), Multiplication (*), Division (/)')
Operation = str(input('Select an operation sign: '))
Quantity = int(input('How many numbers do you enter? '))
Nums = []
for i in range(Quantity):
    Num = int(input('Enter a number: '))
    Nums.append(Num)
print('Your numbers are ' + str(Nums))

def Addition(NumList):
    i = 0
    for num in NumList:
        i += num
    return (i)
    
def Subtraction(NumList):
    i = Nums[0]
    for num in NumList[1:]:
        i -= num
    return i

def Multiplication(NumList):
    i = 1
    for num in NumList:
        i *= num
    return (i)

def Division(NumList):
    i = Nums[0]
    for num in NumList[1:]:
        i /= num
    return (i)

def Ops(Operation):
    if Operation == '+':
        print('Addition is ' + str(Addition(Nums)))
    if Operation == '-':
        print('Subtraction is ' + str(Subtraction(Nums)))
    if Operation == '*':
        print('Multiplication is ' + str(Multiplication(Nums)))
    if Operation == '/':
        print('Divison is ' + str(Division(Nums)))

Ops(Operation)
