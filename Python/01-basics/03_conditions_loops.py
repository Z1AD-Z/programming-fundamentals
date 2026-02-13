def main():
    x = 7

    # condition
    if x > 10:
        print("x is greater than 10")
    elif x == 10:
        print("x equals 10")
    else:
        print("x is less than 10")

    # for loop
    for i in range(1, 6):
        print("for:", i)

    # while loop
    count = 3
    while count > 0:
        print("while:", count)
        count -= 1

if __name__ == "__main__":
    main()
