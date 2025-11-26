#this is for test.
import random

def generateList(n):
    return [random.randint(0, 50) for _ in range(n)]

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]


def main():
    arr = generateList(10)
    print("Бульбашкове сортування до:", arr)
    bubble_sort(arr)
    print("Бульбашкове сортування після:", arr)

    arr = generateList(10)
    print("Сортування вибором до:", arr)
    selection_sort(arr)
    print("Сортування вибором після:", arr)

    arr = generateList(10)
    print("Бульбашкове вибором до:", arr)
    insertion_sort(arr)
    print("Бульбашкове вибором після:", arr)

if __name__ == "__main__":
    main()