# Dictionary in Python --> 
#    • dictionaries are used to store data values in key:value pairs
#    • They are Unordered,mutable(changable) and don't allow duplicate keys

# key-Value pair
# key-unique
# value- can be duplicate


student = {
   "name":"satyanam",
   "Dept":"CSE",
   "language":['Python','JavaScript'],
   "topics":('list','set','tuple'),
   "age":22,

}
print(student)

# data={
#     "name":"satyam",
#     "dept":"CSE",
#     "course":"Python full stack",
#     101:5000
# }

# print(data["name"])
# print(data[101])
# print(data["course"])

# data["duration"]="5+1"
# data["duration"]="6+2"
# print(data["duration"])

# data[102]=1000
# data.setdefault(102,800)
# print(data)

# print(len(data))
# print(data.get(101,0))
# data.pop("name")-- pass atleat one argument
# data.popitem()-- last data delete karta h

# print(data.keys())
# print(data.values())
# print(data.items())


    # Set -->

# set-{} --> Hetrogenous

# unique 
# duplicate value not allowed 
# Indexing not allowed 
# unordered data deta hai
# Multiple value 

data = {2,5,7,1,5,3,4,18}
# print(type(data))

# To add data in set

# data.add(100)
# print(data)

# data.update([2,5,8])

# To remove data from set

# data.pop()

# data.remove(18)

# data.discard(180)

# data.clear()
# del data



x={2,4,5,3}
y={1,3,2,8}

# x=x.union(y)
# print(x)

# intersection - jo jo common hoga dono me

# x=x.intersection(y)
# print(x)

x=x.difference(y)
print(x)

y=y.difference(x)
print(y)

x=x.symmetric_difference(y)
print(x)




