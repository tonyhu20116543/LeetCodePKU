class Solution:
    # Best solution: time O(n), space: O(1)
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0
        
        profit = 0
        for i in range(1, len(prices)):
            diff = prices[i] - prices[i - 1]
            if diff > 0:
                profit += diff
        
        return profit

#     def maxProfit(self, prices: List[int]) -> int:
#         if len(prices) == 0:
#             return 0
#         N = len(prices)
#         # dp = [0] * N
#         for i in range(1, N):
#             diff = prices[i] - prices[i - 1]
#             if diff > 0:
#                 dp[i] += dp[i - 1] + diff
#             else:
#                 dp[i] = dp[i - 1]
                
#         return dp[N - 1]
        
            