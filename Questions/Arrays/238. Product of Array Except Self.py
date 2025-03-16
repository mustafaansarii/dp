from sys import prefix
from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix=1
        n=len(nums)
        res = [1] * n
        for i  in range(n):
            res[i]=prefix
            prefix*= nums[i]

        suffix=1
        for i in range(n-1,-1,-1):
            res[i] *= suffix
            suffix*=nums[i]

        return  res



if __name__ == '__main__':
    s = Solution()
    print(s.productExceptSelf([1,2,3,4]))