class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n <= 1:
            return n

        x = 0
        y = 0
        longest = 0
        seen = set()
        while y < n:
            if s[y] not in seen:
                seen.add(s[y])
                curr = y - x + 1
                longest = max(longest, curr)
                y += 1
            else:
                seen.remove(s[x])
                x += 1

        return longest
