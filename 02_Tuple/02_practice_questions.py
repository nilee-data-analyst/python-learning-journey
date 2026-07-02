
# print weekdays
weekdays = ("monday", "tuesday", "wednesday", "thursday", "friday")
print(weekdays[0])
print(weekdays[1])
print(weekdays[2])
print(weekdays[3])
print(weekdays[4])

# find index
print(weekdays.index("thursday"))

# Even Numbers
nums = (2, 5, 8, 10, 13, 16, 23, 28, 36, 44, 55, 60)

for num in nums:
    if num%2 == 0:
        if num > 10:
            print(num)

# check item
weekdays = ("monday", "tuesday", "wednesday", "thursday", "friday")
if "wednesday" in weekdays:
    print("yes")
else:
    print("no")   

# count positive numbers
numbers = (-6, 10, 18, 20, 3, -8, 12)
count = 0
for num in numbers:
    if num > 0:
        count += 1
print(count)

# Longest Word in tuple
countries = ("India", "Netherlands", "USA", "Canada", "Germany")

longest_word = max(countries, key = len)
print(longest_word)

# Reverse a Tuple
countries = ("India", "Netherlands", "USA", "Canada", "Germany")
print(countries[::-1])

# join tuples
tuple1 = (1,2,3)
tuple2 = ("a","b", "c")

tuple3 = tuple1 + tuple2
print(tuple3)

# Monthly Sales
sales = (2500, 3200, 2800, 4100, 3900, 5000)

print("Highest:", max(sales)) # highest sale
print("Lowest:", min(sales)) # lowest sale
print("Total:", sum(sales)) # total sales
print("Average:", sum(sales) / len(sales)) # avg sales

# Palindrome Tuple
numbers = (1, 2, 3, 2, 1)

if numbers == numbers[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")

# Second Largest Number
numbers = (15, 8, 40, 22, 30)

unique = sorted(set(numbers))
print(unique[-2])
   



    
 
        