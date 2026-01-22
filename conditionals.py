# Conditional statement -->

# Syntax  if-elif-else


# if(condition):
#     Statement1
# elif(condition):
#     statement2
# else:
#     statementN 

# Q1 Eligible for vote or not

""" age = int(input("Enter age: "))
if age>=18:
    print("Eligible for vote")
else:
    print("Not Eligible for vote") """


age = int(input("Enter age: "))
vote = ("yes","No") [age<=18]
print(vote)



""" income=int(input("Enter your income:"))

if income>=0 and income<=250000:
    print("You Do not need to pay tax")
    tax=0
elif income>250000 and income<=500000:
    print("you have to pay 5% tax") 
    tax = (income*5)/100
    # print("Your taxable amount is:",tax)  
elif income>500000 and income<=1000000:
    print("You have to pay 10% tax")
    tax=(income*10)/100
    # print("Your taxable amount is:",tax)
elif income>1000000:
    print("20% tax")
    tax=(income*20)/100   
    # print("your taxable amount is:",tax)
else:
    ("Invalid amount")  


print("your taxable amount is:",tax) """


# physics = int(input("Enter your physics marks:"))              
# chemistry = int(input("Enter your chemistry marks:"))              
# math = int(input("Enter your math marks:"))  

# if physics>=75 and chemistry>=75 and math>=75:
#     print("Distinction")
#     # print(percentage)
# elif ((physics>=60 and physics<75) and (chemistry>=60 and chemistry<75) and (math>=60 and math<75)):
#     print("First Division")  
# elif ((physics>=40 and physics<60) and (chemistry>=40 and chemistry<60) and (math>=40 and math<60)):
#     print("Second Division")
# elif ((physics<40 and physics>=0) and (chemistry<40 and chemistry>=0) and (math<40 and math>0)):
#     print("Fail")
# else:
#     print("Please enter valid marks:")            

# percentage=(physics+chemistry+math)*(100/300)
# print("your percentage is:",percentage)


""" print("WELCOME TO SBI ATM 😊")
print("Enter your choice:")
print("Enter 1 for Balance check:")
print("Enter 2 for Deposit:")
print("Enter 3 for Withdraw:")
print("Enter 4 for Exit:")

choice = int(input("Enter 1 to 4:"))
balance = 5000
if choice == 1 :
    print("Balance Checking...")
    print("Your Balance is:",balance)
    print("Thank You!")
    
elif choice==2:
    amount=int(input("Enter deposit amount:"))
    if amount<0:
        print("Please enter positive amount")
    else:
        total=balance+amount
        print("Your balance is now:",total)
elif choice ==3:
     amount=int(input("Enter Withdraw amount:"))
     print("Withdrawl Successful!!")
     total=balance-amount
     print("Your balance is now:",total)
elif choice ==4:
    print("Exiting....")
    print("Thank You!") """



""" char = input("Enter a character:")
if char>='a' and char<='z':
    print("Alphabet")
elif char>='0' and char<='9':
    print("Digit")
else:
    print("Special character") """ 




""" a = int(input("Enter first Numbers:"))
b = int(input("Enter second Numbers:"))
c = int(input("Enter third Numbers:"))

if a>b and a>c:
    print("a is largest",a)
    if a<b and a<c:
        print("smallest is:",a)
    elif b<c and b<a:
        print("B is smallest",b)
    else:
        print("c is smallest:",c)
elif b>a and b>c:
    print("b is largest",b)
    if b<a and b<c:
        print("b is smallest",b)
    elif a<b and a<c:
        print("a is smallest:",a)
    else:
        print("c is smallest:",c)
else:
    print('c is largest',c)  
    if b<a and b<c:
        print("b is smallest",b)
    elif a<b and a<c:
        print("a is smallest:",a)
    else:
        print("c is smallest:",c)  """  


""" 
units=int(input("Enter units:"))
if units>0 and units<=100:
    bill = units*1.5
elif units>100 and units<=200:
    bill = (100*1.5)+(units-100)*2.5
elif units>200:
    bill= (100*1.5)+(100*2.5)+(units-200)*4
print("Your total bill is:",bill) """  







