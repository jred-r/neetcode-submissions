class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for st in strs:
            encoded += str(len(st)) + '#' + st
        return encoded

    def decode(self, s: str) -> List[str]:
        if len(s) == 0:
            return []
            
        decoded = []
        scan = 0
        while scan < len(s):
            next = scan
            while s[next] != '#':
                next += 1

            length = int(s[scan:next])
            scan = next + 1
            decoded.append(s[scan : scan + length])
            scan += length
        
        return decoded


