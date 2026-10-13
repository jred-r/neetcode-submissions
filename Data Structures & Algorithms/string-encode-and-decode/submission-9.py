class Solution:
    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for text in strs:
            encoded += str(len(text)) + "#" + text
        return encoded

    def decode(self, s: str) -> List[str]:
        if len(s) == 0:
            return []

        res = []
        position = 0
        while position < len(s):
            delimiter_position = position
            while s[delimiter_position] != "#":
                delimiter_position += 1

            length = int(s[position:delimiter_position])
            position = delimiter_position + 1
            res.append(s[position : position + length])
            position += length
        return res
