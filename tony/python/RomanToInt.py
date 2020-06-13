class Solution:
    def romanToInt(self, s: str) -> int:
        map = {'I': 1, 
               'V': 5,
               'X': 10, 
               'L': 50,
               'C': 100,
               'D': 500,
               'M': 1000}
        
        num = 0
        for i in range(len(s)):
            if i > 0 and map[s[i]] > map[s[i - 1]]:
                num += map[s[i]] - 2 * map[s[i - 1]]  # Note, we have already added s[i - 1] one time
            else:
                num += map[s[i]]
                
        return num