class Solution:
    def left_bound(self, arr,target):
        left=0
        right=len(arr)
        while left < right:
            mid=(left+right)//2
            if arr[mid] < target:
                left=mid+1
            else:
                right=mid
        return left
    
    def right_bound(self, arr, target):
        left=0
        right=len(arr)
        while left < right:
            mid=(left+right)//2
            if arr[mid] <= target:
                left=mid+1
            else:
                right=mid
        return right-1

if  __name__ == '__main__':
    arr=[1,2,2,2,3]
    s=Solution()
    print(s.left_bound(arr,2))
    print(s.right_bound(arr,2))