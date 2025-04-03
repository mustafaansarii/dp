from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(start, subset):
            if tuple(subset) not in res:
                res.append(tuple(subset))
            
            for i in range(start, len(nums)):
                subset.append(nums[i])
                backtrack(i + 1, subset)
                subset.pop()
        
        nums.sort()
        backtrack(0, [])
        result = []
        for subset in res:
            result.append(list(subset))
        return result

if __name__ == '__main__':
    s = Solution()
    print(s.subsetsWithDup([1,2,2]))