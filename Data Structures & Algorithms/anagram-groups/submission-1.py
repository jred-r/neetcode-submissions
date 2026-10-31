class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped = defaultdict(list)
        def hash(text:str):
            res = [0] * 26
            for ch in text:
                res[ord(ch) - ord('a')] += 1
            return res

        for text in strs:
            computed_hash = hash(text)
            grouped[tuple(computed_hash)].append(text)
        
        return list(grouped.values())
        