class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        return self._gen_hash(s) == self._gen_hash(t)

    def _gen_hash(self, source:str)->List[int]:
        freq:List[int] = [0] * 26
        for ch in source:
            freq[ord(ch) - ord('a')] += 1          
        return freq