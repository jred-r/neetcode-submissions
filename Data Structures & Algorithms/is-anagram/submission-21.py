class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #base case
        if len(s) != len(t):
            return False
        #declare two def dict
        count_s = defaultdict(int)
        count_t = defaultdict(int)

        
        for index in range(len(s)):
            count_s[s[index]]+= 1
            count_t[t[index]]+=1

        return count_s == count_t