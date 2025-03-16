from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        maps = {}
        for i in strs:
            key = tuple(sorted(i))
            maps[key] = maps.get(key, []) + [i]

        res=[]
        print(maps)
        for i in maps:
            res.append(maps[i])
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
