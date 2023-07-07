'''
Created on 02-Jul-2023

@author: Asus
1.define : using(), built in function tuple --tuple(range(6))
2.accept duplicate values , heterogeous (we can store any datatype)
3. I can create empty list
4.access: index and slicing
5.reverse list:using -1 as step in slicing operator
6.tuple are immutable (cannot change the value once assigned)
7. we can store fixed object in a tuple 
8.we can add two tuples
9.we can't subtract two tuples

'''
a=(1,2,3,4,4,3,5,6)
b=tuple(range(0,6))
c=()
d=(11,33,44,'fe')
print(id(a))
print(a)
print(c)
print(type(a))
print(type(b))
print(type(c))
print(type(d))
#accessing through index
print(a[1])
#slicing operator
print(a[3:2])
print(a[::-1])
#to add new value to the tuple
a=a+(40,)
print(a)
print(len(a))
print(a.count(4))
print(id(a))
for x in a:
    print(x)
    
ab=(1,2,3,4,5,6,7,8,9)    
bdd=[x for x in ab if x%2 == 0]
print('comprahension',bdd)

print(a+b)      #extension happens
#print(a*b)      #TypeError: can't multiply sequence by non-int of type 'tuple'
print(a*2)
#print(a+2)      #TypeError: can only concatenate tuple (not "int") to tuple
#print(a-b)      #TypeError: can only concatenate tuple (not "int") to tuple
print(8 in a)
print(8 not in a)
print(4 in a)
print(4 not in a)