from typing import List
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack=[]
        max_area=0
        for i,h in enumerate(heights):
            start=i
            while stack and stack[-1][1]>h:
                index,height=stack.pop()
                max_area=max(max_area,height*(i-index))
                start=index
            stack.append((start,h))
        return  max(max_area, max([h*(len(heights)-i) for i,h in stack]))


if __name__=="__main__":
    heights = [2, 1, 5, 6, 2, 3]
    # Output: 10
    heights2 = [2, 4]
    # Output: 4
    print(Solution().largestRectangleArea(heights))
    print(Solution().largestRectangleArea(heights2))
