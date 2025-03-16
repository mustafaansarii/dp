from typing import  List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # Implementation without using Python built-in functions
        res = []
        def permute_helper(nums, path):
            if len(nums) == 0:
                temp = []
                for x in path:
                    temp.append(x)
                res.append(temp)
                return

            for i in range(len(nums)):
                left = []
                right = []
                for j in range(len(nums)):
                    if j < i:
                        left.append(nums[j])
                    elif j > i:
                        right.append(nums[j])

                new_path = []
                for x in path:
                    new_path.append(x)
                new_path.append(nums[i])

                next_nums = []
                for x in left:
                    next_nums.append(x)
                for x in right:
                    next_nums.append(x)

                permute_helper(next_nums, new_path)
        permute_helper(nums, [])
        return res

if __name__ == '__main__':
    s = Solution()
    print(s.permute([1, 2, 3]))
