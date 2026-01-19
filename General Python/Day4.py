
# 1 create a list of 5 numbers, print the first element, last element and length of the list
l = [1,2,3,4,5]
print(l[0], l[-1], len(l))

# 2 take a list of numbers, and find the sum and average using built-in functions.
l2 = [10,20,30,40,50]
print(sum(l2))
avg = sum(l2)/len(l2)
print(avg)


# 3 create a list of fruits, add a new fruit using .append() and insert one at position 2 using .insert()
fruits = ["banana", "apple", "kiwi", "cherry"]
fruits.append("pineapple")
fruits.insert(2,"mango")
print(fruits)


# 4 remove an element from a list using .remove() and delete the last element using .pop()
fruits.remove("banana")
fruits.pop()
print(fruits)


# 5 create a list with duplicate numbers. use .count() to check how many times a number appears
l3 = [1,1,1,1,2,2,2,3,3,3,4,4,5,6,7,8,9]
print("1 is present: ",l3.count(1), "times")
print("3 is present: ",l3.count(3), "times")


# SEARCHING AND SORTING
# 6 write a program to check if a number exists in a list or not
l4 = [1,2,3,4,5,6,100]
if 100 in l4:
    print("yes, it exists")
else:
    print("it doesn't")

# 7 
