from typing import List

class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        pos = [0]*n
        for i in range(n):
            pos[nums2[i]] = i

        # Replace SortedList with sorted array implementation
        before = [0]*n
        sorted_pos = []
        for i in range(n):
            # Count elements less than current position
            before[i] = self.bisect_left(sorted_pos, pos[nums1[i]])
            # Insert while maintaining sorted order
            self.insert_sorted(sorted_pos, pos[nums1[i]])

        after = [0]*n
        sorted_pos = []
        for i in range(n-1,-1,-1):
            # Count elements greater than current position
            after[i] = len(sorted_pos) - self.bisect_right(sorted_pos, pos[nums1[i]])
            # Insert while maintaining sorted order
            self.insert_sorted(sorted_pos, pos[nums1[i]])

        ans = 0
        for i in range(n):
            ans += before[i]*after[i]
        return ans

    def bisect_right(self, arr: List[int], x: int) -> int:
        left, right = 0, len(arr)
        while left < right:
            mid = (left + right) // 2
            if arr[mid] <= x:
                left = mid + 1
            else:
                right = mid
        return left

    def bisect_left(self, arr: List[int], x: int) -> int:
        left, right = 0, len(arr)
        while left < right:
            mid = (left + right) // 2
            if arr[mid] < x:
                left = mid + 1
            else:
                right = mid
        return left

    def insert_sorted(self, arr: List[int], x: int) -> None:
        pos = self.bisect_left(arr, x)
        arr.insert(pos, x)

if __name__=="__main__":
    nums1 = [2, 0, 1, 3]
    nums2 = [0, 1, 2, 3]
    print(Solution().goodTriplets(nums1,nums2))

    nums1 = [4, 0, 1, 3, 2]
    nums2 = [4, 1, 0, 2, 3]
    print(Solution().goodTriplets(nums1, nums2))