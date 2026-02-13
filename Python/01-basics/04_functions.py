def add(a, b):
    return a + b

def greet(name="friend"):
    return f"Hello, {name}!"

def main():
    print(greet("User"))
    print("add(3, 5) =", add(3, 5))

    # simple input example
    # (uncomment to use)
    # n = input("Enter your name: ")
    # print(greet(n))

if __name__ == "__main__":
    main()
