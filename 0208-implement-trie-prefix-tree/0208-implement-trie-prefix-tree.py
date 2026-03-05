class Trie:

    def __init__(self):
        self.children: dict = {} # map char to TrieNode(char)
        self.is_end_of_word: bool = False
        
    def insert(self, word: str) -> None:
        node = self
        for c in word:
            if c not in node.children:# if a key hasnt been made
                node.children[c] = Trie()
            node = node.children[c]
        node.is_end_of_word = True

    def search(self, word: str) -> bool:
        node = self
        for c in word:
            if c not in node.children:
                return False
            node = node.children[c]
        return node.is_end_of_word

    def startsWith(self, prefix: str) -> bool:
        node = self
        for c in prefix:
            if c not in node.children:
                return False
            node = node.children[c]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)