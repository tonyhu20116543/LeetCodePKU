class Solution:
    def intToRoman(self, num: int) -> str:
        map = {1: 'I',
               4: 'IV',
               5: 'V',
               9: 'IX',
               10: 'X',
               40: 'XL',
               50: 'L',
               90: 'XC',
               100: 'C',
               400: 'CD',
               500: 'D',
               900: 'CM',
               1000: 'M'}
        
        pair = sorted(map.items(), key=lambda k: k[0], reverse=True)
        
        roman_str = ''
        i = 0
        while num > 0:
            count = num // pair[i][0]
            num %= pair[i][0]
            while count > 0:
                roman_str += pair[i][1]
                count -= 1
            i += 1
                
        return roman_str