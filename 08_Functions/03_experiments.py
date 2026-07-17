
# print() vs return() : print() displays the result & return sends the result back to the caller
def add1(a, b):
    print(a + b)

result = add1(10, 20)

print(result)
#-------------------------------------------
def add2(a, b):
    return a + b

result = add2(10, 20)

print(result)

# Local vs Global Scope : "Global" keyword change the name in local scope
name = "Nilee"

def change_name():
    name = "Rahul"
    print("Inside:", name)

change_name()

print("Outside:", name)
#-------------------------------------------
name = "Nilee"

def change_name():
    global name
    name = "Rahul"

change_name()

print(name)

# Lambda vs Normal Function : lambda function is shorter
def square(number):
    return number ** 2

print(square(5))
#----------------------------------------------
square = lambda number: number ** 2

print(square(5))