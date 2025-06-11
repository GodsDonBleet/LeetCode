class Solution(object):
    def ATOI(self, s):
        for i in range(len(s)):
            if s[i] != ' ':
                break
        else:
            return 0

        sign = 1
        if s[i] == '-':
            sign = -1
            i += 1
        elif s[i] == '+':
            i += 1    
        s = s[i:]
        
        num_str = ""
        for char in s:
            if char.isdigit():
                num_str += char
            else:
                break
        if not num_str:
            return 0

        x = sign * int(num_str)
        if x < -2**31:
            return -2**31
        elif x > 2**31 - 1:
            return 2**31 - 1
        else:
            return x    

