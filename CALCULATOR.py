def add(x, y):
    return x + y

def subtract(a,b):
    return a - b

def multiply(a, b):
    return a * b 

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero"
    return a/ b

def calculator():
    n1 = float(input("Enter the first number: "))
    n2 = float(input("Enter the second number: "))

    print("\nSelect operation:")
    print("1. Add(+)")
    print("2. Subtract(-)")
    print("3. Multiply(*)")
    print("4. Divide(/)")

    choice = input("Enter choice (1, 2, 3, or 4): ")

    if choice == '1':
        result = add(n1, n2)
        operator = '+'
    elif choice == '2':
        result = subtract(n1, n2)
        operator = '-'
    elif choice == '3':
        result = multiply(n1, n2)
        operator = '*'
    elif choice == '4':
        result = divide(n1, n2)
        operator = '/'
    else:
        print("Invalid input. Please enter a valid choice.")
        return

    print(f"\nResult: {n1} {operator} {n2} = {result}\n")

if __name__ == "__main__":
    calculator()
