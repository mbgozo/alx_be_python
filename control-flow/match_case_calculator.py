num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operator = input("Choose the operation (+, -, *, /): ")

match operator:
    case n if n == "+":
        print(f"The result is {num1 + num2}")
    case n if n == "-":
        print(f"The result is {num1 - num2}")
    case n if n == "*":
        print(f"The result is {num1 * num2}")
    case n if n == "/":
        if num2 == 0:
            print("Cannot divide by zero")
        else:
            print(f"The result is {num1 / num2}")