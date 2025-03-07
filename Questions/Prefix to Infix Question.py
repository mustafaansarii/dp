

class Solution:
    def preToInfix(self, pre_exp):
        # Code here
        stack=[]
        n=len(pre_exp)
        ans=''
        for i in range(n):
            if pre_exp[n-1-i] != "^" and  \
                pre_exp[n-1-i] != "*" and  \
                pre_exp[n-1-i] != "/" and  \
                pre_exp[n-1-i] != "+" and  \
                pre_exp[n-1-i] != "-" and  \
                pre_exp[n-1-i] != "(" and  \
                pre_exp[n-1-i] != ")":
                stack.append(pre_exp[n-1-i])
            else:
                if len(stack)>1:
                    op1 = stack.pop()
                    op2 = stack.pop()
                    stack.append("(" + op1 + pre_exp[n-1-i] + op2 + ")")
                elif len(stack)==1:
                    stack.append("(" + stack.pop() + pre_exp[n-1-i] +")")
        return  stack[0]


if  __name__ == '__main__':
    pre_exp = '*-A/BC-/AKL'
    # Output: ((A-(B/C))*((A/K)-L))
    ob = Solution()
    print(ob.preToInfix(pre_exp))
