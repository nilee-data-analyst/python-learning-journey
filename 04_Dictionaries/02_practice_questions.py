
# create and print dictonary
mydict = {"name":"Nilee","age":34,"country":"India"}
print(mydict)

# create a dictionary of five fruits and their prices
fruits = {"apple":30, "banana":20, "cherry":60, "kiwi":40, "mango":100}

# print the price of Mango
print(fruits["mango"])

# update the price of Apple
fruits["apple"] = 50

# add a new key
fruits["orange"] = 90

# delete the Banana
fruits.pop("banana")

print(fruits)

# loop through the dictionary and print
for fruit,price in fruits.items():
    print(fruit,":",price)

# count how many students scored above 80
marks = {
    "Amit":75,
    "Rahul":90,
    "John":82,
    "Nilee":95,
    "Sneha":65
}
count = 0
for score in marks.values():
    if score > 80:
        count+=1
print("students scoring above 80:", count)

# find the student with the highest marks
highest_student = max(marks, key=marks.get)
print("student with highest marks:", highest_student)
print("marks:", marks[highest_student])

# calculate the average marks
avg_marks = sum(marks.values())/len(marks)
print("average marks:", avg_marks)

# print only the student names
for student in marks:
    print(student)

# count how many products cost more than 500.
products = {
    "Laptop":800,
    "Mouse":25,
    "Monitor":300,
    "Phone":950,
    "Keyboard":75
}

count = 0
for cost in products.values():
    if cost > 500:
        count += 1
print("products cost more than 500:", count)

# total cost of products
total = 0
for price in products.values():
    total += price
print("total value of products:", total)

# print only products cheaper than 100
for product,price in products.items():
    if price < 100:
        print(product)

'''
Create a dictionary of employee salaries.
Increase every salary by 10%.
'''
employees = {
    "Amit" : 50000,
    "Rahul" : 60000,
    "John" : 70000
    }

for employee in employees:
    employees[employee] = employees[employee] * 1.10
print(employees)

# check whether the key "Python" exists
skills = {
    "Excel":1,
    "SQL":2,
    "Power BI":3
}

if "python" in skills:
    print("python exists")
else:
    print("python does not exists")

# Reverse the dictionary
data = {
    "A": 1,
    "B": 2
}

reverse = {}

for key, value in data.items():
    reverse[value] = key
print(reverse)
