class NumArray:

    def __init__(self, nums: List[int]):
        dp = [0] * (len(nums) + 1)
        dp[0] = 0
        for i in range(1, len(nums) + 1):
            dp[i] += dp[i - 1] + nums[i - 1]
            
        self.dp = dp

    def sumRange(self, i: int, j: int) -> int:
        return self.dp[j + 1] - self.dp[i]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)