class Solution(object):
    def longestCommonPrefix(self, a):
        i = 0
        size = len(a)
        if (size == 0):
            return ""
        if (size ==1):
            return a[0]
        a.sort()
        end = min(len(a[0]), len(a[size - 1]))    
        while(i < end and a[0][i] == a[size - 1][i]):
            i += 1
        pre = a[0][0:i]
        return pre 

solutions = Solution()

a = ["test", "test1", "tes2", "te3"]
print("The longest Common Prefix is :" , solutions.longestCommonPrefix(a))        