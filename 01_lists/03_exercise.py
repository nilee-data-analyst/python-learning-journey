# experimented difference between list1=list2 and real copy

list1 = [1, 2, 3]
list2 = list1

list3 = list1.copy()

list1.append(100)

print(list1)
print(list2)  # same reference
print(list3)  # real copy

# if a list can store different data type by append() method
fruits = ["Apple", "Banana"]

fruits.append(100)
fruits.append(True)

print(fruits) 

# sort in descending order vs reverse
numbers = [5,2,8,1]
numbers.sort(reverse=True) # descending order
print(numbers)

numbers.reverse() # reverse the list
print(numbers)

# index error
fruits = ["Apple","Banana"]
print(fruits[10]) # throws error



