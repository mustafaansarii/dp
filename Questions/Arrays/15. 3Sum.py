from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        res=[]
        maps={}
        for i in range(n):
            for j in range(i+1,n):
                maps[nums[i] + nums[j]]=maps.get(nums[i]+nums[j],[])+[[i, j]]
                if nums[i]==0 and nums[j]==0:
                    maps[0]=maps.get(0, [])+[[i, j]]

        for i in range(n):
            if -nums[i] in maps:
                for pair in maps[-nums[i]]:
                    if i not in pair:
                        tmp=[nums[pair[0]], nums[pair[1]], nums[i]]
                        tmp.sort()
                        if tmp not in res:
                            res.append(tmp)
        return res



if __name__=="__main__":
    solution = Solution()
    print(solution.threeSum([-1,0,1,2,-1,-4]))