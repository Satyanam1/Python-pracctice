

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

# Object and class
# syntax
""" class class_name:
    "doc string"
    variable
    method
object = class_name()
obj =class_name """    