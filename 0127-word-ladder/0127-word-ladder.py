class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        wordList= set(wordList)
        q = deque()
        q.append((beginWord, 1))
        alphabets='abcdefghijklmnopqrstuvwxyz'
        while q:
            word, steps = q.popleft()
            if word == endWord:
                return steps
            
            for i in range(len(word)):
                for alpha in alphabets:
                    new_word = word[:i]+alpha+word[i+1:]
                    if new_word in wordList:
                        q.append((new_word, steps+1))
                        wordList.remove(new_word)

        return 0
            