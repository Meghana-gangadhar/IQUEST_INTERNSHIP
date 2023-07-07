'''
Created on 02-Jul-2023

@author: Asus
1.define : using{}, built in function set --set(range(6))
2.do not accept duplicate values , heterogeous (we can store any datatype)
3. I can create empty list just by using set()
4.can't access: index and slicing
5.can't reverse list:using -1 as step in slicing operator
6.sets are immutable (cannot change the value once assigned)
7. we can store fixed object in a sets 
8.we can't add two sets
'''
a={10,2,3,4,5,'ff'}
print(a)
print(type(a))
b={1,2,3,3,4,4,3,5,5,6,2}
print(b)
print(type(b))
c={}
print(c)
print(type(c))
d=set()
print(d)
print(type(d))
e=set(range(0,10))
print(e)
print(type(e))
print(len(a))
a.add(32)
print(a)
for x in a:
    print(x)
a.remove(4)
print(a)

ab={1,2,3,4,5,6,7,8,9}    
bdd=[x for x in ab if x%2 == 0]
print('comprahension',bdd)

#print(b*2)      #TypeError: unsupported operand type(s) for *: 'set' and 'int'
#print(b+b)      #TypeError: unsupported operand type(s) for +: 'set' and 'set'


