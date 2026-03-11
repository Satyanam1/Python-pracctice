

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

l=[1,2,3,4,5]
def add (sum,x):
    return sum+x
res=reduce(add,l)
res=reduce(add,l,0)
print(res)
