class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False


class PrefixTree:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        current = self.root
        for ch in word:
            if ch not in current.children:
                current.children[ch] = TrieNode()
            current = current.children[ch]
        current.isEnd = True

    def search(self, word: str) -> bool:
        last = self.moveToEnd(word)
        return True if last and last.isEnd else False

    def startsWith(self, prefix: str) -> bool:
        return True if self.moveToEnd(prefix) else False

    def moveToEnd(self, text):
        current = self.root
        for ch in text:
            if ch not in current.children:
                return None
            current = current.children[ch]
        return current
