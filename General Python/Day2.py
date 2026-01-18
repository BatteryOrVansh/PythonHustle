# PRACTICE PROBLEMS

# 1  Write a program that takes two numbers as input and prints their sum, difference, product, and quotient. 
num1 = int(input("Enter number 1; "))
num2 = int(input("Enter number 2; "))
add = num1 + num2
diff = num1 - num2
prod = num1 * num2
quot = num1/num2
print("sum :", add)
print("difference :", diff)
print("product :", prod)
print("quotient :", quot)


# 2 Given a = 15 and b = 4, print:
# ◦ The floor division (a // b)
# ◦ The remainder (a % b)
# ◦ The power (a ** b) 
a = 15
b = 4
print("Floor Division: ", a//b)
print("Remainder : ", a%b)
print("Exponent : ", a**b)


# 3 A shopkeeper sells a pen for ₹15 and a notebook for ₹40. Write a program to calculate the total cost if a student buys 3 pens and 2 notebooks. 
pen = 15
nb = 40
total = (3*pen) + (2*nb)
print(total)


# 4 Write a program to calculate the average of 5 numbers entered by the user.
num1 = float(input("Enter number: "))
num2 = float(input("Enter number: "))
num3 = float(input("Enter number: "))
num4 = float(input("Enter number: "))
num5 = float(input("Enter number: "))
avg = (num1 + num2 + num3 + num4 + num5)/5
print(avg)


# 5 Write a program that asks for a number and prints:
# ◦ Its square (n ** 2)
# ◦ Its cube (n ** 3)
# ◦ Its square root (using n ** 0.5)
num = int(input("Enter a num: "))
sq = num2
cube = num3
sqrt = num**0.5
print("Square :", sq)
print("Cube:", cube)
print("Square Root:", sqrt)


# 6  Write a program to convert total seconds entered by the user into minutes and seconds (Hint:Use // and %). 
sec = int(input("Enter total number of seconds: "))
hrs = sec//60
mint = sec%60
print("Time in Hrs and Minutes:", hrs, "Hours ", mint, "minutes")


# 7 A car travels 120 km in 3 hours. Write a program to calculate its average speed (distance ÷ time). 
dist = 120
time = 3
avg_speed = dist/time
print("Avergae Speed:", avg_speed)


# 8 Write a program that asks the user for two integers and prints whether the first number is a multiple of the second number (using %).
num1 = int(input("Enter number 1:"))
num2 = int(input("Enter number 2:"))
if num1%num2==0:
	print(num1, "is a multiple of", num2)
else:
	print(num1, "isn't a multiple of", num2)


# 9 Write a program to calculate the simple interest given:
# ◦ Principal (P)
# ◦ Rate of Interest (R)
# ◦ Time (T) in years
# Formula: SI = (P * R * T) / 100 
prin = 1000
roi = 5
time = 3
SI = (prin * roi * time)/100

print("Simple Interest is: ", SI)


# 10 Write a program that takes two floating-point numbers as input and prints their rounded quotient (using // for floor division). 
num1 = float(input("Enter first float: "))
num2 = float(input("Enter second float: "))
print("Rounded Quotient of both number is:", num1//num2)

