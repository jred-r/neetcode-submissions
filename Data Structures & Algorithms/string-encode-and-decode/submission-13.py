class Solution:
    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for text in strs:
            encoded += f"{len(text)}#{text}"
        return encoded

    def decode(self, s: str) -> List[str]:
        if len(s) == 0:
            return []

        decoded = []
        start = 0
        while start < len(s):
            scan = start
            while s[scan] != "#":
                scan += 1
            span = int(s[start:scan])
            start = scan + 1
            decoded.append(s[start : start + span])
            start += span

        return decoded
