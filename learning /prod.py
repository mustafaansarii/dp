class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        res = [0 for _ in range(n)]
        prefix = 1
        for i in range(n):
            res[i] = prefix
            prefix *= nums[i]

        sufix = 1
        for i in range(n - 1, -1, -1):
            res[i] *= sufix
            sufix *= nums[i]
        return res



num=[1,2,3,4]
Solution().productExceptSelf(num)