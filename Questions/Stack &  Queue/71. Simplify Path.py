class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        path = path.split("/")
        for p in path:
            if p == "..":
                if stack:
                    stack.pop()
            elif p == "." or p == "":
                continue
            else:
                stack.append(p)
        return "/" + "/".join(stack)





if  __name__ == "__main__":
    sol = Solution()
    path = "/home//foo/"
    print(sol.simplifyPath(path))
    path = "/../"
    print(sol.simplifyPath(path))
    path = "/home/"
    print(sol.simplifyPath(path))
    path = "/.../a/../b/c/../d/./"
    print(sol.simplifyPath(path))