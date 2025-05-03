class Solution:
    def climbStairs(self, n: int) -> int:

        sc = [1, 2, 3] + ([0] * n)
        if n < 4:
            return sc[n-1]
        else:
            for i in range(3, n+1):
                sc[i] = sc[i-1] + sc[i-2]
        return sc[n-1]