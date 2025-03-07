
class Solution:
    def postToInfix(self, postfix):
        # Code here
        priority={"^": 3, "*":2, "/":2, "+":1, "-":1, "(":0}
        stack=[]
        ans=''
        n=len(postfix)
        for i in range(n):
            if postfix[i] != "^" and  \
                postfix[i] != "*" and  \
                postfix[i] != "/" and  \
                postfix[i] != "+" and  \
                postfix[i] != "-" and  \
                postfix[i] != "(" and  \
                postfix[i] != ")":
                stack.append(postfix[i])
            else:
                if len(stack)>1:
                    op2 = stack.pop()
                    op1 = stack.pop()
                    stack.append("(" + op1 + postfix[i] + op2 + ")")
                elif len(stack)==1:
                    stack.append("(" + stack.pop() + postfix[i] +")")
            if i==n-1:
                ans+=stack[0]
        return  ans

if __name__ == '__main__':
    postfix = 'ab*c+'
    # Output: ((a*b)+c)
    ob = Solution()
    print(ob.postToInfix(postfix))
