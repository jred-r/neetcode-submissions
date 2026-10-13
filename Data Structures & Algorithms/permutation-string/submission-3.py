class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_len = len(s1)
        s2_len = len(s2)
        if s1_len > s2_len:
            return False
        
        s1_freq = [0] * 26
        s2_freq = [0] * 26

        for ch in s1:
            s1_freq[ord(ch) - ord('a')] += 1
        
        for index in range(s1_len):
            s2_freq[ord(s2[index]) - ord('a')] += 1
        
        if s1_freq == s2_freq:
            return True
        
        for index in range(s1_len, s2_len):
            s2_freq[ord(s2[index]) - ord('a')] += 1
            s2_freq[ord(s2[index - s1_len]) - ord('a')] -= 1

            if s1_freq == s2_freq:
                return True

        return False

        