def binary_search(sorted_arr, target):
    left, right = 0, len(sorted_arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if sorted_arr[mid] == target:
            return mid
        elif sorted_arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

def main():
    arr = [1, 3, 5, 7, 9, 11]
    print(binary_search(arr, 7))   # 3
    print(binary_search(arr, 2))   # -1

if __name__ == "__main__":
    main()
