
# create a Tuple
countries = ("India", "Netherlands", "USA", "Canada", "Germany")
print(countries)

# access Items
print(countries[0]) # first element
print(countries[-1]) # last element

# slicing
countries = ("India", "Netherlands", "USA", "Canada", "Germany")
print(countries[:3]) # first three element
print(countries[-2:]) # last two element
print(countries[2:4]) # third and fourth element

# tuple length
fruits = ("apple", "banana", "cherry", "kiwi")
print(len(fruits))

# update tuple
# tuples are immutable. So to add or remove items convert tuple into a list
fruits = ("apple", "banana", "cherry", "kiwi")
x = list(fruits)
x.append("mango")
fruits = tuple(x)
print(fruits)

#index method
print(fruits.index("kiwi"))

# count method
fruits = ("apple", "banana", "cherry", "kiwi", "apple")
print(fruits.count("apple"))

# unpack tuple
num = (10, 20, 30)
num1 , num2, num3 = num
print(num1)
print(num2)
print(num3)

#loop tuple
fruits = ("apple", "banana", "cherry", "kiwi")

for fruit in fruits:
    print(fruit)



