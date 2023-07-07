'''
Created on 02-Jul-2023

@author: Asus
'''

a = [1, 2, 3, 2, 1, 3, 4, 5, 1, 2, 4, 3]
b = []

# Loop through the list and count occurrences
for x in a:
    if x not in b:
        b.append(x)
        count = a.count(x)
        print(x ,":",count)
print('--------------------------------------')      


def fact(n):
    factorial = 1
   
    for i in range(1, n + 1):
        factorial *= i
    return factorial

while True:
    try:
        n = int(input("Enter a number: "))
        if n < 0:
            raise ValueError("Factorial is not defined for negative numbers.")
        a = fact(n)
        print("The factorial of ", n," is" ,a)
    except ValueError as ve:
        print( ve)
    except Exception as e:
        print( e)
 
print("-------------------------")

def fs(n):
    fs = [0, 1]
    while len(fs) < n:
        fs.append(fs[-1] + fs[-2])
    return fs
    
while True:
    try:
        n = int(input("Enter anumber : "))
        if n< 0:
            raise ValueError("Negative numbers do not have fs")
        elif n==0:
            raise ValueError('fs of  is 0')
        fib_seq = fs(n)
        print( 'fs ',fib_seq)
    except ValueError as ve:
        print( ve)
    except Exception as e:
        print( e)
        
s1=('a','m')
s2=('c','c')
s3=s1+s2
print(s3)
for i in range(5,0,-1):
    print(i)
list=[80,90,100,120]
print(list[::-2])