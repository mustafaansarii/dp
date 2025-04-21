class trienode:
    def __init__(self):
        self.links = [None] * 26  # Each node has its own array
        self.flag = False  # Each node has its own end marker

    def containsKey(self, ch):
        return self.links[ord(ch) - ord('a')] is not None

    def put(self, ch, node):
        self.links[ord(ch) - ord('a')] = node

    def get(self, ch):
        return self.links[ord(ch) - ord('a')]

    def setEnd(self):
        self.flag = True

    def isEnd(self):
        return self.flag


class Trie:
    def __init__(self):
        self.root = trienode()

    def insert(self, word: str):
        node = self.root
        for ch in word:
            if not node.containsKey(ch):
                node.put(ch, trienode())
            node = node.get(ch)
        node.setEnd()

    def search(self, word: str) -> bool:
        node = self.root
        for ch in word:
            if not node.containsKey(ch):
                return False
            node = node.get(ch)
        return node.isEnd()

    def isPrefix(self, prefix: str) -> bool:
        node = self.root
        for ch in prefix:
            if not node.containsKey(ch):
                return False
            node = node.get(ch)
        return True

    def deleteHelper(self, root, key, depth):
        if depth == len(key):
            if root.isEnd():
                root.flag = False
                return not any(root.links)
            return False

        ch = key[depth]
        if not root.containsKey(ch):
            return False
        shouldDeleteCurrentNode = self.deleteHelper(root.get(ch), key, depth + 1)

        if shouldDeleteCurrentNode:
            root.put(ch, None)
            return not root.isEnd() and not any(root.links)
        return False

    def delete(self, key):
        if not self.search(key):
            return
        self.deleteHelper(self.root, key, 0)





if __name__ == "__main__":
    keys = ["the", "a", "there", "answer", "any",
            "by", "bye", "their", "abc"]

    # Trie object
    t = Trie()

    # Construct trie
    for key in keys:
        t.insert(key)

    # Search for different keys
    print(t.search("the"))
    print(t.search("these"))
    print(t.search("their"))
    print(t.search("thaw"))
    print(t.isPrefix("th"))
