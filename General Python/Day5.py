# SETS

# Basic Set Creation and Access

# 1 Create a set of 5 colors and print it. 
color = {"red", "green", "blue", "yellow", "purple"}
print(color)


# 2 Create a set of numbers with duplicates and check how Python handles duplicates. 
nums = {1, 2, 3, 4, 4, 4, 5, 5, 6}
print(nums)  


# 3 Write a program to loop through a set and print each element
set1 = {"apple", "banana", "cherry", "date"}
for i in set1:
    print(i)

# Adding and Removing Elements

# 4 Create a set and use .add() to insert a new element
set2 = {"apple", "banana", "cherry"}
set2.add("orange")
print(set2)


# 5 Remove an element using .remove() and observe what happens if the element is not present. 
set3 = {"apple", "banana", "cherry", "date"}
set3.remove("orange") 
print(set3)


# 6 Remove an element using .discard() and compare it with .remove()
set4 = {"apple", "banana", "cherry", "date"}
set4.discard("banana")
set4.discard("orange")
print(set4)


# 7 Use .pop() to remove a random element from a set. 
set5 = {1,2,3,4,5,6,7}
set5.pop()
print(set5)


# Set Operations

# 8 Create two sets and find their union. 
set6 = set5.union(set4)
print(set6)


# 9 Create two sets and find their intersection. 
set7 = set6.intersection(set5)
print(set7)

# 10 Create two sets and find their difference (A − B). 
a = {1,2,3}
b = {1,2}
diff = a - b
print(diff)


# Other Methods 

# 11 Use .copy() to create a copy of a set and modify the copy. 
copySet = set4.copy()
copySet.add("guava")
print("Origianl set:", set4)
print("Copy Set modified:",copySet)


# 12 Use .clear() to empty a set. 
s = {1,2,3,4,5}
print(s.clear())


# 13  Convert a list with duplicates into a set to remove duplicates. 
l = [1,2,3,4,5,5,5,6]
c = set(l)
print(c)


# Applications 

# 14 Write a program to find all unique characters in a string using a set. 
str = input("Enter a string: ")
converted_set = set(str)
print("Unique characters in string: ", converted_set)


# 15 Given two lists of students (cricket and football), find students who play both sports (intersection). 
cric_list = ["Shobhit", "Rudra", "Abhishek", "Amandeep", "Vansh"]
foot_list = ["Shivam", "Vansh", "Abhishek", "Shobhit", "Abhikalp"]
common = set(cric_list).intersection(set(foot_list))
print("common players: ", common)


# 16 Given two lists of students, find students who play only cricket (difference). 
only_cricket = set(cric_list) - set(foot_list)
print("only cricket: ", only_cricket)


# 17 Take a sentence as input and print all unique words using a set.
sent = input("Enter a sentence: ")
print(set(sent.split()))


# 18 Write a program to check if two sets are equal (ignoring order).
s1 = {1,2,4,5}
s2 = {1,2,3,5}
if s1 == s2:
    print("equal")
else: 
    print("not equal")


# 19  Create two sets and check if they have at least one element in common (hint: use intersection). 
s1 = {1,2,3,4}
s2 = {4,5,6,7}
if (s1.intersection(s2)):
    print("commmon: ",s1.intersection(s2))
else:
    print("not common")


# 20  Write a program to find the number of unique elements in a list using a set.
sent = [1,2,3,4,4,4,5,6]
print(set(sent)) 