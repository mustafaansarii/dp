class Solution:
    def reverseDegree(self, s: str) -> int:
        count=0
        for i in range(len(s)):
            position=ord('z')-ord(s[i])+1

            count+=((i+1)*position)

        print(count)






if __name__ == "__main__":
    s=Solution()
    s.reverseDegree("abc")