
# function
'''
function is a block of code which only runs when it is called.
function can return data as a result.
function helps avoiding code repetition.
'''
def welcome():
    print("welcom to python")

welcome()

# funtion with one parameter
def greet(name):
    print("welcome to python", name)

greet("Nilee")
greet("John")

# function with multiple parameters
def details(name,country):
    print(name , "lives in", country)

details("Nilee","Netherlands")

# function with return
def add(a,b):
    return a + b

result = add(10,5)
print(result)

# default parameter (If the function is called without an argument, it uses the default value)
def greet(name = "Guest"):
    print("Hello", name)

greet()
greet("Nilee")

# keyword arguments (send arguments with the key = value syntax)
def student(name ,age):
    print(name,age)

student(age = 30, name = "John")

# *args (allows a function to accept any number of positional arguments)
def total(*numbers):
    print(sum(numbers))

total(10,20)
total(10,20,30)
total(10,20,30,40)

# ** kwargs (allows a function to accept any number of positional arguments)
def student(**person):
    print(person)

student(name ="John", country = "India", age = 30)

# lambda function 
square = lambda x: x * x

print(square(6))

# lambda with multiple arguments
total = lambda x,y,z : x+y+z

print(total(5,10,15))

# global scope
country = "Netherlands"

def show():
    print(country)

show()
print(country)

# local scope
def show():
    country = "Netherlands"
    print(country)

show()
