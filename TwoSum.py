class Solution(object):
    def twoSum(self, nums, target):
        num_to_index={}
        for i, num in enumerate(nums):
            if target - num in num_to_index:
                return [num_to_index[target - num], i]
            num_to_index[num]=i

solution = Solution()

nums = [2, 7, 11, 15]
target = 9                
print(solution.twoSum(nums, target))
        