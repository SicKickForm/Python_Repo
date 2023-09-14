# Creating a class with properties
class Info1:
    Name = 'SicKickForm'
    Age = 18


# ------------------------------------------------------------------------------- #

# Creating an object
Person1 = Info1()
print(Person1.Name + ' is ' + str(Person1.Age))

# ------------------------------------------------------------------------------- #

# Use __init__(self) function to initialize variables in the class
# The __init__() is automatically called when You create object using a class
# Object methods are function inserted into the object


class Info2:
    def __init__(self, Name, Age):
        self.Name = Name
        self.Age = Age

    def Introduce(self):
        print(self.Name + ' is ' + str(self.Age))


Person2 = Info2('Dia', 17)
Person2.Introduce()
Person2.Name, Person2.Age = 'akaTeen', 22
Person2.Introduce()

# ------------------------------------------------------------------------------- #

# Class inheritance (Parent and Child)
# The child's __init__() function overrides the parent's __init__() function
# Call parent's __init__ function to prevent overriding


class Info3(Info2):
    def __init__(self, Name, Age, Community):
        Info2.__init__(self, Name, Age)
        self.Community = Community

    def Introduce2(self):
        print('This is The ' + self.Community)


Person3 = Info3('Siren', 20, 'KKC')
Person3.Introduce()
Person3.Introduce2()

# ------------------------------------------------------------------------------- #

# You can use super() function to prevent overriding too


class Info4(Info2):
    def __init__(self, Name, Age, Date):
        super().__init__(Name, Age)
        self.Date = Date

    def Calendar(self):
        print('Today is ' + self.Date)


Date1 = Info4('SicKickForm', 18, '2/8/2022')
Date1.Calendar()

# ------------------------------------------------------------------------------- #

# Use pass command to ignore class empty properties


class Info5:
    pass

# ------------------------------------------------------------------------------- #

# Class iteration
# raise StopIteration to end the execution


class Num:
    def __iter__(self):
        self.X = 1
        return self

    def __next__(self):
        if self.X <= 10:
            Num = self.X
            self.X += 1
            return Num
        else:
            raise StopIteration


Cls = Num()
Cls = iter(Cls)
for i in range(10):
    print(next(Cls))

# ------------------------------------------------------------------------------- #

# Class polymorphism
# Polymorphism refers to functions that work differently on various objects
# Class inheritance overriding is an example of class polymorphism

class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Drive!")

class Boat(Car):
  def move(self):
    print("Sail!")


car1 = Car("Ford", "Mustang") #Create a Car object
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object

for x in (car1, boat1):
  print(x.brand)
  print(x.model)
  x.move()

# ------------------------------------------------------------------------------- #

del (Person2.Name, Person2.Age, Info1, Person1,
     Info2, Person2, Info3, Person3, Info4, Date1, Info5)
del Num, Cls
