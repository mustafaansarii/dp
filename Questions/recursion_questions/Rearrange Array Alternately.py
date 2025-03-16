class Solution:
    ##Complete this function
    # Function to rearrange  the array elements alternately.
    def Rearrange_Array_Alternately(self, arr):
        ##Your code here
        n = len(arr)
        temp = arr.copy()
        left = 0
        right = n - 1
        flag = True

        for i in range(n):
            if flag:
                arr[i] = temp[right]
                right -= 1
            else:
                arr[i] = temp[left]
                left += 1
            flag = not flag

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6]
    output = [6, 1, 5, 2, 4, 3]
    Solution().Rearrange_Array_Alternately(arr)
    print(arr)