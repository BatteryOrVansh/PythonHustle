# 1 Print all num from 1 to 50 that are divisible by 3 using a for loop
for i in range(1, 50):
    if(i%3==0):
        print("Divisible by 3: ", i)
    
# 2 Use a while loop to compute the factorial of a number entered by the user
x = int(input("Enter a number to know its factorial: "))
y = 1
while(x>1):
    y = y*x
    x = x-1
print("The factorial is : ", y)


    