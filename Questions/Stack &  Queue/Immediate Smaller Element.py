def immediate_smaller(arr):
    n = len(arr)
    stack = []
    res = [-1 for _ in range(n)]
    right = n-1
    while right > -1:
        if not stack:
            stack.append(arr[right])
        elif arr[right] > stack[-1]:
            res[right] = stack[-1]
            stack.append(arr[right])
        else:
            while stack and stack[-1] >= arr[right]:
                stack.pop()
            if stack and stack[-1] < arr[right]:
                res[right] = stack[-1]
            stack.append(arr[right])
        right -= 1
    return res


if __name__ == "__main__":
    arr = [4, 2, 1, 5, 3]
    Output = [2, 1, -1, 3, -1]
    print(immediate_smaller(arr))