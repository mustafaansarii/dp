from typing import List
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []

        n = len(nums)
        left = 0
        ans = [str(nums[0])]

        if n == 1:
            return ans

        for i in range(1, n):
            if nums[i] - nums[i-1] != 1:
                if i-1 > left:
                    ans[-1] = ans[-1] + "->" + str(nums[i-1])
                ans.append(str(nums[i]))
                left = i

        if left < n-1:
            ans[-1] = ans[-1] + "->" + str(nums[-1])

        return ans

if __name__== '__main__':
    sol = Solution()
    nums = [0,1,2,4,5,7]
    print(sol.summaryRanges(nums))