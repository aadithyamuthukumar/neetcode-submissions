class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        set_of_letters1 = {}
        set_of_letters2 = {}

        for char in s:
            set_of_letters1[char] = set_of_letters1.get(char, 0) + 1
        for char2 in t:
            set_of_letters2[char2] = set_of_letters2.get(char2, 0) + 1
            
                
        return set_of_letters1 == set_of_letters2


        