def calculate(a, op, b):
    if op == "+":
        return a + b
    if op == "-":
        return a - b
    if op == "*":
        return a * b
    if op == "/":
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return a / b
    raise ValueError("Unsupported operator. Use + - * /")

def main():
    print("CLI Calculator (+ - * /)")
    a = float(input("Enter first number: "))
    op = input("Enter operator (+ - * /): ").strip()
    b = float(input("Enter second number: "))

    try:
        result = calculate(a, op, b)
        print("Result:", result)
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
