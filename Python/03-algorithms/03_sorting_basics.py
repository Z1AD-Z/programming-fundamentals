def bubble_sort(arr):
    a = arr[:]  # copy
    n = len(a)
    for i in range(n):
        for j in range(0, n - 1 - i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a

def main():
    arr = [5, 1, 4, 2, 8]
    print("original:", arr)
    print("sorted:", bubble_sort(arr))

if __name__ == "__main__":
    main()
