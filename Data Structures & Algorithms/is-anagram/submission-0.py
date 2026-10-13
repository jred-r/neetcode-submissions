class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #base case
        if len(s) != len(t):
            return False
        #this is O(nlogn) - sorting takes nlogn
        """
        #assign to list and sort
        lst1 = list(s)
        lst2 = list(t)
        lst1.sort()
        lst2.sort()
        
        #iterate over and exit out when list entries do not match
        for i in range(0,len(lst1)):
            if lst1[i] != lst2[i]:
                return False
    
        return True """
        #optimized method by using dict, all below steps take O(n)
        #init empty dict
        count_s = {}
        count_t = {}
        # dict will hold char and occurance count
        for c in s:
            count_s[c] = count_s.get(c,0) + 1

        for c in t:
            count_t[c] = count_t.get(c,0) + 1

        return count_s == count_t

        