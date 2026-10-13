class Solution:
    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        res = ""
        for st in strs:
            res += str(len(st)) + "#" + st
        return res

    def decode(self, s: str) -> List[str]:
        if len(s) == 0:
            return []
        scan = 0
        res = []
        while scan < len(s):
            next = scan
            while s[next] != "#":
                next += 1

            length = int(s[scan:next])
            scan = next + 1
            res.append(s[scan : scan + length])
            scan += length

        return res
