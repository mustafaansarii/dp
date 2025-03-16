def second_large(arr,n):
    if n < 2:
        return -1
    large = arr[0]
    slarge = -1
    for i in range(1, n):
        if arr[i] > large:
            slarge = large
            large = arr[i]
        elif arr[i] < large and arr[i] > slarge:
            slarge = arr[i]
    return slarge

arr = [1, 2, 4, 6, 7, 5]
n = len(arr)
slarge = second_large(arr, n)
print(slarge)