
# 1. Print Numbers (for loop)
# Write a program to print numbers from 1 to 10 using a for loop.
print("SOLUTION 1: \n")
for i in range(1,11):
    print(i)


print("\n")
print("-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x- \n")    


# 2. Sum of Numbers (while loop)
# Find the sum of first 10 natural numbers using a while loop.
print("SOLUTION 2:\n")
a = 1
sum = 0
while a<=10:
    sum += a
    a += 1
print("sum of first 10 natural numbers:", sum)


print("\n")
print("-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x- \n")  


# 3. Multiplication Table (for loop)
# Take a number as input and print its multiplication table up to 10
print("SOLUTION 3:\n")
num = int(input("Enter a number for multiplication Table: "))
print("Multiplication Table of", num)

for i in range (1,11):
    print(num,"*",i,"=",num*i)


print("\n")
print("-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x- \n")  

# 4. Factorial (while loop)
# Find the factorial of a number using while loop
print("SOLUTION 4:\n")
num2 = int(input("Enter a number to find its factorial: "))
factorial = 1
i = 1
while i <= num2:
    factorial *= i
    i += 1  
print("Factorial of", num2, "is", factorial)


print("\n")
print("-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x- \n")  

# 5. Reverse a Number (while loop)
# Take an integer as input and reverse its digits (eg: 123 -> 321)
print("SOLUTION 5:\n")
num3 = int(input("Enter a number to reverse: "))
reverse = 0
while num3 > 0:       
    last = num3 % 10
    reverse = (reverse*10) + last
    num3 //= 10
print("Reverse is",reverse)


print("\n")
print("-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x- \n")  

# 6. Even numbers (for loop with range)
# Print all even numbers between 1 and 50
print("SOLUTION 6:\n")
for i in range(1,51):
    if i%2==0:
        print(i)


print("\n")
print("-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x- \n")  

# 7. Sum of digits (while loop)
# Take a number as input and find the sum of its digits
print("SOLUTION 7:\n")
num5 = int(input("enter: "))
sum = 0
while num5 > 0:
    sum = sum+(num5%10)
    num5 = num5//10    
print(sum)


print("\n")
print("-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x- \n")  

# 8. Fibonacci Series (for loop)
# Print the first 10 terms of the fibonacci sequence
print("SOLUTION 8:\n")  
a = 0
b = 1

for i in range(10):
    print(a)
    c = a + b
    a = b
    b = c