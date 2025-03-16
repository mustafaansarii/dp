class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        num = 0
        sign = '+'
        operators = {'+', '-', '*', '/'}
        i = 0

        while i < len(s):
            if s[i].isdigit():
                num = num * 10 + int(s[i])
            elif s[i] == '(':
                # Find matching closing parenthesis
                count = 1
                j = i + 1
                while j < len(s) and count > 0:
                    if s[j] == '(':
                        count += 1
                    elif s[j] == ')':
                        count -= 1
                    j += 1
                num = self.calculate(s[i+1:j-1])
                i = j - 1

            if (s[i] in operators or s[i] == ')' or i == len(s)-1):
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack.append(stack.pop() * num)
                elif sign == '/':
                    stack.append(int(stack.pop() / num))
                sign = s[i]
                num = 0
            i += 1

        return sum(stack)

if __name__ == '__main__':
    s = Solution()
    strs = "(1+(4+5+2)-3)+(6+8)"
    print(s.calculate(strs))