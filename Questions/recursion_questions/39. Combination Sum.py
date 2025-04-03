from typing import List
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        final_res=[]
        def combinations(idx,n,res,arr,k):
            if k<0:
                return
            if k==0:
                final_res.append(res.copy())
                return
            if idx==n:
                return

            res.append(arr[idx])
            k-=arr[idx]
            combinations(idx, n, res, arr, k)
            res.pop()
            k+=arr[idx]
            combinations(idx+1, n, res, arr, k)
        combinations(0, len(candidates), [], candidates, target)
        return final_res



if __name__ == '__main__':
    s = Solution()
    print(s.combinationSum([2,3,6,7], 7))
    output = [[2, 2, 3], [7]]