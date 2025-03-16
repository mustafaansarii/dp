from typing import List
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def combine_helper(start, path):
            if len(path) == k:
                temp = []
                for x in path:
                    temp.append(x)
                res.append(temp)
                return

            for i in range(start, n + 1):
                new_path = []
                for x in path:
                    new_path.append(x)
                new_path.append(i)
                combine_helper(i + 1, new_path)
        combine_helper(1, [])
        return res



if __name__ == '__main__':
    s = Solution()
    print(s.combine(4, 2))
    # Output= [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]