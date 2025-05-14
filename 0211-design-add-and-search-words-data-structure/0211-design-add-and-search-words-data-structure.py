'''
Trie
root = #
    |
[b, d, m]

search
p not in children of root: return False
. then sear all children -> recursively -> dfs
if found then return true


class node = letter, children


in init

initialie the root

in add word:
start from root
and move letter by letter in the new word
    if child is present then move to the child node 
    if it is not then add a node with that letter and then move to it



in search

i will start with the 1st letter and the root
if it is a . then traverse through all the children
if it is a letter present in the children then move to the next
not present return False
if all traversal complete return True


'''
class tNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False


class WordDictionary:

    def __init__(self):

        self.root = tNode()


    def addWord(self, word: str) -> None:

        currnode = self.root

        for currletter in word:

            if currletter in currnode.children:
                currnode = currnode.children[currletter]
            else:
                currnode.children[currletter] = tNode()
                currnode = currnode.children[currletter]

        currnode.isEnd = True


    

    def search(self, word: str) -> bool:
        def helper( node, i):
            if i == len(word):
                return node.isEnd
        
            if word[i] == '.':
                for c in node.children.values():
                    if helper(c, i+1):
                        return True
                return False
            elif word[i] not in node.children:
                return False
            else:
                return helper(node.children[word[i]], i+1)
        currnode = self.root
        return helper(currnode, 0)
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)