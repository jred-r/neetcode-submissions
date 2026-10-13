class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        n = len(s)
        longest = 0
        seen = set()
        while r < n:
            if s[r] not in seen:
                seen.add(s[r])
                r += 1
                longest = max(r-l, longest)
            else:
                seen.remove(s[l])
                l += 1
                
        return longest
        