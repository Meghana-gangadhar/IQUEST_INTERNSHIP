'''
Created on 27-Jun-2023

@author: Asus
'''
for x in range(5,0,-1):
    print("*"*x)
print("-----------")
for x in range(1, 6):
    print("*" * x)
print("-----------")
for i in range(4):
    print(" " * (4 - i - 1) + "*" * (2 * i + 1))
print("-----------")
for i in range(4, 0, -1):
    print(" " * (4 - i) + "*" * (2 * i - 1))
print("-----------")
for i in range(6, 0, -1):
    for j in range(6, i-1, -1):
        print(j, end=" ")
    print()
print("-----------")
for i in range(1, 7):
    for j in range(6, i-1, -1):
        print(j, end=" ")
    print()
print("-----------")
'''numbers = [1, 2, 3, 5, 6]
for i in range(len(numbers)):
    for j in range(i + 1):
        print(numbers[j], end=" ")
    print()
'''
for i in range(1, 7):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
print("-----------")

import string

for i in range(1, 6):
    for j in range(1, i + 1):
        print(string.ascii_uppercase[j-1], end=" ")
    print()
print("-----------")
for i in range(5, 0, -1):
    print("*" * i)

for i in range(1, 6):
    print("*" * i)
print('----------') 
factorial = 1

for i in range(1, 4 + 1):
    factorial *= i
    print(factorial ,end=' ')
print()
print('------------')

fs = [0, 1]

for i in range(2, 10):
    next_number = fs[i-1] + fs[i-2]
    fs.append(next_number)

for number in fs:
    print(number,end=' ')
print()
print('------------')