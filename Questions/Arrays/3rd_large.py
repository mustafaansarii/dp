def third_large(arr, n):
    if n < 3:
        return -1

    # Initialize three largest values
    large = slarge = tlarge = float('-inf')

    for i in range(n):
        if arr[i] > large:
            tlarge = slarge
            slarge = large
            large = arr[i]
        elif arr[i] > slarge:
            tlarge = slarge
            slarge = arr[i]
        elif arr[i] > tlarge:
            tlarge = arr[i]

    return tlarge if tlarge != float('-inf') else -1


# Test case
arr = [855, 450, 132, 359, 233, 825, 604, 481, 262, 337, 720, 525, 652, 300, 906, 219, 926, 906, 293, 864, 817, 498, 30, 639, 661]
n = len(arr)
tlarge = third_large(arr, n)
print(tlarge)  # Expected output: 906
