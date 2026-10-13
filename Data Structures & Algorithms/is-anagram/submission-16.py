class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #base case, we need both strings to be of equal length
        if len(s) != len(t):
            return False
        #we create two dictionaries and assign the count of each char
        counter_s = {}
        counter_t = {}

        for index in range(len(s)):
            counter_s[s[index]] = counter_s.get(s[index], 1) + 1
            counter_t[t[index]] = counter_t.get(t[index], 1) + 1
        
        return counter_s == counter_t




        