class TrieNode:
    def __init__(self):
        self.chars = {}
        self.end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.chars:
                curr.chars[char] = TrieNode()
            curr = curr.chars[char]
        curr.end = True

    def search(self, word: str) -> bool:
        curr = self.root
        for char in word:
            if char in curr.chars:
                curr = curr.chars[char]
            else:
                return False
        return curr.end        

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for char in prefix:
            if char in curr.chars:
                curr = curr.chars[char]
            else:
                return False
        return True    


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)