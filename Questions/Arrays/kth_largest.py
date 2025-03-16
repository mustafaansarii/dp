import random
def quickselect(arr, k):
    k = len(arr) - k
    return select(arr, 0, len(arr) - 1, k)

def select(arr, left, right, k):
    if left == right:
        return arr[left]

    pivot_index = partition(arr, left, right)

    if k == pivot_index:
        return arr[k]
    elif k < pivot_index:
        return select(arr, left, pivot_index - 1, k)
    else:
        return select(arr, pivot_index + 1, right, k)

def partition(arr, left, right):
    pivot = arr[right]
    i = left

    for j in range(left, right):
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1

    arr[i], arr[right] = arr[right], arr[i]
    return i


if __name__ == "__main__":
    arr=[12, 3, 5, 7, 19]
    n = len(arr)
    k=4
    print("K'th smallest element is",
          quickselect(arr, k))

