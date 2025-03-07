class Solution:
    def isValid(self, s: str) -> bool:
        n = len(s)
        stack = []
        for i in range(n):
            if s[i] == "(" or s[i] == "{" or s[i] == "[":
                stack.append(s[i])
            elif len(stack) == 0:
                return False
            else:
                curr = stack.pop()
                if (curr == "(" and s[i] != ")") or \
                   (curr == "{" and s[i] != "}") or \
                   (curr == "[" and s[i] != "]"):
                    return False
        return len(stack) == 0

if __name__ == '__main__':
    s=Solution()
    print(s.isValid("()[]{}"))