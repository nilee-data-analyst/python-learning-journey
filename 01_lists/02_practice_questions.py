
# access list items
fruits = ["apple", "banana", "mango", "grapes", "orange"]
print(fruits[0])   # first
print(fruits[-1])  # last
print(fruits[2])   # 3rd item

# print only even index items
nums = [1,2,3,4,5,6,7,8,9]

for i in range(len(nums)):
    if i % 2 == 0:
        print(nums[i])

# change List Items
# Replace all numbers greater than 50 with 0
nums = [10, 60, 70, 30]

for i in range(len(nums)):
    if nums[i] > 50:
        nums[i] = 0

print(nums)

# add List ItemsS
# Take 5 inputs from user and store in list
nums = []

for i in range(5):
    value = input("Enter value: ")
    nums.append(value)

print(nums)

# remove List Items
fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")
print(fruits)

# pop
fruits = ["apple", "banana", "cherry"]
fruits.pop()
print(fruits)

# Loop Lists
animals = ["cat", "dog", "lion", "tiger"]
for animal in animals:
    print(animal)

# loop through a given condition
animals = ["cat", "dog", "lion", "tiger"]

for animal in animals:
    if "a" in animal:
        print(animal)

# find square of a given list with list Comprehension
squares = [i*i for i in range(1, 11)]
print(squares)

# Copy Lists
list1 = [1, 2, 3]
copy_list = list1[:]
print(copy_list)

# Join Lists with loop
a = [1,2,3]
b = [4,5,6]

for i in b:
    a.append(i)
print(a)

# Find Largest Number
numbers = [10, 45, 3, 99, 22]
largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num
print("Largest number:", largest)

# Find Smallest Number
numbers = [10, 45, 3, 99, 22]
smallest = numbers[0]

for num in numbers:
    if num < smallest:
        smallest = num
print("Smallest number:", smallest)

# Sum of List
numbers = [1, 2, 3, 4, 5]
total = 0

for num in numbers:
    total = total + num
print("Sum:", total)

# Remove Duplicate Values
numbers = [1, 2, 2, 3, 1, 4, 4, 5]
unique = []

for num in numbers:
    if num not in unique:
        unique.append(num)
print("Without duplicates:", unique)

# count votes
votes = ["yes", "no", "yes", "yes", "no"]

yes_count = votes.count("yes")
no_count = votes.count("no")

print("Yes:", yes_count)
print("No:", no_count)
