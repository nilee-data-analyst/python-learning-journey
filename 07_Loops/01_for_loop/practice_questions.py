# Print all numbers from 1–50
for num in range(1,51):
    print(num)

# Print only even numbers
for num in range(2, 51, 2):
    print(num)

# Print squares from 1–10
for num in range(1,11):
    print(num ** 2)

# Print cubes from 1–10
for num in range(1,11):
    print(num ** 3)

# Calculate factorial of a number
num = int(input("Enter a number: "))

factorial = 1

for i in range(1, num + 1):
    factorial = factorial * i

print("Factorial:", factorial)

# Find the sum of all numbers
numbers = [12,18,25,40,60]

total = 0

for num in numbers:
    total = total + num
print(total)

# Find the largest number in a list
numbers = [12,18,25,40,60]

largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

print("Largest number:", largest)

# Count vowels in "Data Analytics"
text = "Data Analytics"

count = 0

for char in text:
    if char.lower() in "ariou":
        count+=1
print("Vowels: ", count)

# Print each word separately
sentence = "Python is powerful"

words = sentence.split()

for word in words:
    print(word)

# Count names starting with "A"
names = [
    "Amit",
    "John",
    "Alice",
    "Nilee",
    "Andrew"
]

count = 0

for name in names:
    if name.startswith("A"):
        count += 1

print(count)

# Print pattern
for i in range(1, 6):
    print("*" * i)

# reverse the above pattern
for i in range(5, 0, -1):
    print("*" * i)