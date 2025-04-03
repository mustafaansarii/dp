from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.dfs(nums, [], res)
        return res

    def dfs(self, nums, path, res):
        if not nums:
            res.append(path.copy())
        for i in range(len(nums)):
            new_nums = []
            for j in range(len(nums)):
                if j != i:
                    new_nums.append(nums[j])
            new_path = path[:]
            new_path.append(nums[i])
            self.dfs(new_nums, new_path, res)
    

