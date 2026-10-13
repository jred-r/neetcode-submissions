class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
       #base case
        if(len(s) != len(t)):
            return False
        
        #assign both strings to a dictionary, which holds the char and the occurance count
        count_s1 = {}
        count_s2 = {}

        for i in range(len(s)):
            count_s1[s[i]] = count_s1.get(s[i], 0) +1
            count_s2[t[i]] = count_s2.get(t[i], 0) + 1
                
        return count_s1 == count_s2

        