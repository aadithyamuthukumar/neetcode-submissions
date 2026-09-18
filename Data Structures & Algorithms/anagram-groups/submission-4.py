class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hashmap = defaultdict(list)
        res = []
        for word in strs:
            key = ''.join(sorted(word))
            hashmap[key].append(word)
        
        res = list(hashmap.values())
        return res