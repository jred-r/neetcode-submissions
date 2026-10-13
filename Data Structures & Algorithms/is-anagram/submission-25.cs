public class Solution {
    public bool IsAnagram(string s, string t) {
        if (s.Length != t.Length){
            return false;
        }

        int[] freq = new int[26];
        for(int index = 0; index < s.Length; index++)
        {
            freq[s[index] - 'a'] += 1;
            freq[t[index] - 'a'] -= 1;
        }

        foreach(int index in freq)
        {
            if (index != 0)
            {
                return false;
            }
        }
        return true;
    }
}
