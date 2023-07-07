'''
Created on 02-Jul-2023

@author: Asus

1.define : using[], built in function list --list(range(6))
2.accept duplicate values , heterogenous (we can store any datatype)
3. i can creaate empty list
4.access: index and slicing
5.reverse list:using -1 as step in slicing operator
6.lists are mutable (can change the value once assigned)
7. we cannot store fixed object in a list so we need tuples and sets
8.we can add two lists

1. count the occurance of each element in a given list
'''
a=[1,2,2,2.9,'abc',3,1,2,1,4,9]           #list within square braces
h=[11,2,34,22,55,66,0,88,66]
b=[]                #empty list can possible
c=list(range(6))    #list with range(built in function list
print(a)
print(b)
print(c)
#accessing through index
print(a[0])
#slicing operator
print(c[0:5:2]) 
print(c[::-1])        #start step stop
a[2]=10             #mutable
print(a)
weekdays=['mon','tue','wed','thu','fri','sat','sun']  #user can change the values

print(len(a))           #to print length of list
print(a.count(1))       #to get number of repeated element in list
for x in a:
    print(x)
    
a.append(10)            #adds only a value to the list at the end
print(a)
a.append(c)              #adds whole list to the list at the end
print(a)
a.insert(4, 999)      #to add an element to the list at particular index in list
print(a)
d=a.copy()          #to copy the list and assign the value
print(d)


print(a[13])        #append only adding the entire list as single element
#print(a[14])        #list index out of range
#print(a[13.1])      #list indecies must be integer or sclices, not float
a.extend(c)         #extends the list by adding list element by element at the end
print(a)
print(a[17])
a.pop(5)            #removes the elements according to the index
print(a)
a.remove(999)   #remove the value from list
print(a)
a.reverse()     #reverse the list elements
print(a)
h.sort()            #ascending order
print(h)
h.pop()            #removes the last elements 
print(h)
h.remove(2)     #remove need value
print(h)
print('-----------------')
ab=list(range(0,20))
ba=[]
for num in ab:
    if num%2==0:
        ba.append(num)
print('normal',ba)
print('---------list comprehension--------')
bdd=[x for x in ab if x%2 == 0]
print('comprahension',bdd)
print(8 in a)
print(8 not in a)
print(4 in a)
print(4 not in a)






