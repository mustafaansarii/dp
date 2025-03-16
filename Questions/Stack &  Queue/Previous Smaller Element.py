def smaller_ele(arr):
    n=len(arr)
    stack=[]
    res=[]
    for i in range(n):
        while stack and stack[-1] > arr[i]:
            stack.pop()
        if not stack:
            res.append(-1)
        else:
            res.append(stack[-1])
        stack.append(arr[i])
    return res



if  __name__ == "__main__":
    arr = [12, 1, 2, 3, 0, 11, 4]
    print(smaller_ele(arr))
