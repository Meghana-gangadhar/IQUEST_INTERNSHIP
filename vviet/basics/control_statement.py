'''
Created on 25-Jun-2023

@author: Asus
'''

'''
flow control:used to control the flow of programs
1.conditional statements:if,if else,nested if else,series if else
2.looping statements:for,while,do while,
3.sequential flow
'''
#to take 2 input values and check its type

a=int(input('enter a value'))
b=int(input('enter b value'))
#we include the int(input()) then the type casting string into integer value 
print(a,b)
print(a+b)
print(type(a))
print(type(b))


#to get largest value from 3 variables

a=int(input('enter a value:'))
b=int(input('enter b value:'))
c=int(input('enter c value:'))

if a>=b and a>=c:
    print('largest',a)
elif b>=c:
    print(' largest',b)
else:
    print('largest',c)


