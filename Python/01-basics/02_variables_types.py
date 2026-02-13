def main():
    name = "User"
    age = 20
    height = 1.75
    is_student = True

    print("name:", name, type(name))
    print("age:", age, type(age))
    print("height:", height, type(height))
    print("is_student:", is_student, type(is_student))

    # Type conversion
    age_as_str = str(age)
    height_as_int = int(height)  # truncates decimals
    print("age_as_str:", age_as_str, type(age_as_str))
    print("height_as_int:", height_as_int, type(height_as_int))

if __name__ == "__main__":
    main()
