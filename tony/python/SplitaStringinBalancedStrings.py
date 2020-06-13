class Solution:
    def balancedStringSplit(self, s: str) -> int:
        res = 0
        cnt = 0
        for c in s:
            cnt += 1 if c == 'L' else -1
            res += 1 if cnt == 0 else 0
        
        return res