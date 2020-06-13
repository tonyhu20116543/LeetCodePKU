class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        memo = {}
        return self.dfs(s1, s2, memo=memo)

    def dfs(self, s1, s2, memo={}):
        # check the sorted is fundamental
        if len(s1) != len(s2) or sorted(s1) != sorted(s2):
            return False
        if len(s1) <= 1 and len(s2) <= 1:
            return s1 == s2
        if s1 == s2:
            return True
        if (s1, s2) in memo:
            return memo[s1, s2]
        
        for i in range(1, len(s1)):
            a = self.dfs(s1[:i], s2[:i], memo) and self.dfs(s1[i:], s2[i:], memo)
            if not a:
                b = self.dfs(s1[:i], s2[-i:], memo) and self.dfs(s1[i:], s2[:-i], memo)
            if a or b:
                memo[s1, s2] = True
                return True
        
        memo[s1, s2] = False
        return False