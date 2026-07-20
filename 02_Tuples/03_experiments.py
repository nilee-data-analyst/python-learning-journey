
# modifying tuple will throw error
fruits = ("Apple", "Banana", "Mango")

fruits[1] = "orange" # throws error
print(fruits)

# modify tuple by converting it to a list
fruits = ("Apple", "Banana", "Mango")
print("original tuple:", fruits)

fruits_list = list(fruits)
fruits_list.append("orange")

fruits = tuple(fruits_list)

print("updated tuple:", fruits)

# check if a tupple can contain duplicate values
nums = (10, 20, 30, 40, 10, 20, 50, 10)

print(nums)
print("count of 10:", nums.count(10))
print("count of 20:", nums.count(20))
