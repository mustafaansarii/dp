from typing import  List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        ans = []
        for i in intervals:
            if not ans or ans[-1][1] < i[0]:
                ans.append(i)
            else:
                ans[-1][1] = max(ans[-1][1], i[1])
        return ans




if __name__== "__main__":
    sol=Solution()
    interval=[]
    print()
    