def max_score(arr):
    n = len(arr)
    if n < 2:
        return 0
    m = len(arr[0])
    if m < 2:
        return 0

    max_val = 0
    for i in range(n - 1):
        for j in range(m - 1):
            if arr[i][j] == arr[i][j + 1] == arr[i + 1][j] == arr[i + 1][j + 1]:
                max_val = max(max_val, arr[i][j])
    return max_val if max_val > 0 else 0


# Test the function with the provided example
arr = [[5,5,5],[5,5,6],[5,5,5]]
print(max_score(arr))
