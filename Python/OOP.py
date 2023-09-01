# Creating class with properties
class Info1:
    Name = 'SicKickForm'
    Age = 18


# Creating object
Person1 = Info1()
print(Person1.Name + ' is ' + str(Person1.Age))
# Use __init__() function to assign values
# The __init__() is automatically called when You create object using a class
# Object methods are function inserted into the object


class Info2:
    def __init__(self, Name, Age):
        self.Name = Name
        self.Age = Age

    def Func1(self):
        print(self.Name + ' is ' + str(self.Age))


Person2 = Info2('Dia', 17)
Person2.Func1()
Person2.Name = 'akaTeen'
Person2.Age = 22
Person2.Func1()
# Class inheritance (Parent and Child classes)
# The child's __init__() function overrides the parent's __init__() function
# Call parent's __init__ function to prevent overriding


class Info3(Info2):
    def __init__(self, Name, Age, Community):
        Info2.__init__(self, Name, Age)
        self.Community = Community

    def Func2(self):
        print('This is The ' + self.Community)


Person3 = Info3('Siren', 20, 'KKC')
Person3.Func1()
Person3.Func2()
# You can use super() function to prevent overriding too


class Info4(Info2):
    def __init__(self, Name, Age, Date):
        super().__init__(Name, Age)
        self.Date = Date

    def Func3(self):
        print('Today is ' + self.Date)


Date1 = Info4('SicKickForm', 18, '2/8/2022')
Date1.Func3()

# Use pass command to ignore class empty properties


class Info5:
    pass


del (Person2.Name, Person2.Age, Info1, Person1,
     Info2, Person2, Info3, Person3, Info4, Date1, Info5)

# Class iteration
# Use raise StopIteration command to end the execution


class Num:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 10:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration


Cls = Num()
Cls = iter(Cls)
print(next(Cls))
print(next(Cls))
print(next(Cls))
print(next(Cls))
print(next(Cls))
print(next(Cls))
print(next(Cls))
print(next(Cls))
print(next(Cls))
print(next(Cls))

# Class polymorphism refers to functions that can be used on multiple objects
# Class inheritance is an example of class polymorphism
# Child classes inherits the properties and methods from the parent class



del Num, Cls
