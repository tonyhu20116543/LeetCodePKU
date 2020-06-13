class Solution:
    # Best solution
    def findNumbers(self, nums: List[int]) -> int:
        return len([x for x in nums if len(str(x)) % 2 == 0])
        
#     def findNumbers(self, nums: List[int]) -> int:
#         k = 0
#         for num in nums:
#             nd = 0
#             while num != 0:
#                 num //= 10
#                 nd += 1
#             k = k + 1 if nd % 2 == 0 else k

#         return k