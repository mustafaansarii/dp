class Solution:
    def printUniqueSubset(self, nums):
        # Sort array first to handle duplicates efficiently
        nums.sort()
        fin_res = []
        def subset(idx, n, arr, res):
            fin_res.append(res[:])
            for i in range(idx, n):
                # Skip duplicates
                if i > idx and arr[i] == arr[i-1]:
                    continue
                res.append(arr[i])
                subset(i+1, n, arr, res)
                res.pop()
        subset(0, len(nums), nums, [])
        return fin_res


if __name__=="__main__":
    nums=[1,2,2]
    print(Solution().printUniqueSubset(nums))