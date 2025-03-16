from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def subset(idx, arr, curr_res,n):

            if idx == n:
                res.append(curr_res.copy())
                return
            curr_res.append(arr[idx])
            subset(idx+1, arr, curr_res, n)
            curr_res.pop()
            subset(idx+1, arr, curr_res, n)
        subset(0, nums, [], len(nums))
        return res


if __name__ == "__main__":
    nums = [1, 2, 3]
    print(Solution().subsets(nums))
