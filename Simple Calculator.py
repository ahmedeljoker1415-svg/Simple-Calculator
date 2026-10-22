# ---Simple Calculator---
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b


def getnumber(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid Input , Please Enter A Valid Number : ")


def main():
    num1 = None

    while True:
        print("\n--- Command-Line Calculator ---")

        if num1 == None:
            num1 = getnumber("Enter First Number : ")

        print("Options / Operations: +, -, *, /, clear, exit")

        op = input("Enter Operation or choice ").strip().lower()

        if op == "exit":
            print("Goodbye!")
            break
        elif op == "clear":
            num1 = None
            print("Calculator cleared.")
            continue
        elif op not in ["+", "-", "*", "/"]:
            print("Invalid operator! Please choose from +, -, *, /")
            continue

        num2 = getnumber("Enter Second Number : ")

        if op == "+":
            result = add(num1, num2)
        elif op == "-":
            result = subtract(num1, num2)
        elif op == "*":
            result = multiply(num1, num2)
        elif op == "/":
            result = divide(num1, num2)

        print(f"Result: {num1} {op} {num2} = {result}")

        if isinstance(result, (int, float)):

            num1 = result
        else:
            num1 = None


if __name__ == "__main__":
    main()
