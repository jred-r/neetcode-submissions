public class Solution {
    public bool IsAnagram(string s, string t) {
        if (t.Length != s.Length)
        {
            return false;   
        }
        int[] freq_s = GenerateHash(s);
        int[] freq_t = GenerateHash(t);

        for(int index = 0; index < freq_s.Length; index++)
        {
            if (freq_s[index] != freq_t[index])
            {
                return false;
            }
        }
        return true;
    }

    public static int[] GenerateHash(string text)
    {
        int[] freq = new int[26];
        for(int index = 0; index < text.Length; index++)
        {
            freq[text[index] - 'a'] += 1;
        }
        return freq;
    }
}
