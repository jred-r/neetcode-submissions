class Solution:

    def encode(self, strs: List[str]) -> str:
        #-> <strlen><seperator><str>
        encoded = []
        for text in strs:
            encoded.append(f"{len(text)}#{text}")
        return "".join(encoded)
        

    def decode(self, s: str) -> List[str]:
        decoded = []
        left = 0
        right = 0
        n = len(s)
        while left < n:
            while s[right] != '#':
                right += 1
            print(left, right)
            txt_len = int(s[left:right])
            left = right + 1
            text = s[left : left + txt_len]
            decoded.append(text)
            left = left + txt_len
            right = left
        return decoded



