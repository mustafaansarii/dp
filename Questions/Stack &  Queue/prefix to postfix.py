class Solution:
    def prefix_to_postfix(self, prefix):
        stack=[]
        n=len(prefix)
        for i in range(n-1,-1,-1):
            if prefix[i] not in "^*/+-()":
                stack.append(prefix[i])
            else:
                op1 = stack.pop()
                op2 = stack.pop()
                stack.append(op1+op2+prefix[i])
        return  stack[0]


if  __name__ == '__main__':
    prefix='*-A/BC-/AKL'
    output='ABC/-AK/L-*'

    ob = Solution()
    print(ob.prefix_to_postfix(prefix))