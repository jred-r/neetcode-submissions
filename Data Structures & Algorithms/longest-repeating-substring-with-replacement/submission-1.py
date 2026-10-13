class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        freq = defaultdict(int)
        longest, left, maxFreq = 0, 0, 0
        for right in range(n):
            freq[s[right]] += 1
            maxFreq = max(maxFreq, freq[s[right]])
            while (self.getWindowSize(left, right) - maxFreq > k):
                #reduce window
                freq[s[left]] -= 1
                left += 1
            window_size = self.getWindowSize(left, right)
            longest = max(window_size, longest)
        
        return longest

    def getWindowSize(self, left, right):
        return right - left + 1