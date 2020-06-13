class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        p = [[0] * n for _ in range(n)]
        dp = [0] * (n + 1)
        
        for i in range(n, -1, -1):
            dp[i] = n - 1 - i
            
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i <= 2 or p[i + 1][j - 1]):
                    p[i][j] = 1
                    dp[i] = min(dp[i], dp[j + 1] + 1)
                    
        return dp[0]