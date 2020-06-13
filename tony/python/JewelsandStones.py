class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        cnt = {}
        for c in J:
            cnt[c] = 0
        
        sum = 0
        for c in S:
            if c in cnt:
                sum += 1
        
        return sum
        