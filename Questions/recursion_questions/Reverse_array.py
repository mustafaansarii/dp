def reverse_arr(arr):
    left=0
    right=len(arr)-1
    def rev(left,right,arr):
        if not left<right:
            return arr
        arr[left],arr[right]=arr[right],arr[left]
        rev(left+1,right-1,arr)
    rev(left,right,arr)
    return arr




if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    print(reverse_arr(arr))
