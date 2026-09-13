class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        combs = []
        self.helper(1, [], n, k, combs)
        return combs

    def helper(self, i, currComb, n, k, combs):
        if len(currComb) == k:
            combs.append(currComb.copy())
            return
        if i > n:
            return

        currComb.append(i)
        self.helper(i + 1, currComb, n, k, combs)

        currComb.pop()
        self.helper(i + 1, currComb, n, k, combs)