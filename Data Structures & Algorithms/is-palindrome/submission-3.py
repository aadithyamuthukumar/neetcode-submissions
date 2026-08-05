class Solution:
    def isPalindrome(self, s: str) -> bool:

        cleanedS = []

        for char in s:
            if char.isalnum():
                cleanedS.append(char.lower())

        l = 0
        r = len(cleanedS) - 1

        while l < r:
            if cleanedS[l].lower() != cleanedS[r].lower():
                return False
            l += 1
            r -= 1

        
        return True
