

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        final_list = []
        for string in strs:
            key = "".join(sorted(string))
            hashmap[key].append(string)
        for key in hashmap:
            final_list.append(hashmap[key])
        return final_list
        


        