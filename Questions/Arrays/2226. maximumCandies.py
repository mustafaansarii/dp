from typing import List
class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        left = 1
        right = max(candies)
        res = 0
        while left <= right:
            mid = (left + right) // 2
            children_count = sum(pile // mid for pile in candies)

            if children_count >= k:
                res = mid
                left = mid + 1
            else:
                right = mid - 1

        return res


if __name__ == "__main__":
    candies = [5, 8, 6]
    k = 3
    print(Solution().maximumCandies(candies, k))
