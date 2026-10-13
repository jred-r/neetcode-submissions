class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n <= 1:
            return n

        left = 0
        right = 0
        seen = set()
        longest = 0

        while right < n:
            right_char, left_char = s[right], s[left]
            if right_char in seen:
                seen.remove(left_char)
                left += 1
            else:
                seen.add(right_char)
                right += 1
                longest = max(longest, right - left)
                
        return longest




        