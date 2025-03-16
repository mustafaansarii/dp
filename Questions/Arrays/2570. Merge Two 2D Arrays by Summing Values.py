from typing import  List


class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        maps = {}
        m = len(nums1)
        n = len(nums2)
        for i in range(m):
            maps[nums1[i][0]] = maps.get(nums1[i][0], 0) + nums1[i][1]

        for i in range(n):
            maps[nums2[i][0]] = maps.get(nums2[i][0], 0) + nums2[i][1]

        res = []
        for key in (maps.keys()):
            res.append([key, maps[key]])
        return res


if __name__=="__main__":
    nums1 = [[1,2],[2,3],[4,5]]
    nums2 = [[1,4],[3,2],[4,1]]
    print(Solution().mergeArrays(nums1,nums2))
