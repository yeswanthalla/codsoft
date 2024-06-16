def calculator():
    print("Simple Calculator")
    print("Enter two numbers and choose an operation.")

    # Get user input
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    print("Choose an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    operation = input("Enter the number corresponding to the operation: ")

    # Perform the calculation based on the user's choice
    if operation == '1':
        result = num1 + num2
        op = '+'
    elif operation == '2':
        result = num1 - num2
        op = '-'
    elif operation == '3':
        result = num1 * num2
        op = '*'
    elif operation == '4':
        if num2 != 0:
            result = num1 / num2
            op = '/'
        else:
            print("Error: Division by zero is not allowed.")
            return
    else:
        print("Invalid operation choice. Please try again.")
        return

    # Display the result
    print(f"The result of {num1} {op} {num2} is: {result}")

# Run the calculator
calculator()
