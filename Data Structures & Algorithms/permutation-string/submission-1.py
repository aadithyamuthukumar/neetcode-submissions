class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        L = 0
        s1Len = len(s1)
        s1_sorted = sorted(s1)

        for R in range(len(s2)):
            
            if R - L + 1 > s1Len:
                L += 1

            if R - L + 1 == s1Len:
                if sorted(s2[L:R+1]) == s1_sorted:
                    return True

        return False