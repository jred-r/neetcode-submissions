class Solution:

    def encode(self, strs: List[str]) -> str:
        #we can add the length of the string and a seperator
        # -> for ex: "5#hello"
        encoded = ""
        for text in strs:
            encoded += f"{len(text)}#{text}"
        return encoded

    def decode(self, s: str) -> List[str]:
        #input will be "5#hello5#there"
        #need to iterate till we hit the '#' and take everything before that.
        #use 2 pointers.
        scan = 0
        seperator = 0
        res = []
        while seperator < len(s):
            if s[seperator] != '#':
                seperator += 1
                continue
            
            length = int(s[scan : seperator])
            scan = seperator + 1
            res.append(s[scan : scan + length])
            scan +=length
            seperator = scan

        return res
