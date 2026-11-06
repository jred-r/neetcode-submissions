class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_set = set(s)
        n = len(s)
        longest = 0

        for ch in char_set:
            count = left = 0
            for right in range(n):
                if s[right] == ch:
                    count += 1
                
                while(right - left + 1) - count > k:
                    if s[left] == ch:
                        count -= 1
                    left += 1
                
                longest = max(longest, right - left + 1)
                
        return longest
        