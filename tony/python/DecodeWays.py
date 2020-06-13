class Solution:
    # Best solution
    def numDecodings(self, s: str) -> int:
        if len(s) == 0 or s[0] == '0':
            return 0
        
        s = [ord(c) - ord('0') for c in s]
        dp1, dp2 = 1, 1
        dp = 0
        for i in range(1, len(s)):
            dp = 0
            if s[i] != 0:
                dp += dp2
            if 0 < s[i] + s[i - 1] * 10 <= 26 and s[i - 1] != 0:
                dp += dp1
            dp1 = dp2
            dp2 = dp
        
        return dp2
    
#     def numDecodings(self, s: str) -> int:
#         # dp[i] = dp[i - 1] + dp[i - 2]
#         s = [ord(c) - ord('0') for c in s]
#         dp = [0] * (len(s) + 1)
#         dp[0] = 1
#         for i in range(1, len(s) + 1):
#             if s[i - 1] != 0:
#                 dp[i] += dp[i - 1]
#             if i - 2 >= 0 and 0 < s[i - 1] + 10 * s[i - 2] <= 26 and s[i - 2] != 0:
#                 dp[i] += dp[i - 2]
        
#         return dp[len(s)]