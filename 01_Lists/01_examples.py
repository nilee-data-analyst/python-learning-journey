
# Creating a List
cities = ["Amsterdam", "Rotterdam", "Utrecht", "Zwolle"]
print(cities)

# Accessing Items
print(cities[0])
print(cities[-1])

# Slicing
print(cities[1:3])

# Change Item
cities[1] = "Almere"
print(cities)

# Append
cities.append("Delft")
print(cities)

# Insert
cities.insert(2, "Gouda")
print(cities)

# Remove
cities.remove("Almere")
print(cities)

# Pop
cities.pop()
print(cities)

# Loop
for city in cities:
    print(city)

# Length
print(len(cities))

# Sort
numbers = [50, 10, 40, 20]
numbers.sort()
print(numbers)

# Reverse
numbers.reverse()
print(numbers)

# Copy
copy_list = cities.copy()
print(copy_list)

# Join Lists
list1 = [1, 2]
list2 = [3, 4]

list3 = list1 + list2

print(list3)
