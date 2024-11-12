class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0  

        char_map = {}
        max_len = 0
        left = 0

        for right in range(len(s)):
            if s[right] in char_map and char_map[s[right]] >= left:
                left = char_map[s[right]] + 1
            char_map[s[right]] = right
            max_len = max(max_len, right - left + 1)

        return max_len


