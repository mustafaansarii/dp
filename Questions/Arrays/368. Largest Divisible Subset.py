from typing import List
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        dp = [1] * n
        max_len = 1
        max_index = 0
        for i in range(1, n):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    dp[i] = max(dp[i], dp[j] + 1)
                    if dp[i] > max_len:
                        max_len = dp[i]
                        max_index = i
        result = []
        curr = nums[max_index]
        for i in range(max_index, -1, -1):
            if curr % nums[i] == 0 and dp[i] == max_len:
                result.append(nums[i])
                curr = nums[i]
                max_len -= 1
        return result[::-1]


if __name__ == '__main__':
    nums = [1, 2, 4, 8]
    Output= [1, 2, 4, 8]
    sol=Solution().largestDivisibleSubset(nums)
    print(sol)