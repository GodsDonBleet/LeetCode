'''

class Solution(object):
    def strStr(self, haystack, needle):
        if not needle:
            return 0
        if not haystack or len(needle) > len(haystack):
            return -1
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i + len(needle)] == needle:
                return i
        return -1
        
'''

class Solution(object):
    def strStr(self, haystack, needle):
        return haystack.find(needle)


 