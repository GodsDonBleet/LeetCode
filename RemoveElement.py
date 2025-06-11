class Solution(object):
    def removeElement(self, nums, val):
        stack = []
        for num in nums:
            if num != val:
                stack.append(num)
        nums[:] = stack
        return len(stack)
    
    
        