class Solution:
    def nextLargerElement(self, arr):
        # For circular array, iterate twice through array
        stack = []
        n = len(arr)
        ans = [-1] * n

        # Iterate from 0 to 2n-1 and use modulo to handle circular nature
        for i in range(2*n):
            curr = i % n
            while stack and arr[stack[-1]] < arr[curr]:
                ans[stack.pop()] = arr[curr]
            if i < n:
                stack.append(curr)

        return ans

if __name__ == '__main__':
    Iarr = [1, 3, 2, 4]
    # Output= [3 4 4 -1]
    print(Solution().nextLargerElement(Iarr))