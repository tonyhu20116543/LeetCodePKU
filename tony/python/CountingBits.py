class Solution:
    def countBits(self, num: int) -> List[int]:
        dp = [0] * (num + 1)
        for i in range(1, num + 1):
            if i % 2 == 0:
                dp[i] = dp[i >> 1]
            else:
                dp[i] = dp[i >> 1] + 1
        
        return dp