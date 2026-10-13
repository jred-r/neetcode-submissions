from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped = defaultdict(list)

        for text in strs:
            freq = [0] * 26
            for ch in text:
                freq[ord(ch) - ord('a')] += 1
            grouped[tuple(freq)].append(text)
        
        return list(grouped.values())

        