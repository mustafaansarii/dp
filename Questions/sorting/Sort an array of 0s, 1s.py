def Sort_0_1(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        while left < right and arr[left] == 0:
            left += 1

        while left < right and arr[right] == 1:
            right -= 1

        if left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1


if __name__ == "__main__":
    arr = [1,0,1,0,1,0,0,1]
    Sort_0_1(arr)
    print(arr)