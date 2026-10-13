class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n  = len(s)
        if n <= 1:
            return n

        left = 0
        right = 0
        max_length = 0
        seen = set()

        while right < n:
            if s[right] not in seen:
                seen.add(s[right])
                current_length = right - left + 1
                max_length = max(max_length, current_length)
                right += 1
            else:
                seen.remove(s[left])
                left += 1
       
        return max_length