class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Naive approach wil be to compare each element
        in the first string with the corresponding element in the
        other string. This will be O(n^2).


        An efficient approach will be to assign the string to a set
        """

        # base case, compare the length of the strings.
        if len(s) != len(t):
            return False

        # declare two dictionaries and add the number of occurances of each charcter,
        # at the end, compare if both the dictionaries are the same.
        count_s = {}
        count_t = {}

        for i in range(len(s)):
            count_s[s[i]] = count_s.get(s[i], 0) + 1
            count_t[t[i]] = count_t.get(t[i], 0) + 1

        return count_t == count_s
