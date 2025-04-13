class letterNode:
    def __init__(self, letter=None, isEnd=False):
        self.letter = letter
        self.isEnd = isEnd 
        self.children = {}

class Trie:

    def __init__(self):
        self.root = letterNode()

    def insert(self, word: str) -> None:
        if not word:
            return
       
        node  = self.root
        wordend = len(word) 
        for w in range(wordend):
            if word[w] not in node.children:
                newNode = letterNode(word[w], False)
                node.children[word[w]] = newNode
                node = newNode
            else:
                node = node.children[word[w]]
        node.isEnd = True
            


    def search(self, word: str) -> bool:
        if not word:
            return True
        
        node = self.root
        for w in word:
            if w in node.children:
                node = node.children[w]
            else:
                return False
        return node.isEnd
            



    def startsWith(self, prefix: str) -> bool:
        if not prefix:
            return True
        node = self.root
        for w in prefix:
            if w in node.children:
                node = node.children[w]
            else:
                return False
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)