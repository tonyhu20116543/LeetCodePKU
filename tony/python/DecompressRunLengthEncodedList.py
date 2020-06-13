class Solution:
    # Best solution
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        res = []
        ks = []
        vs = []
        for i in range(0, len(nums), 2):
            ks.append(nums[i])
            vs.append(nums[i + 1])
        
        for k, v in zip(ks, vs):
            res.extend([v] * k)
            
        return res
    
#     def decompressRLElist(self, nums: List[int]) -> List[int]:
#         res = []
#         for i in range(0, len(nums), 2):
#             k = nums[i]
#             v = nums[i + 1]
#             while k != 0:
#                 res.append(v)
#                 k -= 1
        
#         return res