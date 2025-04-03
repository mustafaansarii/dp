from typing import *
def merge(arr: List[int], left: int, mid: int, right: int):
    left_copy = arr[left:mid + 1]
    right_copy = arr[mid + 1:right + 1]
    i = 0
    j = 0
    k = left
    count = 0
    while i < len(left_copy) and j < len(right_copy):
        if left_copy[i] <= right_copy[j]:
            arr[k] = left_copy[i]
            i += 1
        else:
            # Count inversions when right element is smaller
            count += len(left_copy) - i
            arr[k] = right_copy[j]
            j += 1
        k += 1
    while i < len(left_copy):
        arr[k] = left_copy[i]
        i += 1
        k += 1
    while j < len(right_copy):
        arr[k] = right_copy[j]
        j += 1
        k += 1
    return count

def mergeSort(arr: List[int], left: int, right: int):
    count = 0
    if left < right:
        mid = (left + right) // 2
        count += mergeSort(arr, left, mid)
        count += mergeSort(arr, mid + 1, right)
        count += merge(arr, left, mid, right)
    return count

def numberOfInversions(a: List[int], n: int) -> int:
    return mergeSort(a, 0, n - 1)


if  __name__ == '__main__':
    A = [5, 3, 2, 1, 4]
    N = 5
    print(numberOfInversions(A, N))

