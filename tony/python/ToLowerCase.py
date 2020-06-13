class Solution:
    def toLowerCase(self, str: str) -> str:
        low_str = ''
        for i in range(len(str)):
            x = ord(str[i])
            if x >= ord('A') and x <= ord('Z'):
                x += ord('a') - ord('A')
                low_str += chr(x)
            else:
                low_str += str[i]
                
        return low_str