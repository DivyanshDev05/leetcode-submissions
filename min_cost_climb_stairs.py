class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        c1 = c2 = 0
        n = len(cost)
        for i in range(2, n+1):
            cur = c1
            c1 = min(c1+cost[i-1], c2+cost[i-2])
            c2 = cur
        return c1