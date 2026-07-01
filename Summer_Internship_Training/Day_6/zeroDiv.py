try:
    numerator = float(input("Enter the numerator: "))
    denominator = float(input("Enter the denominator: "))
    
    # Attempt Division
    result = numerator / denominator
    print(f"The result of {numerator} divided by {denominator} is: {result}")

except ZeroDivisionError:
    # This run only if the user enters 0 as the denominator
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Error: Please enter valid numbers.")