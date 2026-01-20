# LISTS OF DICTIONARIES 
print("\n")
print("-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x- \n")  
print("LISTS OF DICTIONARIES")
print("-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x- \n") 

# 1. Create a list of 3 dictionaries, each containing student "name" and "age". 
print("SOLUTION 1:\n") 
student = [
    {"name": "Vansh", "age": 20},
    {"name": "Rahul", "age": 21},
    {"name": "Neha", "age": 19}
]
print(student)


print("\n")
print("-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x- \n")  

# 2. Print the name of the first student. 
print("SOLUTION 2:\n") 
print("name of the first student: ", student[0]["name"])


print("\n")
print("-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x- \n")  

# 3``. Loop through the list and print all student names.
print("SOLUTION 11:\n") 
for i in student:
    print(i["name"])


print("\n")
print("-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x- \n")  

# 4. Add a new dictionary {"name": "Priya", "age": 21} to the list
print("SOLUTION 4:\n") 
student.append({"name": "Priya", "age": 21})
print(student)


print("\n")
print("-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x- \n")  

# 5. Update "Rahul"’s age to 20
print("SOLUTION 5:\n") 
for i in student:
    if i["name"] == "Rahul":
        i["age"] = 20
        break

print(student)


print("\n")
print("-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x- \n")  

# 6. Remove "Neha" from the list. 
print("SOLUTION 6:\n") 
for i in student:
    if i["name"] == "Neha":
        student.remove(i)
        break
print(student)


print("\n")
print("-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x- \n")  

# 7. Find the oldest student from the list. 
print("SOLUTION 7:\n")
oldest = student[0]
for individual in student:
    if individual["age"] > oldest["age"]:
        oldest = individual
print("oldest student: ", oldest)


print("\n")
print("-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x- \n")  

# 8.  Print all students whose age is greater than 20
print("SOLUTION 8:\n")
for i in student:
    if i["age"] > 20:
        print(i)


print("\n")
print("-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x- \n")  

# 9. Convert this list of dictionaries into just a list of names. 
print("SOLUTION 9:\n") 
for i in range(len(student)):
    student[i] = student[i]["name"]

print(student)
    

print("\n")
print("-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x- \n")  

# 10.  Sort the list of dictionaries by age. 
print("SOLUTION 10:\n") 
student = [
    {"name": "Vansh", "age": 20},
    {"name": "Rahul", "age": 21},
    {"name": "Neha", "age": 19}
]
student.sort(key = lambda x : x["age"])
print(student)
