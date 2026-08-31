class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)
        while len(stones) > 1:
            x = heapq.heappop_max(stones)
            y = heapq.heappop_max(stones)
            if x == y:
                continue
            elif x < y:
                diff = y - x
                heapq.heappush_max(stones, diff)
            else:
                diff = x - y
                heapq.heappush_max(stones, diff)
        if stones:
            return stones[0]
        else:
            return 0