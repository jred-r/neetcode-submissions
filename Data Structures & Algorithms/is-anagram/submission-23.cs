public class Solution {
    public bool IsAnagram(string s, string t) {
        // Base case compare the string length
        if (s.Length != t.Length) {
            return false;
        }

        int[] freq = new int[26];

        for (int i = 0; i < s.Length; i++) {
            freq[s[i] - 'a']++;
            freq[t[i] - 'a']--;
        }

        return freq.All(x => x == 0);
    }
}
