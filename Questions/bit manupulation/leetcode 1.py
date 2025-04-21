from typing import List
class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        n=len(nums)
        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            bits = n.bit_length()
            return 1 << bits



if __name__ == '__main__':
    nums = [1,2,1]
    print(Solution().uniqueXorTriplets(nums))