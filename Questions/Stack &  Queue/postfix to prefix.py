class Solution:
    def postfix_to_prefix(self, postfix):
        stack=[]
        n=len(postfix)
        ans=''
        for i in range(n):
            if postfix[i] not in "^*/+-()":
                stack.append(postfix[i])
            else:
                if len(stack)>1:
                    op2 = stack.pop()
                    op1 = stack.pop()
                    stack.append(postfix[i]+op1+op2)
                elif len(stack)==1:
                    stack.append(postfix[i]+stack.pop())
            if i==n-1:
                ans+=stack[0]
        return  ans




if  __name__ == '__main__':
    postfix = 'ABC/-AK/L-*'
    # Output: +*ab
    ob = Solution()
    print(ob.postfix_to_prefix(postfix))