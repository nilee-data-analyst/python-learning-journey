
# create a set and check type
fruits = {"apple", "banana", "cherry", "kiwi"}
print(fruits)
print(type(fruits))

# access a set
'''
sets are unordered. So sets are not accessible by referring to an index or a key.
but set items can be loop through using a for loop.
'''
for fruit in fruits:
    print(fruit)

#add and remove set item
'''
once a set is created , set items can not be changed.
but we can add and/or remove items in a set.
'''
fruits.add("mango") #add an item
print(fruits)

fruits.remove("apple") #remove an item
fruits.discard("kiwi") #discard and item
fruits.pop() #remove an return an item
print(fruits)

# join sets
set1 ={1, 2, 3, 4, 5}
set2 = {"a", "b", "c"}
set3 = {"apple", "banana"}

# union and update method (can use '|' operator so join one set to multiple sets instead of union() method)
mainset = set1.union(set2, set3) # can use | operator so join one set to multiple sets
print(mainset)

set1.update(set2, set3) # update method inserts the items from set2 and set3 into set1
print(set1)

# intersection method ( can use '&' operator instead of intersection() method)
set1 = {1, 2, 3, 4, 5}
set2 = {3, 4}

set3 = set1.intersection(set2) # keeps ONLY the duplicates from both sets
print(set3)

# difference method (can use '-' operator instead of intersection() method)
set1 = {1, 2, 3, 4, 5}
set2 = {3, 4}

set3 = set1.difference(set2) #  keeps the items from the first set that are not in the other set(s)
print(set3)

# symmetric_difference (can use '^' operator instead of symmetric_difference() method)
set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 6, 7}

set3 = set1.symmetric_difference(set2) # keep only the elements that are NOT present in both sets
print(set3)


