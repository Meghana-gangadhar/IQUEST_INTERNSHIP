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
for x in range(1,6,2):          #start stop step
    print(x,end=" ") 