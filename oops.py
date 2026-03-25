

from functools import reduce
# map
""" l1=[1,2,3]
l2=[2,4,5,6,7]
l3=[0,2,4]

def hey(n1,n2,n3):
    return n1+n2+n3
res=map(hey,l1,l2,l3)
print(res)
print(tuple(res)) """

# filter

""" l=[4,6,8]

def even(n):
    if n%2==0:
        return n
res = list(filter(even,l))
print(res) """


# reduce

""" l=[1,2,3,4,5]
def add (sum,x):
    return sum+x
res=reduce(add,l)
res=reduce(add,l,0)
print(res) """

# Square
""" n= int(input("Enter the value: "))
var = lambda x:x**2
print(var(n)) """

# Lambda Function
# lambda variable : if-result if condition else else-result 

# lambda with map
""" l= eval(input("Enter list: "))
res= list(map(lambda n: n**2,l))
print(res) """

# maximum value
""" from functools import reduce
l=[1,12,3,4,5]
res=reduce(lambda x,y:x if x>y else y,l)
print(res) """

# Decorator - Change the behaviour

""" def  outer(var):
    def inner():
        var() / show()
    return inner
def show():
    print("From show function")    
res =outer(show)   """

# Objects / Classes
"""  Python is an object oriented programming languages.
Create a Class
To create a class, use the keyword class: """
class Myclass:
    x=5

# create object
# now we can use the class named myclass to create objects:
p1=Myclass()
# print(p1.x)


# Delete objects
# We can delete objects by using del keyword:

del p1

# Multiple objects
# We can create the multiple objects from the same class:

""" p1=Myclass()
p2=Myclass()
p3=Myclass()

print(p1.x)
print(p2.x)
print(p3.x) """

# __init__() method
# The __init__() method is used to assign values to object properties, or to perform operations that are necessary when the object is being created.

""" class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Emil", 36)

print(p1.name)
print(p1.age) """

""" class Person:
  def __init__(self, name, age=18):
    self.name = name
    self.age = age

p1 = Person("Emil")
p2 = Person("Tobias", 25)

print(p1.name, p1.age)
print(p2.name, p2.age) """


# Self Parameter 
# The self parameter is a reference to the current instance of the class.
# It is used to access properties and methods that belong to the class.

# use self to access class properties
""" class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def greet(self):
    print("Hello, my name is " + self.name)
    print(f"I'm {self.age} Years old")

p1 = Person("Satyanam", 23)
p1.greet() """

# Accessing properties with self 

""" class Car:
  def __init__(self, brand, model, year):
    self.brand = brand
    self.model = model
    self.year = year

  def display_info(self):
    print(f"{self.year} {self.brand} {self.model}")

car1 = Car("Toyota", "Corolla", 2020)
car1.display_info() """

# Class properties

# Properties are variable that belongs to a class. They store data for each object created from the class

""" class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Satyanam", 23)

print(p1.name)
print(p1.age)

# Access Properties -- using dot notation
class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

car1 = Car("Toyota", "Corolla") """

""" print(car1.brand)
print(car1.model)

# Delete Properties 

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Linus", 30)

del p1.age

print(p1.name) """
# print(p1.age) # This will throw an error

# Add new properties
""" class Person:
  def __init__(self, name):
    self.name = name

p1 = Person("Tobias")

p1.age = 25
p1.city = "Oslo"

print(p1.name)
print(p1.age)
print(p1.city) """

# Class Methods
# Methods are functions that belongs to a class. They define the behaviour of objects created from the class

# create a method inn class 
""" class Person:
  def __init__(self, name):
    self.name = name

  def greet(self):
    print("Hello, my name is " + self.name)

p1 = Person("Satyanam")
p1.greet() """

# Methods with Parameters
# Methods can accept parameters just like regular functions

""" class Calculator:
  def add(self, a, b):
    return a + b

  def multiply(self, a, b):
    return a * b

calc = Calculator()
print(calc.add(5, 3))
print(calc.multiply(4, 7)) """


# Methos accessing properties
# Methods can access and modify object properies using self
# A method that accesses object properties:

""" class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def get_info(self):
    return f"{self.name} is {self.age} years old"

p1 = Person("Satyanam", 23)
print(p1.get_info()) """


# __str__() Method
# The __str__() method is a special method that controls what is returned when the object is printed:

# without __str__() method
""" class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Emil", 36)
print(p1) """


# with __str__() method
""" class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name} ({self.age})"

p1 = Person("Tobias", 36)
print(p1) """

# Inheritence 
# parent child relationship
# Inheritance allows us to define a class that inherits all the methods and properties from another class.
# Parent class is the class being inherited from, also called base class.
# Child class is the class that inherits from another class, also called derived class.

# Create a parent class
# Any class can be a parent class, so the syntax is same as creting any other class.

# class Person:
#   def __init__(self, fname, lname):
#     self.firstname = fname
#     self.lastname = lname

#   def printname(self):
#     print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

# x = Person("Satyanam", "Ray")
# x.printname()


""" class parent:
  x=10
  def home(self):
    print("home from parent class")
class child(parent):
  pass
obj=child()
print(obj.x)
obj.home()     """

# Multilevel inheritance
#  
""" class A:
  def home(self):
    print("Hoem from gp")
class B(A):

  def home(self):
    print("Home from Parent")
    super().home()

  def car(self):
    print("car from parent")      
class C(B):
   pass 

obj=C()
obj.home()
obj.car() """

# Multiple Inheritance

""" class A:
  def home(self):
    print("Home from A")
class B:
  def home(self):
    print("home from b")
    A().home()
  def car(self):
    print("car from b")
class C(B,A):
  pass

obj = C()
obj.home()
obj.car() """

# Heirarchical Inheritance

""" class A:
  def home(self):
    print("Hey, Python")
  def about(self):  
    print("Hi, I'm satyanam")
class B(A):
  pass
class C(A):
  pass  

obj = B()
obj2=C()

obj.home()
obj.about() """

# obj2.home()
# obj2.about()


# Hybriud Inheritance

""" class A:
  def home(self):
    print("hello")
  def about(self):
    print()   """

# Abstraction

from abc import ABC, abstractmethod
# class Calculator(ABC):
#   @abstractmethod
#   def register(self):
#     pass
# class B(Calculator):
#   def register(self):
#     return super().register()
#     print("hello")
# obj = B()

""" class Calculator(ABC):
  def add(self,*n):
    sum = 0
    for i in n:
      sum+=i
    print(sum)
  @abstractmethod
  def division(self):
    pass
  def multi(self):
    pass
class A(Calculator):
  def multi(self,*n):
    multi = 1
    for i in n:
      multi*=i
    print(multi) 
  def division(self):
    pass   
obj = A()
obj.add(1,2,3,4,5)
obj.multi(1,2,3)       """

# Encapsulation


# Private variable/ method

class student:
  __school='KDKN Secondary School'
  def __detail(self):
    print("Hey, I'm satyanam")
class A(student):
  pass

obj = A()
print(student._student__school)
# obj._student__detail()
# print(dir(student))

# Polymorphism
 
# OperAtor Polymorphism

x=5
y=2
z=x*y
print(z)

# Function Polymorphism
s="Satyanam"
print(len(s)) # length = 8

s=["Satyanam"]
print(len(s))  # length = 1

# Method Polymorphism
class A:
   def first(self):
      print("Hey")
class B:
   def second(self):
      print("Second")
                    
obj = A()
obj.first() 
                   