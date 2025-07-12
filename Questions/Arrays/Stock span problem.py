class Solution:
    def calculateSpan(self, arr):
        #write code here
        n=len(arr)
        curr=0
        res = []
        stack=[]

        for i in range(n):
            while stack and arr[stack[-1]] <= arr[i]:
                stack.pop()

            if not stack:
                curr=i+1
            else:
                curr=i-stack[-1]

            stack.append(i)
            res.append(curr)

        return res

if __name__=="__main__":
    arr= [100, 80, 60, 70, 60, 75, 85]
    sol=Solution()
    print(sol.calculateSpan(arr))