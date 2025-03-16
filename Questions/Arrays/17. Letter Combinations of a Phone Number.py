from typing  import List
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        letters = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        def backtrack(index, path):
            if len(path) == len(digits):
                res.append(path)
                return

            for char in letters[digits[index]]:
                backtrack(index + 1, path + char)

        res = []
        backtrack(0, "")
        return res

if __name__=="__main__":

    digits = "23"
    print(Solution().letterCombinations(digits))