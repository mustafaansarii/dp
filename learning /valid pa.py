class Solution:
    def isValid(self, s: str) -> bool:
        arr=[]
        for i in s:
            if i=="(":
                if ")" in arr:
                    arr.remove(")")
                else:
                    arr.append(")")
            if i=="[":
                if "]" in arr:
                    arr.remove("]")
                else:
                    arr.append("]")

            if i=="{":
                if "}" in arr:
                    arr.remove("}")
                else:
                    arr.append("}")
        return True if not arr else False

