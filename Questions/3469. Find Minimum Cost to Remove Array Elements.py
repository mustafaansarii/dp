class Solution:
    def minCost(self, nums):
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])
        dp = [0] * (n + 1)
        dp[n-1] = nums[n-1]
        dp[n-2] = max(nums[n-2], nums[n-1])
        for i in range(n-3, -1, -1):
            cost1 = max(nums[i], nums[i+1]) + dp[i+2]
            cost2 = max(nums[i], nums[i+2]) + dp[i+2]
            cost3 = max(nums[i+1], nums[i+2]) + (dp[i+3] if i + 3 < n else 0)

            dp[i] = min(cost1, cost2, cost3)

        return dp[0]



if __name__=="__main__":
    solution = Solution()
    print(solution.minCost(nums = [6,2,8,4]))
