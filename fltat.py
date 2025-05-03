class Solution:
    def repeatedCharacter(self, s: str) -> str:
        strMap = {}
        n = len(s)
        for i in range(n):
            if s[i] in strMap:
                return s[i]
            strMap[s[i]] = 1