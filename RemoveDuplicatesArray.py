class Solution(object):
    def removeDuplicates(self, nums):
        stack = []
        for num in nums:
            if not stack or stack[-1] != num:
                stack.append(num)
        nums[:] = stack
        return len(stack)
    
    
        