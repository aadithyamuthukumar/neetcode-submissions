

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashTable = defaultdict(list)

        for str in strs:
            hashTable[''.join(sorted(str))].append(str)
        return list(hashTable.values())