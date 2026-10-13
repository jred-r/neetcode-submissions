class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        return self.hash(s) == self.hash(t)
        

    def hash(self, text:str):
        freq = [0] * 26
        for ch in text:
            freq[ord(ch) - ord('a')] += 1
        return freq
        