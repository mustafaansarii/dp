from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)

        # Step 1: Modify the array to handle negative and zero
        for i in range(n):
            if nums[i] <= 0:
                nums[i] = n + 1
        print(nums)
        # Step 2: Mark the presence of each number in the array
        for i in range(n):
            num = abs(nums[i])
            if num <= n: 
                nums[num - 1] = -abs(nums[num - 1])
        print(nums)
        # Step 3: Find the first missing positive number
        for i in range(n):
            if nums[i] > 0:
                return i + 1
        print(nums)
        return n + 1



if __name__=='__main__':
    output=Solution()
    print(output.firstMissingPositive([-7,8,-9,11,12,1,2,3,-5876]))