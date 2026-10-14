class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        l = 0

        s1Count = [0] * 26
        s2Count = [0] * 26

        for c in s1:
            s1Count[ord(c)- ord('a')] += 1


        for r, c in enumerate(s2):


            if r - l + 1 > len(s1):
                s2Count[ord(s2[l])- ord('a')] -= 1
                l += 1

            s2Count[ord(c)- ord('a')] += 1


            if s1Count == s2Count:
                return True
        
        return False
