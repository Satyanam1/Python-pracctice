# for i in range(1,11,1):
#     i
#     print(i,end=" ")
# print(i)   # i will give output 10

# val =10
# while val>=1:
#     print(val)
#     val-=1

# for i in range(10,0,-1):
#     print(i)    

# Q1. 1 to 10
# for i in range(1,11,1):
#     print(i)

# i=1
# while i<=10:
#     print(i)
#     i+=1

# Q2. 10 to 1
# for i in range(10,0,-1):
#     print(i)

# i=10
# while(i>=1):
#     print(i)
#     i-=1


# num = int(input("Enter a number: "))
# Q3. 1 to n
# for i in range(1,num+1):
#     print(i)

# i=1
# while(i<=num):
#     print(i)
#     i+=1

# Q4 n to 1
# for i in range(num,0,-1):
#     print(i)

# i=num
# while(i>=1):
#     print(i)
#     i-=1

#5

# even
# for i in range(1,num,1):
#     if i%2==0:
#         print(i)

# i=1
# while(i<=num):
#     if i%2==0:
#         print(i)
#     i+=1    

#odd
# for i in range(1,num,1):
#     if i%2!=0:
#         print(i)

#
# i=1
# while(i<=num):
#     if i%2!=0:
#         print(i)
#     i+=1




# prime or not
# num = int(input("Enter a number: "))
# isPrime =True
# i=2
# if num<2:
#     print("Not a prime Number")
# while(i<num):
#     if num%i==0:
#         isPrime=False
#         break
#     i+=1
# if isPrime:
#     print("prime number")
# else:
#      print("Not Prime")
       

# n=int(input("Enter a number: "))
# count=0
# for i in range(1,n+1,1):
#     if(n%i==0):
#         count+=1    
# if count==2:
#     print("prime Number") 
# else: print("Not prime")    


# n=int(input("Enter a number: "))
# isPrime = True
# if n<2: print("Not prime")
# else:
#     for i in range(2,n):
#      if n%i==0:
#         isPrime=False
#         break
#     if isPrime: print("prime number")
#     else: print("Not Prime")


# reverse any number for example 123 to 321

# n = int(input("enter a number: "))
# rev = 0
# while(n>0):
#     digit=n%10
#     rev = (rev*10)+digit
#     n=n//10
# print(rev)

# palindrome or not
# n = int(input("Enter a number: "))
# rev=0
# copy=n
# while(n>0):
#     remainder = n%10
#     rev = (rev*10)+remainder
#     n=n//10
# if rev == copy: print("palindrome")
# else: print("Not palindrome") 
   

# str = input("Enter a word: ")
# if str == str[::-1]:
#     print("palindrome")
# else: print("Not palindrome")   


# rev = ""
# for ch in str:
#     rev = ch + rev
# if rev == str:
#     print("palindrome")       
# else: print("Not palindrome")

# sum of digit of any number

# n=int(input("Enter a number: "))
# sum=0
# while(n>0):
#     last = n%10
#     n=n//10
#     sum = sum + last
# print(sum)


# sum of first and last digit

# n=1234
# sum=0
# while(n>0):
#     last = n%10
#     sum = sum + last 
#     n=n//1000
# print(sum)   


# n=int(input("Enter a number: "))
# var=n
# lastDigit = n%10

# while var>=10:
#     var = var//10
# first = var    
# print(first+lastDigit)
    

# Greatest digit in a number 78925-->9

# n= int(input("Enter a number: "))
# greatest = 0

# while n>0:
#     digit = n%10
#     if digit>greatest:
#         greatest=digit
#     n=n//10
# print(greatest)


# smallest digit in a number

# n= int(input("Enter a number: "))
# smallest=10
# while n>0:
#     digit = n%10
#     if digit<smallest:
#         smallest=digit
#     n=n//10
# print(smallest)    


# Q count digit

# n = int (input("enter: "))
# count =0
# while(n>0):
#     count+=1
#     n=n//10
# print(count)   


# n=int(input("Enter a number: "))

# sum=0
# for i in range(1,n+1):
#     if i%2==0:
#         sum=sum+i
# print(sum)


# sum=0
# for i in range(1,11):
    
#     if i%2!=0:
#      sum+=i
# print(sum)


# fact =1
# for i in range(1,n+1):
#     fact*=i
# print(fact)


# reverse a number like 123 to 321

# rev = 0
# while(n>0):
#     rem = n%10
#     rev = rev*10+rem
#     n=n//10
# print(rev)    

# count digit 

# count =0
# while(n>0):
#     count+=1
#     n=n//10
# print(count) 


# sum of digit of number
# sum=0
# while(n>0):
#     lastDigit=n%10
#     n=n//10
   
#     sum+=lastDigit       
# print(sum)   

# n=int(input("Enter a number: "))
# for i in range(1,11):
#     print(n,"*",i,"=",n*i)

# n= int(input("Enter a number: "))
# count =0
# for i in range(1,n+1):
#     if n%i==0:
#         count+=1
# if count==2:
#     print("prime number")
# else: print("Not prime") 



# reverse a number

# num = input("Enter a charcter: ")
# print(num[::-1])
# if num[::-1]==num:
#     print("palindrome")
# else: print("Not palindrome")    


# check if a number is Armstrong or not

# num = input("Enter a number: ")
# power = len(num)
# ans = 0

# for i in num:
#     ans+= int(i)**power
# if ans == int(num):
#     print("Armstrong")
# else: print("Not an Arrmstrong")

# count the digit in a number

# num = input("Enter a number: ")
# count = 0
# for i in num:
#     count+=1
# print(count)

# sum of digit in a number

# num = input("Enter a number: ")
# sum = 0
# for i in num:
#     sum = sum +int(i)
# print(sum)

# sum of only even digit in anumber
# num = input("Enter a number")
# sum = 0
# for i in num:
#     if int(i)%2==0:
#         sum = sum + int(i)
# print(sum)


# for i in num:
#     if int(i)%2==0:
#         print(i)


# print maximum digit in a number 572-> 7
# num = int(input("Enter a number: "))
# maximum = 0
# while(num>0):
#     digit = num%10
#     if digit>maximum:
#         maximum=digit
#     num = num//10
# print(maximum)  

# min = 9
# while(num>0):
#     digit = num%10
#     if digit<min:
#         min=digit
#     num = num//10    
# print(min)


# data = [1,2,3,4]
# start = 0
# end = len(data)-1

# while start<end:
#     data[start],data[end]=data[end],data[start]
#     start+=1
#     end-=1
# print(data)    



# second largest

# data = [1,5,70,9,2,14,17,15]
# largest = data[0]
# second_largest = data[0]
# for i in data:
#     if i>largest:
#         second_largest=largest
#         largest=i
#     if i<largest and i>second_largest:
#         second_largest=i      
# print(second_largest)

# data = [1,1,2,1,2,12,1]
# freq = {}

# for i in data:
#     if i not in freq:
#         freq[i]=1
#     else:
#         freq[i]+=1
# print(freq)

# welcome -> eelcomw

# name="welcome"
# print(name[-1]+name[1:-1]+name[0])


# prime or not
# num = int(input("Enter a number: "))
# count = 0
# for i in range(1,num+1):
#     if num%i==0:
#         count +=1    
# if count == 2:
#     print("Prime Number")
# else: print("Not a Prime Number")


# sum first and last digit of four digit number

# n = int(input("Enter four Number: "))
# sum = 0
# while(n>0):
#     last = n%10
#     sum = sum +last
#     n=n//1000
# print(sum)  

# num = int(input("Enter any Number: "))
# temp = num
# last = num%10
# while temp>=10:
#     temp = temp//10
# first = temp
# print(first+last)

# smallest number from a list

# list = [4,7,5,2,6,8]
# smallest = list[0]
# for i in list:
#     if i<smallest:
#         smallest=i
# print(smallest)

# second smallest number in a tuple

# num = (90,32,45,6,1)
# samllest = num[0]
# secondSmallest=num[0]
# for i in num:
#     if i<samllest:
#         secondSmallest= samllest
#         samllest=i
#     if i > samllest and i<secondSmallest:
#         secondSmallest=i
# print(secondSmallest)  
# 
#  

word = "welcome to cybrom"
count =0
for i in word:
    count+=1
print(count)    