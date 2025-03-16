def merge_two_arr(arr1, arr2):
    res = []
    left1, left2 = 0, 0
    right1, right2 = len(arr1), len(arr2)
    while left1 < right1 and left2 < right2:
        while left1 < right1 and arr1[left1] == 0:
            left1 += 1
        while left2 < right2 and arr2[left2] == 0:
            left2 += 1
        if left1 < right1 and left2 < right2:
            if arr1[left1] < arr2[left2]:
                res.append(arr1[left1])
                left1 += 1
            elif arr1[left1] > arr2[left2]:
                res.append(arr2[left2])
                left2 += 1
            else:
                res.append(arr1[left1])
                res.append(arr2[left2])
                left1 += 1
                left2 += 1

    res.extend([num for num in arr1[left1:] if num != 0])
    res.extend([num for num in arr2[left2:] if num != 0])

    return res

if __name__=="__main__":
    arr1=[1,2,3,0,0,0]
    arr2=[2,5,6]
    print(*merge_two_arr(arr1,arr2))