# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair], s=0, e=None) -> List[Pair]:
        if e is None:
            e = len(pairs) - 1
        if e - s + 1 <= 1:
            return pairs
        
        m = (e + s) // 2

        self.mergeSort(pairs, s, m)
        self.mergeSort(pairs, m + 1, e)

        self.merge(pairs, s, m, e)

        return pairs
    
    def merge(self, pairs: List[pair], s:int , m:int, e:int):

        l = pairs[s : m + 1]
        r = pairs[m + 1 : e + 1]


        i = 0
        j = 0
        k = s

        while i < len(l) and j < len(r):
            if l[i].key <= r[j].key:
                pairs[k] = l[i]
                i += 1
            else:
                pairs[k] = r[j]
                j += 1
            k += 1
        
        while i < len(l):
            pairs[k] = l[i]
            i += 1
            k += 1
        
        while j < len(r):
            pairs[k] = r[j]
            j += 1
            k += 1