class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        first_word = strs[0]
        for i in range(len(first_word)):
            char_to_match = first_word[i]
            for other_word in strs[1:]:
                # Check for mismatch or index out of bounds
                if i == len(other_word) or other_word[i] != char_to_match:
                    return first_word[:i]
        return first_word
