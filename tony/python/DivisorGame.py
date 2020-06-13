class Solution:
    def divisorGame(self, N: int) -> bool:
        dp = [0] * (N + 1)
        dp[1] = 0
        for i in range(2, N+1):
            dp[i] = 1 if dp[i - 1] == 0 else 0
            
        return dp[N]