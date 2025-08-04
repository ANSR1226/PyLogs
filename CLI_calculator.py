def addition():
    num1 = int(input("Number 1: "))
    print("  +")
    num2 = int(input("Number 2: "))
    print("Sum:", num1 + num2)

def subtraction():
    num1 = int(input("Number 1: "))
    print("  -")
    num2 = int(input("Number 2: "))
    print("Difference:", num1 - num2)

def multiplication():
    num1 = int(input("Number 1: "))
    print("  x")
    num2 = int(input("Number 2: "))
    print("Product:", num1 * num2)

def division():
    num1 = int(input("Dividend: "))
    print("  /")
    num2 = int(input("Divisor: "))
    if num2 != 0:
        print("Quotient:", num1 / num2)
    else:
        print("Error: Cannot divide by zero")

def power():
    num1 = int(input("Base: "))
    print("  **")
    num2 = int(input("Power: "))
    print("Result:", num1 ** num2)

while True:
    print("\n--- CLI Calculator ---")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Power")
    print("6. Exit")

    option = int(input("Choose an option (1–6): "))

    if option == 1:
        addition()
    elif option == 2:
        subtraction()
    elif option == 3:
        multiplication()
    elif option == 4:
        division()
    elif option == 5:
        power()
    elif option == 6:
        print("Exiting calculator.")
        break
    else:
        print("Invalid option. Try again.")
