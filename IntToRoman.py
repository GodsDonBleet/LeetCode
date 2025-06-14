class Solution(object):

    def IntToRoman(self, num):
        IntToRomanMap = [
            (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
            (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
            (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
        ]
        res = ""
        while num > 0:
            for val, symbol in IntToRomanMap:
                while num >= val:
                    res += symbol
                    num -= val
        return res

solutions = Solution()

s = 58
print(solutions.IntToRoman(s))                    

