class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count_s = {}
        count_t = {}

        for index in range(len(s)):
            count_s[s[index]] =  count_s.get(s[index],0) +1
            count_t[t[index]] = count_t.get(t[index], 0) +1
        
        return count_s == count_t