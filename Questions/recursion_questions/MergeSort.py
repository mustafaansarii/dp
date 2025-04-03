class Solution:
    def MergeSort(self, nums):
        if len(nums) <= 1:
            return nums
        mid = len(nums) // 2
        left = self.MergeSort(nums[:mid])
        right = self.MergeSort(nums[mid:])
        return self.merge(left, right)