from typing import List
class Solution:
    def findMin(self, nums: List[int]) -> int:
        n=len(nums)
        left=0
        right=n-1
        mini=float("inf")
        while left<=right:
            mid=(left+right)//2
            if nums[left]<=nums[mid]:
                mini=min(mini,nums[left])
                left=mid+1
            else:
                mini=min(mini,nums[mid])
                right=mid-1

        # right=mid
        return mini





if  __name__ == "__main__":
    nums = [3,4,5,6,1,2]
    obj = Solution()
    print(obj.findMin(nums))
