class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # dp[k][i] = max(dp[k][i - 1], max(prices[i] - prices[j] + dp[k - 1][j - 1])),
        #            j \in [0, i - 1]
        
        if len(prices) < 2:
            return 0
        
        K = 2
        n = len(prices)
        dp = [[0] * n for _ in range(K + 1)]
        
        for k in range(1, K + 1):
            max_tmp = -prices[0]
            for i in range(1, n):
                dp[k][i] = max(dp[k][i - 1], prices[i] + max_tmp)
                max_tmp = max(max_tmp, dp[k - 1][i - 1] - prices[i])
        
        return dp[2][n-1]