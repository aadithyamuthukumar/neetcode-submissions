class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        window = {}
        tCount = {}

        resLen = float("infinity")
        res = [-1, - 1]

        for char in t:
            tCount[char] = 1 + tCount.get(char, 0)
        have, need = 0, len(tCount)
        L = 0
        for R in range(len(s)):
            window[s[R]] = 1 + window.get(s[R], 0)

            if s[R] in tCount and tCount[s[R]] == window[s[R]]:
                have += 1

            while have == need:
                if (R - L + 1) < resLen:
                    res = [L, R]
                    resLen = R - L + 1
                window[s[L]] -= 1
                if s[L] in tCount and window[s[L]] < tCount[s[L]]:
                    have -= 1
                L += 1
        L, R = res
        return s[L: R + 1] if resLen != float("infinity") else ""


