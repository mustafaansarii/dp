from typing import List
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        # Using stack approach to count smaller numbers after self
        result = [0] * len(nums)
        stack = [] # Stack will store (number, original_index) pairs

        # Process numbers from right to left
        for i in range(len(nums)-1, -1, -1):
            # Binary search to find insertion position
            left, right = 0, len(stack)
            while left < right:
                mid = (left + right) // 2
                if stack[mid][0] >= nums[i]:
                    right = mid
                else:
                    left = mid + 1

            # Number of smaller elements is the insertion position
            result[i] = left

            # Insert current number at correct position to maintain sorted order
            stack.insert(left, (nums[i], i))

        return result

if __name__ == "__main__":
    s = Solution()
    print(s.countSmaller([5,2,6,1]))