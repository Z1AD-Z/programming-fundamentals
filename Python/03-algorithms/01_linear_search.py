def linear_search(arr, target):
    for i, value in enumerate(arr):
        if value == target:
            return i
    return -1

def main():
    arr = [4, 2, 9, 1]
    print(linear_search(arr, 9))   # 2
    print(linear_search(arr, 99))  # -1

if __name__ == "__main__":
    main()
