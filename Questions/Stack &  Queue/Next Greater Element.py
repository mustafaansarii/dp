def Next_Greater(arr):
    n = len(arr)
    stack = []
    res = [-1 for _ in range(n)]
    right = n-1
    while right > -1:
        if not stack:
            stack.append(arr[right])
        elif arr[right] >= stack[-1]:
            while stack and stack[-1] <= arr[right]:
                stack.pop()
            if stack:
                res[right] = stack[-1]
            stack.append(arr[right])
        else:
            res[right] = stack[-1]
            stack.append(arr[right])
        right -= 1
    return res


if __name__ == "__main__":
    arr = [1, 3, 2, 4,4]
    Output = [3, 4, 4, -1]
    print(Next_Greater(arr))