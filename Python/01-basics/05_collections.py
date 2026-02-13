def main():
    # list
    numbers = [1, 2, 3]
    numbers.append(4)
    print("list:", numbers)

    # tuple (immutable)
    point = (10, 20)
    print("tuple:", point)

    # dict
    user = {"name": "User", "age": 20}
    user["country"] = "Morocco"
    print("dict:", user)
    print("user name:", user["name"])

    # set (unique values)
    unique_nums = {1, 1, 2, 3, 3}
    print("set:", unique_nums)

if __name__ == "__main__":
    main()
