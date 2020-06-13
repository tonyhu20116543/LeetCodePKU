class Solution:
    # O(NlogN)
#     def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
#         num2idx = {}
#         for idx, num in enumerate(sorted(nums)):
#             if num not in num2idx.keys():
#                 num2idx[num] = idx
        
#         return [num2idx[num] for num in nums]
    
    # O(N)
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        count = [0] * 102
        for num in nums:
            count[num + 1] += 1
        
        for i in range(1, len(count)):
            count[i] += count[i - 1]
        
        return [count[num] for num in nums]
        