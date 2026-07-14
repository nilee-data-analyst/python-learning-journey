
# Check whether a number is positive, negative or zero
num = int(input("Enter a number:"))

if num > 0:
    print("positive")
elif num < 0:
    print("negative")
else :
    print("zero")

# Find the largest of three numbers
num1 = 5
num2 = 10
num3 = 15

if num1>num2 and num1>num3:
    largest = num1
elif num2>num3 and num2>num1:
    largest = num2
else:
    largest = num3
print(largest)

'''
Check whether a student passed.
Passing marks = 40.
'''
marks = int(input("Enter marks:"))

if marks >= 40:
    print("passed")
else:
    print("failed")

# Check whether a year is a leap year
year = int(input("Enter year:"))

if (year%4 == 0 and year%100 != 0) or (year%400 == 0):
    print("Leap year")
else:
    print("Not a Leap year")

# Assign grades
marks = int(input("Enter marks:"))

if marks >= 90:
    print("Grade A")
elif marks >= 80:
    print("Grade B")
elif marks >= 70:
    print("Grade c")
elif marks >= 60:
    print("Grade D")
else:
    print("Fail")

# Check if a person can vote
age = int(input("Enter age:"))

if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")

# Check whether a password length is at least 8 characters
password = input("Enter password:")
if len(password) >= 8:
    print("valid")
else:
    print("password too short")

# Calculate electricity bill
units = int(input("Enter units consumed: "))

if units < 100:
    bill = units * 5
elif units <= 300:
    bill = units * 7
else:
    bill = units * 10

print("Electricity Bill = ₹", bill)

# BMI Calculator
height = float(input("Enter height in meters: "))
weight = float(input("Enter weight in kg: "))

bmi = weight / (height ** 2)

print("BMI =", round(bmi, 2))

if bmi < 18.5:
    print("Underweight")
elif bmi < 25:
    print("Normal")
elif bmi < 30:
    print("Overweight")
else:
    print("Obese")

