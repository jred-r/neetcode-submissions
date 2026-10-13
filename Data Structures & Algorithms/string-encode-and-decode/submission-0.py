class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for str in strs:
            encoded+= f'{len(str)}#{str}'
        return encoded
    
    def decode(self, s: str) -> List[str]:
        #base case
        if len(s) == 0:
            return []
        
        decoded = []
        start = 0
        while start < len(s):
            end =  start
            while s[end] != '#':
                end+=1
            length =int(s[start:end])
            start = end + 1
            end = start + length
            decoded.append(s[start:end])
            start = end

        return decoded