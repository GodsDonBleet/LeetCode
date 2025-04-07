class Solution(object):
    def lengthOfLongestSubstring(self, s):
        char_index_map = {}
        left = 0
        max_length = 0

        for right, char in enumerate(s):
            if char in char_index_map and char_index_map[char] >= left:
                left = char_index_map[char] + 1
            char_index_map[char] = right
            max_length = max(max_length, right - left +1)

        return max_length    

solutions = Solution()

s = "abcabcbb"
print(solutions.lengthOfLongestSubstring(s))        