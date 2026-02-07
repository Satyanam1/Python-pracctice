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
""" def palindrome(n):
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
palindrome(a) """ 

# Armstrong
""" def Armstrong(n):
    num = str(n)
    power = len(num)
    ans = 0
    for i in num:
        ans += int(i)**power
    if ans == int(n):
        print("Armstrong")
    else: 
        print("Not an Armstrong")  
Armstrong(4) """        

# Reverse a list using functions
""" def reverse(list):
    revlist = []
    for i in range(len(list)-1,-1,-1):
        revlist.append(list[i])
    return revlist
listt=[1,2,3,4,5,6]
print(reverse(listt)) """   

""" def reverse(lst):
    return lst[::-1]
listt = [1,2,3,4,5,6]
print(reverse(listt)) """
            
# Write a function to check Armstrong 
""" def is_armstrong(num):
    digits = str(num)
    power = len(digits)

    total = 0
    for i in digits:
        total += int(i) ** power
    return total == num

if is_armstrong(15):
    print("Armstrong number")
else:
    print("Not an Armstrong number") """

# Second Largest 
""" def second_largest(n):
    n=list(set(n))
    n.sort()
    return n[-2]
listt = [12,13,10,17,18,96]
listt2 = [2,5,10,17,14,90]
print(second_largest(listt)) 
print(second_largets(listt2))"""  



# count digit in a number
""" def count_digit(n):
    count=0
    for i in str(n):
        count+=1
    return count 
a=int(input("Enter a number: ))      
print(count_digit(a))         """


# sum of 1 to n
""" def sum1toN(n):
    sum=0
    for i in range(1,n+1):
        sum+=i
    return sum
a=int(input("Enter Number: "))
print(sum1toN(a)) """  

# Prime or not
""" def prime(n):
    count = 0
    for i in range(1,n+1):
        if n%i==0:
            count+=1
    if count==2:
        print("prime Number")
    else: print("Not Prime Number")
a=int(input("Enter a number: "))
(prime(a)) """ 


""" def frequency_count(lst):
    freq={}
    for item in lst:
        if item in freq:
            freq[item]+=1
        else:
            freq[item]=1
    return freq        
    
listt = [1,2,1,2,1]
print(frequency_count(listt)) """  

# Plus one at the end of list --> [1,2,3]--> [1,2,4] and [1,2,9] --> [1,3,0] 
""" def plusOne(lst):
    n = len(lst)
    for i in range(n-1,-1,-1):
        if lst[i]<9:
            lst[i]+=1
            return lst
        lst[i]=0
    return [1]+lst
    
listt = list(map(int,input("Enter element: ")))
print(plusOne(listt)) """    

# Numbers of step to reduce a number to zero
""" def reduceToZero(num):
    step = 0
    while num!=0:
        if num%2==0:
            num = num//2                
        else:
            num = num-1
        step+=1
    return step
a=int(input("Enter a number: "))
print(reduceToZero(a)) """ 

# Count operation to obtain zero
""" def countZero(num1,num2):
    count=0
    while num1!=0 and num2!=0:
        if num1>=num2:
            num1= num1-num2
        else:
            num2=num2-num1
           
        
        count+=1
    return count
a= int(input("Enter first number: "))
b= int(input("Enter second number: "))  
print(countZero(a,b))           """




