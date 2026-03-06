# f=open("demo.txt",'r')
# data = f.read()
# print(data)
# line1 = f.readline()
# print(line1)

# line2 = f.readline()
# print(line2)
# f.close()

""" with open("demo.txt",'r') as f:
    data = f.read()
    print(data)

with open("demo.txt",'w') as f:
    f.write("hello ") """

""" Deleting a file
using the os module
import os
os.remove("demo.txt") """


""" with open("practice.txt",'r') as f:
    data = f.read()
new_data = data.replace("java","Python") 
print(new_data) 

with open("practice.txt",'w') as f:
    f.write(new_data) """

""" def tablegenerator(n):
    table=""
    for i in range(1,11):
        table+=f"{n}X{i}={n*i}\n"
    with open(f"tables/table{n}.txt","w") as f:
        f.write(table)
for i in range(2,31):
    tablegenerator(i)             """