
# Input weekday number (1-7).
Day = int(input("Enter weekday number(1-7):"))
match Day:
    case 1 | 2 | 3 | 4 | 5 :
        print("Weekday")
    case 6 | 7:
        print("weekend")

# Input month number (1-12).
Month = int(input("Enter month number(1-12):"))
match Month:
    case 1:
        print("January")
    case 2:
        print("February")
    case 3:
        print("March")
    case 4:
        print("April")
    case 5:
        print("May")
    case 6:
        print("June")
    case 7:
        print("July")
    case 8:
        print("August")
    case 9:
        print("September")
    case 10:
        print("October")
    case 11:
        print("November")
    case 12:
        print("December")

# Simple Calculator
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operator = input("Enter operator (+, -, *, /): ")

match operator:
    case "+":
        print("Result:", num1 + num2)
    case "-":
        print("Result:", num1 - num2)
    case "*":
        print("Result:", num1 * num2)
    case "/":
        if num2 != 0:
            print("Result:", num1 / num2)
        else:
            print("Cannot divide by zero")
    case _:
        print("Invalid operator")

# Input traffic light and print action
traffic_light = input("Enter traffic light(Red ,Yellow, Green):")
match traffic_light:
    case "Red":
        print("stop")
    case "Yellow":
        print("Get ready")
    case "Green":
        print("Go")
    case _:
        print("invalid traffic light")

# Input browser and Print corresponding message.
browser = input("Enter browser")

match browser:
    case "Chrome":
        print("Google chrome available")
    case "Edge":
        print("Microsoft edge available")
    case "Firefox":
        print("Mozilla firefox available")
    case "Safari":
        print("Safari available")
    case _:
        print("Invalid browser")
        
