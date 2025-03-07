class Solution:
    def decodedString(self, s):
        # code here
        statck=[]
        n=len(s)
        for i in range(n):
            if s[i]=="]":
                temp=""
                while statck[-1]!="[":
                    temp=statck.pop()+temp
                statck.pop()
                num=""
                while statck and statck[-1].isdigit():
                    num=statck.pop()+num
                statck.append(int(num)*temp)
            else:
                statck.append(s[i])
        return  "".join(statck)




if __name__=="__main__":
    s = "3[b2[ca]]"
    ob = Solution()
    print(ob.decodedString(s))