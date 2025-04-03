from typing import List
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def comb_sum(idx, temp_res, k):
            if k == 0:
                res.append(temp_res[:])
                return

            for i in range(idx, len(candidates)):
                if i > idx and candidates[i] == candidates[i - 1]:
                    continue

                if candidates[i] > k:
                    break

                temp_res.append(candidates[i])
                comb_sum(i + 1, temp_res, k - candidates[i])
                temp_res.pop()

        comb_sum(0, [], target)
        return res

if __name__ == '__main__':
    s = Solution()
    print(s.combinationSum2([10,1,2,7,6,1,5], 8))