
# Does a Set Allow Duplicate Values?
numbers = {10, 20, 30, 20, 10, 40, 50}

print("Set:", numbers)
print("Length:", len(numbers))

# Difference Between remove(), discard() and pop()
animals = {"Dog", "Cat", "Rabbit"}

print("Original Set:", animals)

try:
    animals.remove("Lion") # remove gives error if try to remove anitem that is not present in a set
except KeyError as error:
    print("remove() Error:", error)

animals.discard("Lion") # does nothing if an item is not present in a set
print("After discard():", animals)

print(animals.pop()) # remove an item, but this method will remove a random item, so you cannot be sure what item that gets removed

# Adding a Duplicate Value
fruits = {"Apple", "Banana", "Mango"}
print("Before:", fruits)

fruits.add("Banana")
print("After:", fruits)



