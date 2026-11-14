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
        node = self.moveToEnd(word)
        if node and node.isEnd:
            return True
        else:
            return False

    def startsWith(self, prefix: str) -> bool:
        node = self.moveToEnd(prefix)
        return True if node else False

    def moveToEnd(self, text):
        current = self.root
        for ch in text:
            if ch not in current.children:
                return None
            current = current.children[ch]
        return current
        
        