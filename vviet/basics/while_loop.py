'''
Created on 02-Jul-2023

@author: Asus
break: to come out of the loop after reaching certain condition
continue: to skip the condition
'''
'''
n=int(input('enter a number'))
factorial=1
while(n<0):
    print('enter a valid number')
    n=int(input('enter a number')
    if n==0:
        print('the factorial of 0 is 1')
    else:
        for i in range(1,n+1)
            factorial=factorial*i
        print('the factorial of',n,'is',factorial)
n=0
while n<10:
    if n%2==0:
        continue
    if n>6:
        break
    print(n)
while n>1:
    if n%2==1:
        continue
    print(n)
    '''
    
for x in range (8):
    
    if x%2==0:
        print(x*2)
        continue
    else:
        print(x)