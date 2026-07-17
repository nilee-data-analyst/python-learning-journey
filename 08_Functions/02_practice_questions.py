
# create a simple function
def welcome():
    print("Welcome to Data Analytics")

welcome()

# create a function that prints name
def my_name(name):
    print("My name is" ,name)

my_name("Nilee")

# create a function that accepts one number and prints its square
def square(number):
    print(number ** 2)

square(6)

# create a function that accepts two numbers and prints their sum
def add(a,b):
    return a+b

print(add(10,15))

# create a function that prints whether a number is even or odd
def even_odd(number):
    if number % 2 == 0:
        print("even number")
    else:
        print("odd number")

even_odd(5)

# Create a function that accepts a name and age and prints
def details(name,age):
    print(name ,"is",age, "years old.")

details("John", 30)

# Create a function with a default country as "India"
def country(name = "India"):
    print(name)

country()
country("Netherlands")

# Create a function that returns the largest of two numbers
def largest_num(a,b):
    return max(a,b)

print(largest_num(10,3))

# Create a function that returns the smallest of three numbers
def smallest_num(a,b,c):
    return min(a,b,c)

print(smallest_num(5,12,2))

# Create a function that returns the average of five numbers
def average(a,b,c,d,e):
    return (a+b+c+d+e/5)

print(average(10,20,30,40,50))

# Create a function that counts vowels in a string.
def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0

    for char in text:
        if char in vowels:
            count +=1
    
    return count

print(count_vowels("Data Analytics"))

# Create a function that checks whether a number is positive, negative, or zero.
def check_number(number):
    if number>0:
        print("Positive")
    elif number<0:
        print("Negative")
    else:
        print("Zero")

check_number(-6)

# Create a function that accepts a list and returns the largest element.
def largest_number(number):
    return max(number)

print(largest_number([5,10,15,20,25,30]))

# Create a function that accepts a list and returns the sum of all numbers.
def total(numbers):
    return sum(numbers)

print(total([10, 20, 30, 40]))

# Use *args to calculate the sum of any number of values.
def total(*numbers):
    return sum(numbers)

print(total(10,20,30,40,50))
print(total(10,20))

# Use **kwargs to print a person's details.
def details(**person):
    for key ,value in person.items():
        print(key , ":", value)

details(name = "John",
        age = 30,
        country = "Netherlands",
        profession = "Data Analyst")

# Create a lambda function that returns the cube of a number.
cube = lambda x:x**3
print(cube(3))

# Use a lambda function to sort this list by marks.
students = [
    ("John",80),
    ("Nilee",95),
    ("Rahul",70)
]

students.sort(key =lambda x:x[1] )
print(students)

# Create a function that returns the factorial of a number
def factorial(num):
    result = 1

    for i in range(1, num+1):
        result= result * i

    return result
print(factorial(5))

# Create a function that calculates total monthly sales
def total_sales(jan,feb,march):
    return jan + feb + march

print(total_sales(1200,1800,1500))

# Create a function that calculates average employee salary
def averge_salary(salaries):
    return sum(salaries)/len(salaries)

print(averge_salary([45000,55000,62000,48000]))

# Create a function that finds the highest sales value in a list
def highest_sales(sales):
    return max(sales)

print(highest_sales([1200,1800,1500]))

# create a function that counts how many employees earn more than €50,000
def salary_count(salaries):
    count = 0

    for salary in salaries:
      if salary > 50000:
        count +=1
    return count
print(salary_count([45000,55000,62000,48000]))

# create a function that accepts customer names and prints them in uppercase
def uppercase_names(names):
    for name in names:
        print(name.upper())

uppercase_names(["John", "Smith", "Emma"])

# create a function that accepts product prices and returns the total bill
def total_bill(prices):
    total = 0

    for price in prices:
        total+=price
    
    return total

print(total_bill([10,25,30,50]))

# create a function that calculates a 21% VAT amount for a given price
def calculate_vat(price):
    return price * 0.21

print(calculate_vat(100))

# create a function that checks whether an email contains "@"
def check_email(email):
    return "@" in email

print(check_email("john123@gmail.com"))
print(check_email("john123gmail.com"))


# Create a function that accepts a dictionary of employee salaries and returns the employee with the highest salary.
def highest_salary(employees):
    highest = max(employees, key = employees.get)
    return highest

employees = {
    "John":62000,
    "Emma":58000,
    "David":72000
}

print(highest_salary(employees))

# Create a function that accepts a list of monthly sales.
def sales_report(sales):
    return {"highest sale": max(sales),
            "lowest sale": min(sales),
            "average sale": sum(sales)/len(sales),
            "total sale" : sum(sales)}

sales = [1200,1800,1500,2200,2800]

report = sales_report(sales)

for key,value in report.items():
    print(key,":",value)