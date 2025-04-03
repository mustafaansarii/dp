
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)
        if n1 > n2:
            return False
        
        s1_count = [0] * 26
        window_count = [0] * 26
        
        for char in s1:
            s1_count[ord(char) - ord('a')] += 1
        
        for i in range(n2):
            window_count[ord(s2[i]) - ord('a')] += 1
            
            if i >= n1:
                window_count[ord(s2[i - n1]) - ord('a')] -= 1
            
            if i >= n1 - 1 and window_count == s1_count:
                return True
        
        return False

