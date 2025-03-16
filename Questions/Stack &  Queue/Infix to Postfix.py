class Solution:
    def InfixtoPostfix(self, s):
        priority={'^':3,'*':2,'/':2,'+':1,'-':1,'(':0}
        stack=[]
        n=len(s)
        ans=''
        for i in range(n):
            if s[i]!="(" and s[i]!=")" and s[i]!="+" and s[i]!="-" and s[i]!="*" and s[i]!="/" and s[i]!="^":
                ans+=s[i]
            if s[i]=="(":
                stack.append(s[i])
            if s[i]==")":
                while stack[-1]!='(':
                    ans+=stack.pop()
                stack.pop()
            if s[i]=="+" or s[i]=="-" or s[i]=="*" or s[i]=="/" or s[i]=="^":
                if len(stack)==0:
                    stack.append(s[i])
                else:
                    while len(stack)!=0 and priority[stack[-1]]>=priority[s[i]]:
                        ans+=stack.pop()
                    stack.append(s[i])
            if i==n-1:
                while len(stack)!=0:
                    ans+=stack.pop()
        return ans



if __name__ == '__main__':
    s = "a+b*(c^d-e)^(f+g*h)-i"
    Output= 'abcd ^ e - fgh * + ^*+i -'
    ob = Solution()
    print(ob.InfixtoPostfix(s))
