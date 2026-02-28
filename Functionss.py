""" x='Hello'
print(x)
print(print(x)) """

""" def new(a,b):
    c=a+b
    return c
p=int(input("Enter a number: "))    
q=int(input("Enter second number: "))    
    
res=new(p,q)
print(res) """

# x=print("hello")
# print(x)

# s="Python"
# x=print(max(s))
# print(x)

# s='abcde'
""" max=0
for i in s:
    x=ord(i)
    if max<x:
        max=x

print(chr(max)) """
               
""" def maxvalue(s):
    max=0
    for i in s:
        x=ord(i)
        if max<x:
            max=x
    print(chr(max))        
a=input("Enter any string: ") 
maxvalue(a) """


 
""" def minimum(s):
    min=255
    for i in s:
        x=ord(i)
        if min>x:
            min=x

    print(chr(min))
a=input("Enter string: ")
minimum(a)  """


""" def secondLargest(lst):
    max=lst[0]
    secondMax=lst[0]
    for i in lst:
        if i>max:
            secondMax=max
            max=i
        if i<secondMax and i>max:
              secondMax=i
    return secondMax

listt = list(map(int,input("Enter a list: ")))
print(secondLargest(listt))  """          


# s="Python"
# l=0
# for i in s:
#      l+=1
# print(l) 

""" def len(s):
     l=0
     for i in s:
          l+=1
     print(l)

a=input("Enter string: ")
len(a) """


# without argument, without return 
# def hey():
#     print("hello")
# hey() 

# def hello(x=10,y=20):
#     print(x+y)
# hello()       


# without argument with return

# def hi():
#     return "Hello"
# print(hi())
# res=hi()
# print(res)

# def hi(x=10,y=20):
#     return x+y
# print(hi())
# res = hi()
# print(res)

# with argument with return
""" def name(x):
    return 'welcome'+' '+x
x=input("Enter name: ")
faa=name(x)
print(faa) """


# with argument without return
# def name(x):
#     print("welcome"+' '+x)
# x=input("Enter name: ")
# name(x)

# def demo(z,y,x):
#     print(x,y,z)
# p=int(input("Enter first number: "))    
# q=int(input("Enter second number: "))    
# r=int(input("Enter third number: "))  
# demo(p,q,r) 
# demo()   #error-- missing 3 arguments
# demo(p)
# demo(p,q)

# default argument
""" def demo(z=0,y=0,x=0,a=0,b=0):
    print(x,y,z,b,a)
p=int(input("Enter first number: "))    
q=int(input("Enter second number: "))    
r=int(input("Enter third number: "))  
s=int(input("Enter fourth number: "))  
t=int(input("Enter fifth number: "))  
demo(p,q,r,s,t) """ 


# variable length positional arguments(*args)
def add(*args):
    print(args)
    print(type(args))
add(1,2,3,4,5,6)    


