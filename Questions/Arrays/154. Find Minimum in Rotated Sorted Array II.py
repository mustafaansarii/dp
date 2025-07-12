class Solution:
    def findMin(self, nums: [int]) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2

            if nums[mid] > nums[right]:
                left = mid + 1

            elif nums[mid] < nums[right]:
                right = mid

            else:
                right -= 1

        return nums[left]

if __name__ == "__main__":
    nums = [10,2,10,10,10]
    print(Solution().findMin(nums))