class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False
        x_str=str(x)
        return x_str == x_str[::-1]

solutions=Solution()

x = int(input())                
output = solutions.isPalindrome(x)
print(str(output).lower())