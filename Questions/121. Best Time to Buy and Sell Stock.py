class Solution:
    def maxProfit(self, prices: [int]) -> int:
        profit=0
        mini=prices[0]
        for i in range(len(prices)):
            curr_max=prices[i]-mini
            profit=max(curr_max,profit)
            mini=min(mini,prices[i])
        return profit


print(Solution().maxProfit(prices = [7, 1, 5, 3, 6, 4]) )
# Input: prices = [7, 1, 5, 3, 6, 4]
# Output: 5
