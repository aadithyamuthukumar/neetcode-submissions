class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        sMap = {}
        tMap = {}

        for char in s:
            sMap[char] = 1 + sMap.get(char, 0)
        for char2 in t:
            tMap[char2] = 1 + tMap.get(char2, 0)
        
        return sMap == tMap        