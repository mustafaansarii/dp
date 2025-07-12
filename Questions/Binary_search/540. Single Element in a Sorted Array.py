class Solution:
    def singleNonDuplicate(self, nums: [int]) -> int:
        left=0
        right=len(nums)-1
        while left<right:
            mid=(left+right)//2
            if mid%2==1:
                if nums[mid]==nums[mid-1]:
                    left=mid+1
                else:
                    right=mid-1
            else:
                if nums[mid]==nums[mid+1]:
                    left=mid+2
                else:
                    right=mid
        return nums[left]



if __name__ == "__main__":
    sol = Solution()
    nums = [1,1,2,3,3,4,4,8,8]
    print(sol.singleNonDuplicate(nums))
