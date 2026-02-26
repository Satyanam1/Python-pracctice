# n=5
# for i in range(1,n+1):
#     print("*"*i+"")

# for i in range(1,n+1):
#     print(" "*(n-i) + "*"*i)  

# for i in range(0,n):
#     print("*"*(n-i)+" "*i)   

# for i in range(0,n):
#     print(" "*i+"*"*(n-i))   

# for i in range(1,n+1):
#     print(" "*(n-i)+"* "*i)

# num = int(input("Enter row number: "))
# for i in range(1,num+1):
#     for j in range(i):
#         print(i,end="") 
#     print() 

# for i in range(1,num+1):
#     for j in range(1,i+1):
#         print(j,end="")
#     print()

# for i in range(1,n+1):
#     for j in range(i):
#         print("*",end="")
#     print()   

# for i in range(num):
#     for j in range(num):
#         print("*",end=' ')
#     print() 

# for i in range(n):
#     for j in range(i,n):
#         print('*',end='')
#     print()


# num = int(input("Enter row number: "))
# i=1
# while i<=num:
#     print("*"*num)
#     i+=1

# while i<=num:
#     print("*"*i+" "*(n-i))
#     i+=1


# while i<=num:
#     print(" "*(n-i)+"* "*i)
#     i+=1


# i=0
# while i<num:
    # print('*'*(n-i)+" "*i)
    # print(" "*i+"*"*(n-i))
    # print(" "*i+"* "*(n-i))
    # i+=1

""" i=1
while i<=n:
    print("*"*i+" "*(n-i))
    i+=1
i=i-2
while i>0:
    print("*"*i+" "*(n-i))
    i-=1 """

num = int(input("Enter row number: "))

""" for i in range(1,num+1):
    for j in range(1,num+1):
        print("*",end=" ")
    print() """

""" for i in range(1,num+1):
    for j in range(1,i+1):
        print("*",end=" ")
    print() """

""" for i in range(1,num+1):
    x=1
    for j in range(1,i+1):
        print(x,end=" ")
        x+=1
    print() """ 

""" for i in range(1,num+1):
    x=3
    for j in range(1,i+1):
        print(x,end=" ")
        x+=3
    print() """  

""" x=2
for i in range(1,num+1):
    for j in range(1,i+1):
        print(x,end=" ")
        x+=2
    print()                  """


# ch='A'
""" for i in range(1,num+1):
    ch='A'
    for j in range(1,i+1):
        print(ch,end=" ")
        ch=chr(ord(ch)+1)
    print() """


i=1
""" while i<=num:
    if i==3 or i==5:
        i+=1
        continue
        
    print(i)
    i+=1 """

while i<=num:
    if i==3 or i==5:
        pass
    print(i)
    i+=1