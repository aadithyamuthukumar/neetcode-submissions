class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counts_s = {}
        counts_t = {}
        for char in s:
            counts_s[char] = counts_s.get(char,0) + 1
        for char2 in t:
            counts_t[char2] = counts_t.get(char2,0) + 1
        if (counts_s == counts_t):
            return True
        else:
            return False

        