class Solution:
    # @param A : tuple of integers
    # @return a list of integers
    def repeatedNumber(self, A):
        n = len(A)
        s = n*(n+1)//2
        s2 = n*(n+1)*(2*n+1)//6
        for i in range(n):
            s -= A[i]
            s2 -= A[i]*A[i]
        s2 = s2//s
        a = (s+s2)//2
        b = s2-a
        return [b,a]

if __name__ == "__main__":
    A = [3,1,2,5,3]
    obj = Solution()
    print(obj.repeatedNumber(A))