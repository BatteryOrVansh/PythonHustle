def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b

def floor_div(a,b):
    return a//b

def mod(a,b):
    return a%b

addition = add(10,20)
subtraction = sub(10,20)
multiplication = mul(10,20)
division = div(10,20)
floor_division = floor_div(10,20)
remainder = mod(10,20)

print("Addition of 10 and 20 is: ", addition)
print("Subtraction of 10 and 20 is: ", subtraction)
print("Multiplication of 10 and 20 is: ", multiplication)
print("Division of 10 and 20 is: ", division)
print("Floor Division of 10 and 20 is: ", floor_division)
print("Remainder of 10 and 20 is: ", remainder)


# exponent functions
def square(x):
    print(f"The square of {x} is {x**2}")
    
x = int(input("Enter a num for its square: "))
square(x)


def cube(n):
    print(f"The cube of {n} is {n**3}")

n = int(input("Enter a number for its cube: "))
cube(n)

# Lambda Functions
square = lambda x: x**2
print(square(5))