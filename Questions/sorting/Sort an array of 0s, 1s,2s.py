def Sort_0_1_2(arr):
    left = 0
    mid=0
    right = len(arr) - 1

    while mid <= right:
        if arr[mid] == 0:
            arr[left], arr[mid] = arr[mid], arr[left]
            left += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:
            arr[mid], arr[right] = arr[right], arr[mid]
            right -= 1


if __name__ == "__main__":
    arr=[0,1,2,0,1,2,0,1,2]
    Sort_0_1_2(arr)
    print(arr)