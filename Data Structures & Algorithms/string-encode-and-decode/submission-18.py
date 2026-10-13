class Solution:
    #The encoded string will be in the format of - f'{len(str)#<str>}' -> '2#HI'
    #decode will use pointers and substrings to extract the encoded part.
    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for text in strs:
            encoded += f'{len(text)}#{text}'
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []
        start = 0
        while start < len(s):
            seperator = start
            while s[seperator] != '#':
                seperator += 1

            length = int(s[start:seperator])
            start = seperator + 1
            decoded_text = s[start: start+length]
            decoded.append(decoded_text)
            start += length 
        return decoded

