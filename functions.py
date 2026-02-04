""" # Functions -> Block of statements that perform a specific task.
# syntax - 
# def function_name(parameter1,param2..):
#   some work
#   return val
# function_name(argument1,arg2..) # function call """

# Tupes of Functions ->
# user define
# Built-in/Predrfine

# sum of two number
""" def calculate_sum(a,b):
    print(a+b)
    return a+b
calculate_sum(10,20) """

# Default Parameter -> Assigning a default value to parameter, which is used when no argument is passed.


# Write a function to print the length of a list.
""" cities = ["Patna","Bhopal","Delhi","Mussorie","Indore"]
heroes = ["Shushant Singh Rajput","Hrithik Roshan","Vijay","Salmon bhai","Nitin","Thalapaty"]

def length(list):
    print(len(list))

def print_list(list):
    for item in list:
        print(item,end=' ')

print_list(heroes)
length(heroes) """    

# Factorial of a number using function
""" def factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact *= i
    print(fact)    
factorial(6) """

# Write a function to check a number is even or odd
""" def check(n):
    if n%2==0:
        print("Even")
    else: print("Odd")
check(13) """

# Write a function to convert USD to INR
""" def converter(usd):
    inr_val = usd*87
    print(usd,"USD =",inr_val,"INR")
converter(100) """


""" def my_function(animal,name,age):
    print("I have a", animal,end=' ')
    print("My",animal+ "'s name is ",name,"she is",age,"year's old")
my_function("Pet","Evaa",2) """

# factorial
""" def fibonacci(num):
    fe=0
    se=1
    for i in range(num):
        print(fe,end='')
        fe,se = se,fe+se
fibonacci(4) """        

# Palindrom 

def palindrome(n):
    rev=0
    copy = n
    while(n>0):
        last = n%10
        rev=(rev*10)+last
        n=n//10
    if rev == copy:
        print("palindrome")
    else: print("Not")
a=int(input("enter a number: "))    
palindrome(a)            
