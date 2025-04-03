from typing import List


class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        arr = []
        for row in grid:
            arr.extend(row)
        arr.sort()
        n = len(arr)
        median = arr[n // 2]
        ans = 0
        for num in arr:
            diff = abs(num - median)
            if diff % x != 0:
                return -1
            ans += diff // x
        return ans


if  __name__ == '__main__':
    grid = [[2, 4], [6, 8]]
    x = 2
    Output= 4
    s = Solution()
    print(s.minOperations(grid, x=2))