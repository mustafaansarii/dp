class Solution:
    def kthCharacter(self, k: int, operations: [int]) -> str:
        n=len(operations)
        count=0
        length= pow(2, n-1)
        for i in range(n-1,-1,-1):
            if k>length:
                k-=length
                if operations[i]==1:
                    count+=1
            length//=2
        return chr(ord('a') + (count%26))

if __name__ == '__main__':
    sol = Solution()
    print(sol.kthCharacter(5, [0, 0, 0]))
    """
    Input: k = 5
    Output: "a"
    Initially, word == "a". Alice performs the three operations as follows:
    - Appends "a" to "a", word becomes "aa"
    - Appends "aa" to "aa", word becomes "aaaa"
    
    
    
    
    
    
    
    
    - Appends "aaaa" to "aaaa", word becomes "aaaaaaaa"
    """