def move_zer(arr):
    j=0
    for i in range(len(arr)):
        if arr[i]:
            arr[i],arr[j]=arr[j],arr[i]
            j+=1
    return arr
arr=[1,0,0,0,5,34,32,32,0]
print(*move_zer(arr))