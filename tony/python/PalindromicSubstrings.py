class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[0] * n for _ in range(n)]  # dp[i][j] = 1 is substring [i:j] is palindromic
        count = 0
        
        for i in range(n):
            for j in range(i, -1, -1):
                if s[i] == s[j] and (i - j <= 2 or dp[i - 1][j + 1] == 1):
                    dp[i][j] = 1
                    count += 1 if dp[i][j] == 1 else 0
                    
        return count