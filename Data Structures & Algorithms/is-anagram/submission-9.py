class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        return self.hash_func(s) == self.hash_func(t)
    
    def hash_func(self, text: str) :
        freq = [0] * 26
        for ch in text:
            freq[ord(ch) - ord('a')] += 1
        return freq

        