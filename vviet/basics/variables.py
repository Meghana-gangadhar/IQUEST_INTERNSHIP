'''
Created on 25-Jun-2023

@author: Asus
variables: these are containers for storing data values
'''

#three ways of variable declaration
c=x=1        #single value can assign to several variables
a="h"       #string variable assignment
k=9.88      #floating point variable
b,n=2 ,6    #integer assignment for 2 variables
#to add two variables
print(c+b)    
#to get variable type     
print(type(a))
print(type(b))
print(type(c))
print(type(k))
#just to print
print(x)
print(c)
print(b)
print(n)
#to  get memory location we use id()
print(id(a))
print(id(b))
print(id(n))
#we declared c=x=1 so the memory location is same
print(id(c))
print(id(x))
d=1
print(id(d))
''' multiple line comment'''
#single line comment