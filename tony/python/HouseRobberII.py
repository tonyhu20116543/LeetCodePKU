class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) <= 2:
            return max(nums)

        m1 = self.rob_once(nums[:-1])
        m2 = self.rob_once(nums[1:])
        
        return max(m1, m2)
        
    def rob_once(self, nums):
        if len(nums) == 0:
            return 0
        if len(nums) <= 2:
            return max(nums)
        
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        
        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
            
        return dp[-1]