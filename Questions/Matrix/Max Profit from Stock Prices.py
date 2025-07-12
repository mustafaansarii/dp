class Solution:
    def maxProfit(self, prices: [int]) -> int:
        mini=prices[0]
        max_profit=float('-inf')

        for i in range(len(prices)):
            curr = prices[i] - mini
            max_profit = max(max_profit, curr)
            mini = min(mini, prices[i])

        return max_profit
