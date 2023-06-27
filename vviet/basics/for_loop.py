'''
Created on 25-Jun-2023

@author: Asus

for loop:
for x in range(1,6):
print(x)
'''
print('initialize with 2',end=" ")
for x in range(2,6):
    print(x,end=" ")
print('not initialized',end=" ") 
for x in range(6):
    print(x,end=" ")   
print('skipping 1 value in between',end=" ")
for x in range(1,6,2):
    print(x,end=" ")
    
'''line=6
for x in range(line):
    for y in range(x):
        print('*' ,end=" ")
    print(' ')

print('-----') 
n=5
m=n-1
for i in range(0,n):
    for j in range(0,m):
        print(end=" ")
        m=m-1
    for j in range(0,i+1):
            print('*',end=" ")
    print(' ')  
        
for i in range(1,6):
    for j in range(i):
        print("*", end=" ")
    print()
    
print('----------')    
for i in range(1,6):
    for j in range(6-i):
        print(" ", end="")
    for j in range(i):
        print("*", end=" ")
    print(' ') 

print('----------')

for i in range(1,6):
    for j in range(6 - i):
        print('*', end=' ')
    print(' ')
    
    
    

print('--------------')
for i in range(1, 4+1):
    for j in range(4 - i):
        print(' ', end=' ')
    for k in range(2 * i - 1):
        print('*', end=' ')
    print()     
for i in range(1, 4+1):
    # printing spaces
    for j in range(i-1):
        print(' ', end=' ')
    # printing stars
    for j in range(2*(4-i)+1):
        print('*', end=' ')
    print() 
print('--------------')
for i in range(1, 4+1):
    # printing spaces
    for j in range(i-1):
        print(' ', end=' ')
    # printing stars
    for j in range(2*(4-i)+1):
        print('*', end=' ')
    print() 
for i in range(1, 4+1):
    for j in range(4 - i):
        print(' ', end=' ')
    for k in range(2 * i - 1):
        print('*', end=' ')
    print()
print("-------------") 
for i in range(1, 4+1):
    # printing spaces
    for j in range(i-1):
        print(' ', end=' ')
    # printing stars
    for j in range(2*(4-i)+1):
        print('*', end=' ')
    print()  
print("---------------")    
for x in range(5,-1,-1):
    print("*"*x)
print("-----------")
'''


