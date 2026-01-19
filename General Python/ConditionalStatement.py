# 1. Write a program to check if a number is positive, negative, or zero.
x = int(input("Enter a number: "))
if x > 0:
    print("It is positive")
elif x < 0:
    print("It is negative")
else:
    print("It is zero")

# 2. Write a program to check if a person is eligible to vote based on their age (age >= 18).
x = int(input("Enter your age: "))
if x >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")

# 3. Write a program to check if a number is even or odd.
n = int(input("Enter the number: "))
if n % 2==0 :
    print("It is even")
else:
    print("It is odd")

# 4. Write a program to compare two numbers and determine which one is greater or if they are equal.
t1 = int(input("Enter the number 1: "))
t2 = int(input("Enter the number 2: "))
if t1 > t2:
    print(t1,"is greater than",t2)
elif t2 > t1:
    print(t2,"is greater than",t1)
else:
    print("both are equal")

# 5. Write a program to check if a number is divisible by 5.
m = int(input("Enter the number: "))
if m % 5==0 :
    print("It is divisible by 5")
else:
    print("It is not divisible by 5")

# 6. Write a program to assign grades based on student marks (A: >=90, B: >=75, C: >=60, Fail: <60).
stu = int(input("Enter students marks: "))
if stu >= 90:
    print("Grade A")
elif stu >= 75:
    print("Grade B")
elif stu >= 60:
    print("Grade C")
else:
    print("Fail")

# 7. Write a program to check if a given year is a leap year.
year = int(input("Enter your year: "))
if year%4==0 and year%400==0:
    print("Leap Year")
else:
    print("Not a leap year")

# 8. Write a program to check if a number is single digit, double digit, or more than 2 digits.
h = int(input("Enter a digit: "))
if h>99:
    print("More than 2 digits")
elif h>10:
    print("Double digits")
else:
    print("Single digit")

# 9. Write a program to print the day of the week based on a number (1-7).
day = int(input("Enter Day number: "))
if day == 1:
    print("Monday")
elif day == 2:
    print("Tuesday")
elif day == 3:
    print("Wednesday")
elif day == 4:
    print("Thursday")
elif day == 5:
    print("Friday")
elif day == 6:
    print("Saturday")
elif day == 7:
    print("Sunday")
else:
    print("enter a valid day number")

# 10. Write a program to categorize temperature as Freezing (<=0), Cold (1-20), Warm (21-35), or Hot (>35).
temp = int(input("Enter a temp: "))
if temp<=0:
    print("Freezing")
elif temp>0 and temp<=20:
    print("Cold")
elif temp>=21 and temp<=35:
    print("Warm")
else:
    print("Hot")