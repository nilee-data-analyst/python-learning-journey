# Print numbers 1–20
i = 1
while i <= 20:
  print(i)
  i += 1

# Print even numbers 2–50
i = 2
while i <= 50:
    print(i)
    i+=2

# Print multiplication table of 7
num = 1
while num <= 10:
   print("7 *", num, "=", 7 * num)
   num +=1 

# Print numbers from 20 down to 1
num = 20 
while num >= 1:
   print(num)
   num -= 1

# Calculate the sum of numbers 1–100
num = 1
total = 0

while num <= 100:
   total += num
   num += 1
print(total)

# Print all multiples of 5 below 100
num = 5

while num < 100:
   print(num)
   num += 5

# Print the first 15 odd numbers
num = 1
count = 0

while count < 15:
    print(num)
    num += 2
    count += 1

# Ask the user to enter a password until it is "python123"
password = ""

while password != "python123":
    password = input("Enter password: ")

print("Access granted")

# Reverse a number
num = int(input("Enter a number: "))

reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

print(reverse)

# Count digits in a number
num = int(input("Enter a number: "))

count = 0

while num > 0:
    num = num // 10
    count += 1

print("Number of digits:", count)