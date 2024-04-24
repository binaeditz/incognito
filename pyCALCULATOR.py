def calculator():
    """A simple calculator that performs basic arithmetic operations."""

    while True:
        try:
            operation = input("Enter an operation (+, -, *, /): ")
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if operation == "+":
                result = num1 + num2
            elif operation == "-":
                result = num1 - num2
            elif operation == "*":
                result = num1 * num2
            elif operation == "/":
                result = num1 / num2
            else:
                print("Invalid operation. Please try again.")
                continue

            print(f"{num1} {operation} {num2} = {result}")
            break
            

        except ValueError:
            print("Invalid input. Please enter numbers only.")

calculator()
