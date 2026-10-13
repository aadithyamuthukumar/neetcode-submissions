class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        l = 0

        s1Freq = [0] * 26
        s2Freq = [0] * 26

        for c in s1:
            s1Freq[ord(c) - ord('a')] += 1
        
        for r, c in enumerate(s2):
            if r - l + 1 > len(s1):
                s2Freq[ord(s2[l]) - ord('a')] -= 1
                l += 1
            s2Freq[ord(c) - ord('a')] += 1

            if s1Freq == s2Freq:
                return True
        
        return False