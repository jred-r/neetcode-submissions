class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False


class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        current = self.root
        for ch in word:
            if ch not in current.children:
                current.children[ch] = TrieNode()
            current = current.children[ch]
        current.isEnd = True

    def search(self, word: str) -> bool:
        word_len = len(word)

        def dfs(start_idx, node):
            trie_node = node

            for pos in range(start_idx, word_len):
                char = word[pos]

                if char == ".":
                    for child_node in trie_node.children.values():
                        if dfs(pos + 1, child_node):
                            return True
                    return False

                if char not in trie_node.children:
                    return False

                trie_node = trie_node.children[char]

            return trie_node.isEnd

        return dfs(0, self.root)
