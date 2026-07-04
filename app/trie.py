class TrieNode:

    def __init__(self):
        self.children = {}
        self.is_end = False
        self.products = []


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str):

        node = self.root

        word = word.lower()

        for char in word:

            if char not in node.children:
                node.children[char] = TrieNode()

            node = node.children[char]

            if word not in node.products:
                node.products.append(word)

        node.is_end = True

    def search_prefix(self, prefix: str):

        node = self.root

        prefix = prefix.lower()

        for char in prefix:

            if char not in node.children:
                return []

            node = node.children[char]

        return sorted(node.products)