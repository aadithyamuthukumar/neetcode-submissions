class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def bfs(x):
            if x >= n:
                return x==n
            if x not in memo:
                memo[x] = bfs(x+1) + bfs(x+2)
            return memo[x]
        return bfs(0)