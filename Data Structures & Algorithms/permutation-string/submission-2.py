class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        freq1 = [0] * 26
        freq2 = [0] * 26

        for ch in s1:
            freq1[ord(ch) - ord('a')] += 1

        window = len(s1)

        for ch in s2[:window]:
            freq2[ord(ch) - ord('a')] += 1

        if freq1 == freq2:
            return True

        for i in range(window, len(s2)):
            freq2[ord(s2[i]) - ord('a')] += 1
            freq2[ord(s2[i - window]) - ord('a')] -= 1

            if freq1 == freq2:
                return True

        return False
