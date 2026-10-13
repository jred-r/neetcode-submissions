class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""#we encode with len(str) then # adn then string content
        for text in strs:
            encoded = f'{encoded}{len(text)}#{text}'
        return encoded


    def decode(self, s: str) -> List[str]:
        res = []
        start = 0
        while start < len(s):
            sep_pos = start
            while s[sep_pos] != '#':
                sep_pos += 1
            
            str_len = int(s[start:sep_pos])

            start = sep_pos + 1            
            print(start, start+str_len)

            txt = s[start : (start + str_len)]
            res.append(txt)
            print(txt)

            start = start + str_len
            sep_pos = start

        return res