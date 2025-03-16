from typing import List
class Solution:
    def countArrays(self, original: List[int], bounds: List[List[int]]) -> int:
        low, high = bounds[0]  

        for i in range(1, len(original)):
            diff = original[i] - original[i - 1] 
            new_low = low + diff
            new_high = high + diff

            ui, vi = bounds[i]
            low = max(new_low, ui)
            high = min(new_high, vi)

            if low > high:
                return 0

        return high - low + 1


if __name__ == '__main__':
    original = [1, 3, 5]
    bounds = [[6, 10], [5, 15], [1, 6]]
    print(Solution().countArrays(original, bounds))

